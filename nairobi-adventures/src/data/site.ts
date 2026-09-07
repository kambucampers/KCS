export const site = {
  name: 'Nairobi Adventures',
  legalName: 'Nairobi Adventures',
  tagline: 'Day excursions and Nairobi National Park tours',
  url: 'https://nairobiadventures.com',
  email: 'bookings@nairobiadventures.com',
  // Add a phone or WhatsApp number here and it appears in the header, footer,
  // contact page and LocalBusiness schema automatically.
  phone: '',
  city: 'Nairobi',
  region: 'Nairobi County',
  country: 'KE',
  streetAddress: '',
  social: {
    // Add profile URLs here and they render in the footer.
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
  /** Key from media-sources.json, used for the card image. */
  photo: string;
};

export const tours: Tour[] = [
  {
    slug: 'nairobi-national-park-game-drive',
    title: 'Nairobi National Park game drive',
    navTitle: 'Nairobi National Park',
    summary:
      'A guided game drive through the only national park inside a capital city, where lions, rhinos and giraffe graze against the Nairobi skyline.',
    duration: '4 to 5 hours, or a full day with Karen',
    bestFor: 'First-time safari-goers, photographers, families with a free morning',
    pickup: 'Nairobi hotels, Airbnbs and JKIA',
    accent: 'acacia',
    photo: 'lion-plains',
  },
  {
    slug: 'nairobi-city-excursions',
    title: 'Nairobi city excursions',
    navTitle: 'City excursions',
    summary:
      'The Sheldrick elephant orphanage, the Giraffe Centre, the Karen Blixen Museum, Bomas of Kenya and the Kazuri bead workshop, combined into one unhurried day.',
    duration: '5 hours half day, 9 hours full day',
    bestFor: 'Visitors with one free day, families with children, culture-first travellers',
    pickup: 'Nairobi hotels, Airbnbs and JKIA',
    accent: 'clay',
    photo: 'elephant-orphanage',
  },
  {
    slug: 'day-trips-from-nairobi',
    title: 'Day trips from Nairobi',
    navTitle: 'Day trips',
    summary:
      'Long single days out of the city to Lake Naivasha, Hell&rsquo;s Gate, Lake Nakuru, Amboseli, Ngong Hills and the Great Rift Valley, back in Nairobi by evening.',
    duration: '11 to 14 hours, dawn until evening',
    bestFor: 'Travellers without time for an overnight safari, weekend residents',
    pickup: 'Nairobi hotels, Airbnbs and JKIA',
    accent: 'ink',
    photo: 'lake-nakuru',
  },
  {
    slug: 'airport-layover-tours',
    title: 'Airport layover tours',
    navTitle: 'Layover tours',
    summary:
      'A short excursion built around your connecting flight, timed backwards from check-in so you reach the terminal with hours to spare.',
    duration: 'Layovers of 6 hours or longer',
    bestFor: 'Transit passengers at JKIA with a long connection',
    pickup: 'Jomo Kenyatta International Airport',
    accent: 'marigold',
    photo: 'jkia-airport',
  },
];

export const tourBySlug = (slug: string) => tours.find((t) => t.slug === slug)!;
