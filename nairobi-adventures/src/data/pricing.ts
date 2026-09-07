/**
 * Pricing model for Nairobi Adventures.
 *
 * Method: every price is built from two published components, then marked up.
 *
 *   market price per person = (vehicle and guide day rate + entry fees x travellers) / travellers
 *   listed price per person = market price x MARKUP, rounded to the nearest 5 USD
 *
 * The market anchors come from advertised 2026 rates for comparable private day
 * tours from Nairobi (SafariBookings day-trip listings, Viator and GetYourGuide
 * private departures) and from published park and attraction entry fees. Sources
 * and the full arithmetic are recorded in PRICING.md.
 *
 * Change MARKUP or any component below and every price on the site, including the
 * schema.org offers, updates on the next build.
 */

export const MARKUP = 1.2;
export const CURRENCY = 'USD';

/** Entry fees per person per day, non-resident adult rates. */
export const fees = {
  nairobiNationalPark: 80,
  lakeNakuru: 90,
  amboseli: 90,
  hellsGate: 30,
  mountLongonot: 30,
  ngongHills: 12,
  sheldrickOrphanage: 12,
  giraffeCentre: 12,
  karenBlixenMuseum: 10,
  bomasOfKenya: 10,
  naivashaBoatAndCrescentIsland: 45,
} as const;

/** Private vehicle, fuel, driver guide and road tolls for the whole day. */
export const vehicleDayRate = {
  nairobiHalfDay: 170,
  nairobiFullDay: 250,
  layover: 190,
  riftValleyDay: 320,
  nakuruDay: 340,
  amboseliDay: 420,
  longonotDay: 280,
  ngongDay: 190,
} as const;

export const groupSizes = [1, 2, 3, 4, 5, 6] as const;
export type GroupSize = (typeof groupSizes)[number];

const roundTo5 = (n: number) => Math.round(n / 5) * 5;

/** Listed price per person for a given group size. */
export function pricePerPerson(vehicle: number, feesPerPerson: number, travellers: number): number {
  return roundTo5(((vehicle + feesPerPerson * travellers) / travellers) * MARKUP);
}

export type PriceTier = { travellers: number; label: string; perPerson: number; total: number };

export function priceTable(vehicle: number, feesPerPerson: number): PriceTier[] {
  return groupSizes.map((travellers) => {
    const perPerson = pricePerPerson(vehicle, feesPerPerson, travellers);
    return {
      travellers,
      label: travellers === 1 ? 'Solo traveller' : `${travellers} travellers`,
      perPerson,
      total: perPerson * travellers,
    };
  });
}

/** Lowest per-person price across the table, used for "from" figures and schema offers. */
export function fromPrice(vehicle: number, feesPerPerson: number): number {
  return pricePerPerson(vehicle, feesPerPerson, 6);
}

/** Named options that appear on the tour pages. */
export const options = {
  parkHalfDay: {
    name: 'Half-day game drive',
    vehicle: vehicleDayRate.nairobiHalfDay,
    fees: fees.nairobiNationalPark,
    feeNote: 'Nairobi National Park conservation fee',
  },
  parkFullDay: {
    name: 'Full-day park and Karen combination',
    vehicle: vehicleDayRate.nairobiFullDay,
    fees:
      fees.nairobiNationalPark + fees.sheldrickOrphanage + fees.giraffeCentre + fees.karenBlixenMuseum,
    feeNote: 'park fee plus orphanage, Giraffe Centre and Karen Blixen Museum entry',
  },
  cityHalfDay: {
    name: 'Half-day city excursion',
    vehicle: vehicleDayRate.nairobiHalfDay,
    fees: fees.sheldrickOrphanage + fees.giraffeCentre + fees.karenBlixenMuseum,
    feeNote: 'orphanage, Giraffe Centre and Karen Blixen Museum entry',
  },
  cityFullDay: {
    name: 'Full-day city excursion',
    vehicle: vehicleDayRate.nairobiFullDay,
    fees:
      fees.sheldrickOrphanage + fees.giraffeCentre + fees.karenBlixenMuseum + fees.bomasOfKenya,
    feeNote: 'entry to all four attractions',
  },
  naivashaHellsGate: {
    name: "Lake Naivasha and Hell's Gate",
    vehicle: vehicleDayRate.riftValleyDay,
    fees: fees.hellsGate + fees.naivashaBoatAndCrescentIsland,
    feeNote: "Hell's Gate entry, boat ride and Crescent Island walk",
  },
  lakeNakuru: {
    name: 'Lake Nakuru National Park',
    vehicle: vehicleDayRate.nakuruDay,
    fees: fees.lakeNakuru,
    feeNote: 'Lake Nakuru conservation fee',
  },
  amboseli: {
    name: 'Amboseli National Park',
    vehicle: vehicleDayRate.amboseliDay,
    fees: fees.amboseli,
    feeNote: 'Amboseli conservation fee',
  },
  mountLongonot: {
    name: 'Mount Longonot crater hike',
    vehicle: vehicleDayRate.longonotDay,
    fees: fees.mountLongonot,
    feeNote: 'Mount Longonot entry',
  },
  ngongHills: {
    name: 'Ngong Hills ridge walk',
    vehicle: vehicleDayRate.ngongDay,
    fees: fees.ngongHills,
    feeNote: 'Ngong Hills entry',
  },
  layoverPark: {
    name: 'Layover game drive',
    vehicle: vehicleDayRate.layover,
    fees: fees.nairobiNationalPark,
    feeNote: 'Nairobi National Park conservation fee',
  },
  layoverCity: {
    name: 'Layover city visit',
    vehicle: vehicleDayRate.layover,
    fees: fees.sheldrickOrphanage + fees.giraffeCentre,
    feeNote: 'orphanage and Giraffe Centre entry',
  },
} as const;

export type OptionKey = keyof typeof options;

export const tableFor = (key: OptionKey) => priceTable(options[key].vehicle, options[key].fees);
export const fromFor = (key: OptionKey) => fromPrice(options[key].vehicle, options[key].fees);
export const twoPersonFor = (key: OptionKey) =>
  pricePerPerson(options[key].vehicle, options[key].fees, 2);
