/**
 * Single source of truth for business details.
 *
 * Everything marked PLACEHOLDER was not supplied by the business owner.
 * Replace the value, and it updates across every page, the footer,
 * the JSON-LD schema and the booking form at once.
 */

export const site = {
  name: 'Nairobi Day Trips',
  domain: 'nairobidaytrips.com',
  url: 'https://nairobidaytrips.com',
  tagline: 'Half-day tours of Nairobi National Park and the city, 4 to 6 hours',
  description:
    'Nairobi Day Trips runs half-day tours of Nairobi National Park and Nairobi city attractions, each lasting 4 to 6 hours, plus a full-day option of 7 to 9 hours. Hotel pickup included.',

  // --- contact -----------------------------------------------------------
  phone: '[PLACEHOLDER: phone number]',
  phoneHref: '', // e.g. 'tel:+254700000000'
  whatsapp: '[PLACEHOLDER: WhatsApp number]',
  whatsappHref: '', // e.g. 'https://wa.me/254700000000'
  email: '[PLACEHOLDER: booking email address]',
  emailHref: '', // e.g. 'mailto:hello@nairobidaytrips.com'

  // --- location ----------------------------------------------------------
  city: 'Nairobi',
  region: 'Nairobi County',
  country: 'Kenya',
  countryCode: 'KE',
  street: '[PLACEHOLDER: street address]',
  postalCode: '[PLACEHOLDER: postal code]',
  // Nairobi National Park main gate, the geographic anchor for every tour.
  geo: { lat: -1.3733, lng: 36.8583 },

  // --- operating ---------------------------------------------------------
  timezone: 'EAT (UTC+3)',
  openingHours: '[PLACEHOLDER: office opening hours, e.g. Mon-Sun 06:00-20:00]',
  languages: ['English', 'Swahili'],

  // --- social ------------------------------------------------------------
  social: {
    instagram: '', // '[PLACEHOLDER: Instagram URL]'
    facebook: '',
    tripadvisor: '',
  },

  /**
   * Where the booking form posts.
   *
   * A static site cannot process a form on its own, so this needs a free
   * form endpoint. Two that work on Cloudflare Pages with no server:
   *   Formspree   https://formspree.io      -> 'https://formspree.io/f/xxxxxxxx'
   *   Web3Forms   https://web3forms.com     -> 'https://api.web3forms.com/submit'
   *
   * Leave it empty and the form still validates, but it tells the visitor to
   * email instead of silently losing the enquiry.
   */
  formEndpoint: '', // '[PLACEHOLDER: form endpoint URL]'
  // Web3Forms only: paste the access key it gives you.
  formAccessKey: '',
} as const;

export const nav = [
  { label: 'Tours', href: '/tours/' },
  { label: 'About', href: '/about/' },
  { label: 'Questions', href: '/faq/' },
  { label: 'Contact', href: '/contact/' },
] as const;

export const hasContact =
  !site.email.startsWith('[PLACEHOLDER') || !site.phone.startsWith('[PLACEHOLDER');
