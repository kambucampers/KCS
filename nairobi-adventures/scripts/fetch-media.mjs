#!/usr/bin/env node
/**
 * Fetch real photographs for every slot in src/data/media-sources.ts.
 *
 * Sources
 *   Wikimedia Commons  free-licensed photographs of named Nairobi places
 *   Pexels             stock photography, free to use with attribution
 *
 * Usage
 *   npm run media                 fetch anything missing
 *   npm run media -- --force      refetch everything
 *   npm run media -- --only=rhino,amboseli    fetch named slots only
 *
 * The Pexels key is read from PEXELS_API_KEY in .env or the environment.
 * Files land in public/images/ and the manifest is written to src/data/media.json.
 */

import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const imagesDir = path.join(root, 'public', 'images');
const manifestPath = path.join(root, 'src', 'data', 'media.json');

const args = process.argv.slice(2);
const force = args.includes('--force');
const onlyArg = args.find((a) => a.startsWith('--only='));
const only = onlyArg ? onlyArg.split('=')[1].split(',').map((s) => s.trim()) : null;

const MIN_WIDTH = 1400;
const TARGET_WIDTH = 1800;

/** Licences we accept from Wikimedia Commons. Anything else is skipped. */
const FREE_LICENCES = [
  'cc0', 'cc-zero', 'public domain', 'pd',
  'cc by 2.0', 'cc by 3.0', 'cc by 4.0',
  'cc by-sa 2.0', 'cc by-sa 2.5', 'cc by-sa 3.0', 'cc by-sa 4.0',
];

async function loadEnv() {
  const envPath = path.join(root, '.env');
  if (!existsSync(envPath)) return;
  const text = await readFile(envPath, 'utf8');
  for (const line of text.split('\n')) {
    const match = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
    if (match && !process.env[match[1]]) {
      process.env[match[1]] = match[2].replace(/^["']|["']$/g, '');
    }
  }
}

const stripHtml = (s = '') => s.replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim();

async function searchCommons(query) {
  const url =
    'https://commons.wikimedia.org/w/api.php?' +
    new URLSearchParams({
      action: 'query',
      format: 'json',
      origin: '*',
      generator: 'search',
      gsrsearch: `filetype:bitmap ${query}`,
      gsrnamespace: '6',
      gsrlimit: '12',
      prop: 'imageinfo',
      iiprop: 'url|size|extmetadata|mime',
      iiurlwidth: String(TARGET_WIDTH),
    });

  const res = await fetch(url, { headers: { 'User-Agent': 'NairobiAdventuresSiteBuild/1.0 (bookings@nairobiadventures.com)' } });
  if (!res.ok) throw new Error(`Commons search failed: ${res.status}`);
  const data = await res.json();
  const pages = Object.values(data?.query?.pages ?? {});

  for (const page of pages) {
    const info = page.imageinfo?.[0];
    if (!info) continue;
    if (!/^image\/(jpeg|png)$/.test(info.mime ?? '')) continue;
    if ((info.width ?? 0) < MIN_WIDTH) continue;

    const meta = info.extmetadata ?? {};
    const licence = stripHtml(meta.LicenseShortName?.value ?? '').toLowerCase();
    if (!FREE_LICENCES.some((l) => licence.includes(l))) continue;

    return {
      url: info.thumburl ?? info.url,
      width: info.thumbwidth ?? info.width,
      height: info.thumbheight ?? info.height,
      source: 'Wikimedia Commons',
      sourceUrl: info.descriptionurl,
      author: stripHtml(meta.Artist?.value ?? '') || 'Unknown',
      license: stripHtml(meta.LicenseShortName?.value ?? '') || 'See source',
    };
  }
  return null;
}

async function searchPexels(query, orientation = 'landscape') {
  const key = process.env.PEXELS_API_KEY;
  if (!key) return null;

  const url =
    'https://api.pexels.com/v1/search?' +
    new URLSearchParams({ query, orientation, per_page: '10', size: 'large' });

  const res = await fetch(url, { headers: { Authorization: key } });
  if (res.status === 429) throw new Error('Pexels rate limit reached, wait an hour and rerun');
  if (!res.ok) throw new Error(`Pexels search failed: ${res.status}`);
  const data = await res.json();

  const photo = (data.photos ?? []).find((p) => p.width >= MIN_WIDTH);
  if (!photo) return null;

  return {
    url: photo.src.large2x ?? photo.src.large,
    width: 1880,
    height: Math.round((1880 * photo.height) / photo.width),
    source: 'Pexels',
    sourceUrl: photo.url,
    author: photo.photographer,
    authorUrl: photo.photographer_url,
    license: 'Pexels License',
  };
}

async function download(url, destination) {
  const res = await fetch(url, { headers: { 'User-Agent': 'NairobiAdventuresSiteBuild/1.0' } });
  if (!res.ok) throw new Error(`Download failed: ${res.status}`);
  const buffer = Buffer.from(await res.arrayBuffer());
  await writeFile(destination, buffer);
  return buffer.length;
}

async function main() {
  await loadEnv();
  await mkdir(imagesDir, { recursive: true });

  const mediaSlots = JSON.parse(
    await readFile(path.join(root, 'src', 'data', 'media-sources.json'), 'utf8')
  );

  let manifest = {};
  try {
    manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
  } catch {
    manifest = {};
  }

  const slots = mediaSlots.filter((s) => !only || only.includes(s.key));
  let fetched = 0;
  let skipped = 0;
  const failures = [];

  for (const slot of slots) {
    const existing = manifest[slot.key];
    if (existing && !force && existsSync(path.join(root, 'public', existing.file))) {
      skipped += 1;
      continue;
    }

    const order = slot.prefer === 'commons' ? ['commons', 'pexels'] : ['pexels', 'commons'];
    let found = null;

    for (const source of order) {
      try {
        found =
          source === 'commons'
            ? await searchCommons(slot.commons)
            : await searchPexels(slot.pexels, slot.orientation ?? 'landscape');
      } catch (error) {
        console.warn(`  ${slot.key}: ${source} error, ${error.message}`);
      }
      if (found) break;
    }

    if (!found) {
      failures.push(slot.key);
      console.warn(`  ${slot.key}: nothing suitable found, the graphic fallback stays in place`);
      continue;
    }

    const extension = found.url.toLowerCase().includes('.png') ? 'png' : 'jpg';
    const fileName = `${slot.key}.${extension}`;
    const bytes = await download(found.url, path.join(imagesDir, fileName));

    manifest[slot.key] = {
      file: `/images/${fileName}`,
      width: found.width,
      height: found.height,
      source: found.source,
      sourceUrl: found.sourceUrl,
      author: found.author,
      ...(found.authorUrl ? { authorUrl: found.authorUrl } : {}),
      license: found.license,
      fetchedAt: new Date().toISOString().slice(0, 10),
    };

    fetched += 1;
    console.log(
      `  ${slot.key}: ${found.source}, ${found.author}, ${Math.round(bytes / 1024)} KB, ${found.license}`
    );
  }

  const ordered = Object.fromEntries(Object.keys(manifest).sort().map((k) => [k, manifest[k]]));
  await writeFile(manifestPath, JSON.stringify(ordered, null, 2) + '\n');

  console.log(`\nFetched ${fetched}, already present ${skipped}, unmatched ${failures.length}`);
  if (failures.length) console.log(`Unmatched slots: ${failures.join(', ')}`);
  console.log('Manifest written to src/data/media.json. Run npm run build to bake the images in.');
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
