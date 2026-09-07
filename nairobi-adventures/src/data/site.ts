export const site = {
  name: 'Nairobi Adventures',
  legalName: 'Nairobi Adventures',
  tagline: 'Day excursions and Nairobi National Park tours',
  url: 'https://nairobiadventures.com',
  email: 'bookings@nairobiadventures.com',
  // [PLACEHOLDER: phone / WhatsApp number] - add here and it appears in the
  // header, footer, contact page and LocalBusiness schema automatically.
  phone: '',
  city: 'Nairobi',
  region: 'Nairobi County',
  country: 'KE',
  // [PLACEHOLDER: street address for the office, if you list one publicly]
  streetAddress: '',
  social: {
    // [PLACEHOLDER: social profile URLs - delete any you do not use]
    instagram: '',
    facebook: '',
    tripadvisor: '',
  },
} as const;

export type NavItem = { label: string; href: string; children?: NavItem[] };

export const nav: NavItem[] = [
  { label: 'Home', href: '/' },
  {
    label: 'Tours',
    href: '/tours/',
    children: [
      { label: 'Nairobi National Park game drive', href: '/tours/nairobi-national-park-game-drive/' },
      { label: 'Nairobi city excursions', href: '/tours/nairobi-city-excursions/' },
      { label: 'Day trips from Nairobi', href: '/tours/day-trips-from-nairobi/' },
      { label: 'Airport layover tours', href: '/tours/airport-layover-tours/' },
    ],
  },
  { label: 'Plan your day', href: '/plan-your-day/' },
  { label: 'About', href: '/about/' },
  { label: 'Contact', href: '/contact/' },
];

export type Tour = {
  slug: string;
  title: string;
  navTitle: string;
  summary: string;
  duration: string;
  bestFor: string;
  pickup: string;
  accent: 'acacia' | 'clay' | 'marigold' | 'ink';
};

export const tours: Tour[] = [
  {
    slug: 'nairobi-national-park-game-drive',
    title: 'Nairobi National Park game drive',
    navTitle: 'Nairobi National Park',
    summary:
      'A guided game drive through the only national park inside a capital city, where lions, rhinos and giraffe graze against the Nairobi skyline.',
    duration: '[PLACEHOLDER: duration, e.g. 4 to 6 hours]',
    bestFor: 'First-time safari-goers, photographers, families with a free morning',
    pickup: 'Nairobi hotels, Airbnbs and JKIA',
    accent: 'acacia',
  },
  {
    slug: 'nairobi-city-excursions',
    title: 'Nairobi city excursions',
    navTitle: 'City excursions',
    summary:
      'The Sheldrick elephant orphanage, the Giraffe Centre, the Karen Blixen Museum, Bomas of Kenya and the Kazuri bead workshop, combined into one unhurried day.',
    duration: '[PLACEHOLDER: duration, e.g. half day or full day]',
    bestFor: 'Visitors with one free day, families with children, culture-first travellers',
    pickup: 'Nairobi hotels, Airbnbs and JKIA',
    accent: 'clay',
  },
  {
    slug: 'day-trips-from-nairobi',
    title: 'Day trips from Nairobi',
    navTitle: 'Day trips',
    summary:
      'Long single days out of the city to Lake Naivasha, Hell&rsquo;s Gate, Lake Nakuru, Amboseli, Ngong Hills and the Great Rift Valley, back in Nairobi by evening.',
    duration: '[PLACEHOLDER: typical departure and return times]',
    bestFor: 'Travellers without time for an overnight safari, weekend residents',
    pickup: 'Nairobi hotels, Airbnbs and JKIA',
    accent: 'ink',
  },
  {
    slug: 'airport-layover-tours',
    title: 'Airport layover tours',
    navTitle: 'Layover tours',
    summary:
      'A short excursion built around your connecting flight, timed backwards from check-in so you reach the terminal with hours to spare.',
    duration: '[PLACEHOLDER: minimum layover length you accept]',
    bestFor: 'Transit passengers at JKIA with a long connection',
    pickup: 'Jomo Kenyatta International Airport',
    accent: 'marigold',
  },
];

export const tourBySlug = (slug: string) => tours.find((t) => t.slug === slug)!;
