/**
 * Photo slots used across the site.
 *
 * The slot definitions live in media-sources.json so that both Astro and the
 * plain Node script in scripts/fetch-media.mjs read exactly the same list.
 *
 * `npm run media` fills these from Wikimedia Commons and the Pexels API, writing
 * the files into public/images/ and the manifest into src/data/media.json. Alt
 * text lives with the slot rather than the manifest, because it describes the
 * slot's editorial job and stays correct whichever photograph is fetched.
 */
import slots from './media-sources.json';

export type MediaSlot = {
  key: string;
  alt: string;
  pexels: string;
  commons: string;
  prefer?: 'pexels' | 'commons';
  orientation?: 'landscape' | 'portrait';
};

export const mediaSlots = slots as MediaSlot[];

export const slotByKey = (key: string) => mediaSlots.find((s) => s.key === key);
