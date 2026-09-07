export type Faq = { q: string; a: string };

export type Tour = {
  slug: string;
  /** Short label used in navigation, cards and the booking form dropdown. */
  short: string;
  /** Page H1. */
  h1: string;
  metaTitle: string;
  metaDescription: string;
  category: 'park' | 'combo' | 'city' | 'full-day';
  duration: string;
  startWindow: string;
  pickup: string;
  /** The direct, self-contained answer that opens the page. 40 to 50 words. */
  answer: string;
  /** One sentence for the tour grid. */
  cardLine: string;
  art: string;
  highlights: string[];
  included: string[];
  notIncluded: string[];
  timeline: { time: string; label: string; text: string }[];
  forWho: string[];
  notForWho: string;
  costFactors: string[];
  depth: { heading: string; body: string[] }[];
  faqs: Faq[];
};

export const tours: Tour[] = [
  /* ===================================================================== */
  {
    slug: 'morning-nairobi-national-park-half-day',
    short: 'Morning park game drive',
    h1: 'Morning Half-Day Nairobi National Park Tour',
    metaTitle: 'Morning Half-Day Nairobi National Park Tour | Nairobi Day Trips',
    metaDescription:
      'A 4 to 6 hour morning game drive in Nairobi National Park, starting at dawn with hotel pickup. Best light, most active wildlife, back in the city by lunchtime.',
    category: 'park',
    duration: '4 to 6 hours',
    startWindow: 'Pickup from 5:45am, park gates open at 6:00am',
    pickup: 'Nairobi hotels, Airbnbs, JKIA and Wilson Airport',
    answer:
      'The morning half-day Nairobi National Park tour is a 4 to 6 hour guided game drive that starts at dawn, when the park is coolest and the animals are most active. Pickup is from your Nairobi hotel around 5:45am and you are back in the city by late morning.',
    cardLine:
      'Dawn start, coolest air, most movement. The single best window for lions and rhino.',
    art: 'sunrise',
    highlights: [
      'Gates open at 6:00am, so an early start puts your vehicle among the first inside the park',
      'Black and white rhino, which Nairobi National Park holds in unusual density for a park this size',
      'Lion, buffalo, giraffe, zebra, eland, impala and over 400 recorded bird species',
      'The Nairobi skyline standing directly behind grazing wildlife, the view the park is known for',
      'Ivory Burning Site Monument and the Athi Basin dams, depending on how the morning runs',
    ],
    included: [
      'Private 4x4 or safari van with a pop-up roof for photography',
      'Professional driver-guide licensed to work in Nairobi National Park',
      'Hotel, Airbnb or airport pickup and drop-off inside Nairobi',
      'Bottled drinking water',
      'All fuel and parking',
    ],
    notIncluded: [
      'Kenya Wildlife Service park entry fees, which are charged per person per day and differ for citizens, residents and non-residents',
      'Meals and drinks beyond the water provided',
      'Tips for your guide, which are welcome but never expected',
      'Travel insurance',
    ],
    timeline: [
      {
        time: '5:45am',
        label: 'Pickup',
        text: 'Your guide meets you in the hotel lobby. Nairobi roads are empty at this hour, so the transfer to the gate takes 20 to 40 minutes depending on where you are staying.',
      },
      {
        time: '6:15am',
        label: 'Into the park',
        text: 'Entry formalities at the gate, then straight onto the game-viewing circuits while the grass is still wet and tracks from the night are readable.',
      },
      {
        time: '6:30am to 10:00am',
        label: 'Game drive',
        text: 'Your guide works the routes based on that morning’s sightings, radio reports from other guides and where the herds have moved. Nothing is on rails, because wildlife is not.',
      },
      {
        time: '10:00am',
        label: 'Stop and stretch',
        text: 'A break at a designated picnic site or viewpoint. Getting out of the vehicle is only allowed at these marked spots, which is a Kenya Wildlife Service rule your guide will keep to.',
      },
      {
        time: '10:30am to 11:30am',
        label: 'Back to the city',
        text: 'Drop-off at your hotel, or at a restaurant, mall or the airport if that suits your day better. Say the word and your guide will reroute.',
      },
    ],
    forWho: [
      'Visitors with a single free morning before meetings, a flight or a connecting safari',
      'Photographers, because the low dawn light and the skyline backdrop only line up early',
      'Anyone whose priority is rhino, since the early hours give the best odds',
      'Layover passengers with 8 or more hours at Jomo Kenyatta International Airport',
    ],
    notForWho:
      'If waking at 5:00am would ruin the rest of your day, take the afternoon half-day tour instead. The wildlife is quieter but the tour is far kinder to a jet-lagged body.',
    costFactors: [
      'Group size, because the vehicle is priced per trip rather than per seat, so four people split the same vehicle cost between four',
      'Vehicle type, since a pop-roof safari van and a Land Cruiser have different running costs',
      'Kenya Wildlife Service entry fees, which are set by KWS and vary by residency status',
      'Pickup point, because a Karen or Langata hotel sits minutes from the gate while a Westlands or Gigiri hotel adds road time',
      'Whether you add a second stop such as the Sheldrick Wildlife Trust or the Giraffe Centre',
    ],
    depth: [
      {
        heading: 'Why the morning drive is the stronger of the two park tours',
        body: [
          'Nairobi National Park sits at roughly 1,600 metres above sea level, so dawn temperatures often sit around 12 to 15 degrees Celsius. Predators hunt through that cool window and rest once the ground heats, which is why a 6:00am entry consistently produces more movement than a midday one.',
          'The second reason is light. The sun rises around 6:30am year round because Nairobi sits almost on the equator, so the first hour inside the park gives soft, low, side-on light. That is the light that makes the famous frame work, wildlife in the foreground with the office towers of the Nairobi skyline behind.',
          'The third reason is traffic. Leaving your hotel before 6:00am means you miss the Mombasa Road and Langata Road build-up entirely, so more of your 4 to 6 hours is spent in the park rather than in a queue.',
        ],
      },
      {
        heading: 'What Nairobi National Park actually holds',
        body: [
          'Nairobi National Park covers about 117 square kilometres and was gazetted in 1946, which makes it Kenya’s oldest national park. It is fenced on three sides and open on the southern boundary towards the Kitengela plains, so wildlife still moves in and out along that corridor.',
          'The park is one of Kenya’s most reliable rhino sanctuaries and carries both black and white rhino. Lion, leopard, cheetah, spotted hyena, buffalo, Maasai giraffe, common zebra, eland, impala, warthog and hippo are all resident. Birdlife runs past 400 recorded species, and the seasonal dams hold waders through the rains.',
          'One honest exclusion matters: there are no elephants in Nairobi National Park, because the park is too small to hold them safely. If seeing elephants is the point of your morning, pair the park with the Sheldrick Wildlife Trust orphanage, which is the tour built exactly for that.',
        ],
      },
      {
        heading: 'What to bring, and what to wear',
        body: [
          'Bring a light fleece or jacket for the first hour, because an open-roof vehicle at dawn on the Athi plains is genuinely cold, then bring sunscreen for the last hour, when it is not. Layers solve the whole morning.',
          'Binoculars help more than a long lens for most people, since a lot of what your guide finds is at distance. If you are shooting, 200mm is workable and 400mm is comfortable.',
          'Bring your passport or ID and a card for the park gate, because Kenya Wildlife Service collects entry fees electronically at the gate rather than in cash.',
        ],
      },
    ],
    faqs: [
      {
        q: 'How early does the morning Nairobi National Park tour start?',
        a: 'Pickup is normally between 5:45am and 6:15am so that your vehicle reaches the gate close to opening at 6:00am. If your hotel is in Karen or Langata the pickup is later, because the gate is only minutes away.',
      },
      {
        q: 'Will I see the Big Five on a morning half-day tour?',
        a: 'You can realistically see four of the Big Five in Nairobi National Park, which are lion, leopard, buffalo and rhino. There are no elephants in the park, so a full Big Five sighting is not possible here.',
      },
      {
        q: 'Can I do this tour on a layover at JKIA?',
        a: 'Yes, if your layover is 8 hours or longer and you can clear immigration. Your guide collects you from the terminal, runs the game drive and returns you with time to check in again. Tell us your flight numbers when you book so the timings are built around them.',
      },
      {
        q: 'Are park entry fees included in the price?',
        a: 'No. Kenya Wildlife Service sets and collects park entry fees separately, and they differ for Kenyan citizens, Kenyan residents and non-residents. We quote them to you in writing before you confirm, so nothing is a surprise at the gate.',
      },
    ],
  },

  /* ===================================================================== */
  {
    slug: 'afternoon-nairobi-national-park-half-day',
    short: 'Afternoon park game drive',
    h1: 'Afternoon Half-Day Nairobi National Park Tour',
    metaTitle: 'Afternoon Half-Day Nairobi National Park Tour | Nairobi Day Trips',
    metaDescription:
      'A 4 to 6 hour afternoon game drive in Nairobi National Park with hotel pickup after lunch. Golden evening light, no early alarm, back in the city by dusk.',
    category: 'park',
    duration: '4 to 6 hours',
    startWindow: 'Pickup from 12:30pm, park gates close at 6:00pm',
    pickup: 'Nairobi hotels, Airbnbs, JKIA and Wilson Airport',
    answer:
      'The afternoon half-day Nairobi National Park tour is a 4 to 6 hour guided game drive that begins after lunch and runs to the evening gate closing. It suits arrivals, jet lag and slow mornings, because nothing about it requires a dawn alarm.',
    cardLine:
      'A midday pickup, warm golden light and no 5:00am alarm. Built for arrival days.',
    art: 'goldenhour',
    highlights: [
      'Late light through the last two hours, which is the second-best photographic window of the day',
      'Rhino, buffalo, giraffe and zebra moving back towards water as the heat drops',
      'Hippo Pools and the riverine forest along the Athi River, which is at its most comfortable in the afternoon',
      'The Nairobi skyline lit from the west, behind the plains',
      'A genuinely relaxed pace, because you are not racing a gate opening',
    ],
    included: [
      'Private 4x4 or safari van with a pop-up roof',
      'Professional driver-guide licensed for Nairobi National Park',
      'Hotel, Airbnb or airport pickup and drop-off inside Nairobi',
      'Bottled drinking water',
      'All fuel and parking',
    ],
    notIncluded: [
      'Kenya Wildlife Service park entry fees, charged per person per day',
      'Lunch before departure, though your guide will happily stop for it',
      'Tips for your guide',
      'Travel insurance',
    ],
    timeline: [
      {
        time: '12:30pm to 1:30pm',
        label: 'Pickup',
        text: 'Collected from your hotel after lunch. The exact time is set by where you are staying, because Nairobi afternoon traffic is real and we plan around it rather than pretend it is not.',
      },
      {
        time: '2:00pm',
        label: 'Into the park',
        text: 'Gate formalities, then onto the circuits. The first hour is the hottest, so your guide works shade, water and the treelines where animals sit out the heat.',
      },
      {
        time: '3:30pm to 5:30pm',
        label: 'The good hours',
        text: 'As the ground cools, grazers move into the open and predators start to stir. This is the stretch that makes the afternoon tour worth doing.',
      },
      {
        time: '5:30pm',
        label: 'Out before closing',
        text: 'Vehicles must be out of the park by 6:00pm, so your guide times the last loop to finish near a gate rather than sprint for one.',
      },
      {
        time: '6:00pm to 6:45pm',
        label: 'Back to the city',
        text: 'Drop-off at your hotel, or at a restaurant if you would rather go straight to dinner.',
      },
    ],
    forWho: [
      'Travellers landing in Nairobi that morning who want the day to still count',
      'Anyone whose body is still on another time zone',
      'Families with young children, because a post-nap start beats a pre-dawn one',
      'Visitors with a morning meeting and a free afternoon',
    ],
    notForWho:
      'If your priority is the highest possible chance of lion or a leopard sighting, book the morning tour. Predator activity is measurably higher in the first hours after gates open.',
    costFactors: [
      'Group size, because the vehicle is priced per trip and shared between everyone in it',
      'Vehicle type, van or Land Cruiser',
      'Kenya Wildlife Service entry fees, set by KWS and dependent on residency',
      'Pickup point and the traffic between it and the gate',
      'Any add-on stop, such as the Giraffe Centre on the way back',
    ],
    depth: [
      {
        heading: 'What the afternoon tour trades, and what it gains',
        body: [
          'The honest trade is predator activity. Lions in Nairobi National Park are most visible in the cool first hours after 6:00am, so an afternoon drive gives you lower odds on cats than a morning one does. We say that plainly rather than sell you a maybe.',
          'What the afternoon gains is everything else. You get warm directional light from about 4:30pm, grazing herds moving into the open as the ground cools, far more comfortable conditions at the Hippo Pools and along the Athi River, and a start time that does not cost you a night of sleep.',
          'For a visitor who has just landed, that trade is usually the right one, because a tired traveller on a 5:45am pickup remembers the tiredness rather than the park.',
        ],
      },
      {
        heading: 'How the light works in the last two hours',
        body: [
          'Nairobi sits just south of the equator, so sunset lands close to 6:30pm all year with very little seasonal drift. From roughly 4:30pm the light warms and lengthens, which is when the plains stop reading as flat and start showing texture.',
          'That window matters because the park’s signature frame, wildlife against the city skyline, needs the towers lit rather than silhouetted. In the afternoon the sun is behind you as you look north towards the city, so the buildings catch light instead of going dark.',
        ],
      },
      {
        heading: 'Weather, and what the rains actually change',
        body: [
          'Nairobi has two rainy periods, the long rains from roughly March to May and the short rains from roughly October to December. Afternoon showers in those months tend to be short and heavy rather than all-day, so a drive is rarely cancelled outright.',
          'Rain actually improves some things. Dust drops, the light goes dramatic, the seasonal dams fill and bird numbers climb. What it costs you is traction on the black cotton soil tracks in the park’s eastern sections, which is precisely why a 4x4 is worth having in those months.',
        ],
      },
    ],
    faqs: [
      {
        q: 'What time does the afternoon Nairobi National Park tour finish?',
        a: 'All vehicles must leave the park by 6:00pm, so you are normally back at your hotel between 6:00pm and 6:45pm depending on where you are staying and how the evening traffic sits.',
      },
      {
        q: 'Is the afternoon game drive worse than the morning one?',
        a: 'It is different rather than worse. Predator sightings are less likely in the afternoon, and light, comfort and grazing-herd activity in the final two hours are better. Choose the morning for cats and the afternoon for ease and photography.',
      },
      {
        q: 'Can you pick me up straight from the airport?',
        a: 'Yes. Jomo Kenyatta International Airport is about 20 minutes from the park gate outside peak traffic, so an early-afternoon landing works well. We can hold luggage in the vehicle and drop you at your hotel afterwards.',
      },
      {
        q: 'What happens if it rains?',
        a: 'The drive goes ahead. Nairobi rain is usually a heavy hour rather than a lost day, the vehicle roof closes, and your guide adjusts the route to avoid the softest tracks. If weather genuinely makes the park unsafe we will move your booking rather than run a poor tour.',
      },
    ],
  },

  /* ===================================================================== */
  {
    slug: 'nairobi-national-park-sheldrick-half-day',
    short: 'Park + Sheldrick elephants',
    h1: 'Half-Day Nairobi National Park and Sheldrick Elephant Orphanage Tour',
    metaTitle: 'Nairobi National Park and Sheldrick Elephant Orphanage Half-Day Tour',
    metaDescription:
      'A 4 to 6 hour morning tour combining a Nairobi National Park game drive with the 11am public visit at the Sheldrick Wildlife Trust elephant orphanage.',
    category: 'combo',
    duration: '5 to 6 hours',
    startWindow: 'Pickup from 5:45am, timed to reach Sheldrick for the 11:00am visit',
    pickup: 'Nairobi hotels, Airbnbs, JKIA and Wilson Airport',
    answer:
      'This 5 to 6 hour morning tour pairs a Nairobi National Park game drive with the Sheldrick Wildlife Trust elephant orphanage. Because the orphanage opens to the public for one hour only, from 11:00am to noon, the whole morning is timed backwards from that single window.',
    cardLine:
      'The park has no elephants. This is the tour that fixes that, built around Sheldrick’s 11am hour.',
    art: 'elephant',
    highlights: [
      'Rescued orphaned elephant calves feeding and mud-bathing at the Sheldrick Wildlife Trust',
      'A keeper talking through each calf by name, where it was found and why',
      'A full morning game drive in Nairobi National Park beforehand, including rhino and lion country',
      'Both sites sit on the same side of the city, so almost none of your time goes on transfers',
      'A tour with a genuine conservation spine, because the Trust has hand-raised orphaned elephants since 1977',
    ],
    included: [
      'Private 4x4 or safari van with a pop-up roof',
      'Professional driver-guide',
      'Hotel, Airbnb or airport pickup and drop-off inside Nairobi',
      'Transfer between the park and the orphanage',
      'Bottled drinking water',
    ],
    notIncluded: [
      'Kenya Wildlife Service park entry fees',
      'Sheldrick Wildlife Trust entry, which the Trust takes as a donation booked in advance through its own website',
      'Meals and drinks',
      'Tips for your guide',
    ],
    timeline: [
      {
        time: '5:45am',
        label: 'Pickup',
        text: 'An early collection, because the park comes first and the orphanage hour is fixed.',
      },
      {
        time: '6:15am to 10:15am',
        label: 'Game drive',
        text: 'The full morning circuit through Nairobi National Park, worked for rhino, lion, buffalo and giraffe while the air is still cool.',
      },
      {
        time: '10:30am',
        label: 'Move to the orphanage',
        text: 'The Sheldrick nursery sits inside Nairobi National Park land off Magadi Road, so the transfer is short. Arriving before the crowd matters, because the viewing area fills.',
      },
      {
        time: '11:00am to 12:00pm',
        label: 'The elephant hour',
        text: 'The orphaned calves come in for their milk feed and mud bath while a keeper explains each rescue. This is the only hour of the day the nursery opens to general visitors.',
      },
      {
        time: '12:15pm',
        label: 'Back to the city',
        text: 'Drop-off at your hotel, a restaurant or the airport.',
      },
    ],
    forWho: [
      'Anyone whose main reason for visiting Nairobi is elephants, since the park itself has none',
      'Families, because the orphanage hour holds children’s attention in a way a long game drive sometimes does not',
      'Visitors who want their tourism money to land somewhere that does verifiable conservation work',
      'First-time visitors with one morning and a want for range rather than depth',
    ],
    notForWho:
      'If you cannot start before 6:00am, this combination does not work, because the game drive has to happen before the fixed 11:00am orphanage slot. Book the afternoon park tour and visit Sheldrick on a separate day.',
    costFactors: [
      'Group size, because the vehicle cost is split across everyone travelling',
      'Kenya Wildlife Service park entry fees, set by KWS',
      'The Sheldrick Wildlife Trust donation, which the Trust sets and collects directly',
      'Vehicle type and pickup distance',
    ],
    depth: [
      {
        heading: 'Why this tour is timed around 11:00am and nothing else',
        body: [
          'The Sheldrick Wildlife Trust opens its Nairobi nursery to general visitors for one hour a day, from 11:00am to noon, because the rest of the day belongs to the calves’ feeding and care routine. Every other part of this tour is scheduled backwards from that hour.',
          'That is why the game drive starts at dawn rather than mid-morning, and why the tour cannot be run in the afternoon. A late start means either a rushed game drive or a missed orphanage slot, and neither is worth selling.',
          'Visits must be booked in advance directly with the Trust, and space is limited. Tell us your travel dates early so the sequence can be locked in, because the orphanage slot is the constraint that everything else bends around.',
        ],
      },
      {
        heading: 'What actually happens during the orphanage hour',
        body: [
          'Orphaned elephant calves are walked into a roped viewing area in groups, take large bottles of specially formulated milk from their keepers, then drink, dust and mud-bathe while a keeper narrates. The keeper names each calf, says where it was found and what happened to its family.',
          'The Sheldrick Wildlife Trust has hand-raised orphaned elephants since 1977 and reintegrates them into wild herds through its reintegration units in Tsavo, so the nursery you visit is one stage of a long process rather than a permanent home.',
          'Expect an hour that is louder, muddier and more crowded than a game drive, and expect the keeper talk to be the part you remember.',
        ],
      },
      {
        heading: 'How this compares with the Giraffe Centre combination',
        body: [
          'Both combinations pair the same park game drive with one animal attraction, so choose on what you want to see and how you want to see it. The Sheldrick hour is a fixed, scheduled, narrated event where you watch from a rope line. The Giraffe Centre is an open-ended visit where you stand on a raised platform and feed giraffe from your hand.',
          'The practical difference is flexibility. Sheldrick locks your morning to a single hour, while the Giraffe Centre is open from morning to late afternoon, so that combination works with a later start.',
          'If you have a full day rather than a half day, the Nairobi day trip covers both, because 7 to 9 hours is enough to fit the game drive, the 11:00am orphanage hour and the Giraffe Centre afterwards.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Are there elephants in Nairobi National Park?',
        a: 'No. Nairobi National Park has no elephants, because at 117 square kilometres it is too small to support them safely. Seeing elephants near Nairobi means visiting the Sheldrick Wildlife Trust orphanage, which is why this combined tour exists.',
      },
      {
        q: 'Do I have to book the Sheldrick visit myself?',
        a: 'The Sheldrick Wildlife Trust takes bookings and donations directly through its own website, and slots are limited. We tell you exactly what to book and when, and we build the game drive timings around the slot you secure.',
      },
      {
        q: 'Can I touch or feed the elephants?',
        a: 'No. Visitors watch from behind a rope while the keepers feed the calves. The Trust keeps that distance deliberately, because the calves are being prepared for reintegration into wild herds rather than habituated to people.',
      },
      {
        q: 'How long does the whole tour take?',
        a: 'Between 5 and 6 hours door to door, starting with a 5:45am pickup and ending with a drop-off from about 12:15pm.',
      },
    ],
  },

  /* ===================================================================== */
  {
    slug: 'nairobi-national-park-giraffe-centre-half-day',
    short: 'Park + Giraffe Centre',
    h1: 'Half-Day Nairobi National Park and Giraffe Centre Tour',
    metaTitle: 'Nairobi National Park and Giraffe Centre Half-Day Tour | Nairobi Day Trips',
    metaDescription:
      'A 4 to 6 hour tour pairing a Nairobi National Park game drive with the Giraffe Centre in Langata, where you feed endangered Rothschild giraffe by hand.',
    category: 'combo',
    duration: '5 to 6 hours',
    startWindow: 'Morning or afternoon, because the Giraffe Centre opens 9:00am to 5:00pm',
    pickup: 'Nairobi hotels, Airbnbs, JKIA and Wilson Airport',
    answer:
      'This 5 to 6 hour tour pairs a Nairobi National Park game drive with the Giraffe Centre in Langata, where you feed endangered Rothschild giraffe from a raised platform. Because the Giraffe Centre is open from 9:00am to 5:00pm, this combination runs either morning or afternoon.',
    cardLine:
      'Wild giraffe on the plains in the morning, then a giraffe eating out of your hand by 11am.',
    art: 'giraffe',
    highlights: [
      'Hand-feeding endangered Rothschild giraffe from a raised platform built at head height',
      'A full Nairobi National Park game drive beforehand, with rhino, lion and buffalo country',
      'The Giraffe Centre’s conservation programme, run by the African Fund for Endangered Wildlife since 1979',
      'A short forest boardwalk on the Centre grounds, which is a good leg-stretch after a drive',
      'Flexible timing, because the Centre is open across the whole working day',
    ],
    included: [
      'Private 4x4 or safari van with a pop-up roof',
      'Professional driver-guide',
      'Hotel, Airbnb or airport pickup and drop-off inside Nairobi',
      'Transfer between the park and Langata',
      'Bottled drinking water',
    ],
    notIncluded: [
      'Kenya Wildlife Service park entry fees',
      'Giraffe Centre entrance fee, which the Centre sets and collects at its gate',
      'Meals and drinks',
      'Tips for your guide',
    ],
    timeline: [
      {
        time: '6:00am or 12:30pm',
        label: 'Pickup',
        text: 'You choose. The morning version gives better wildlife activity, the afternoon version gives an easier start.',
      },
      {
        time: 'First 3 to 4 hours',
        label: 'Game drive',
        text: 'Nairobi National Park circuits, worked around the day’s sightings for rhino, lion, buffalo, zebra and wild giraffe on the open plains.',
      },
      {
        time: 'Then 20 minutes',
        label: 'Move to Langata',
        text: 'The Giraffe Centre sits in Langata, minutes from the park’s Langata Gate, so the transfer barely dents your time.',
      },
      {
        time: '45 to 60 minutes',
        label: 'Giraffe Centre',
        text: 'Up onto the feeding platform with a handful of pellets, then the warthogs at ground level and the forest boardwalk if you want it.',
      },
      {
        time: 'Final leg',
        label: 'Back to the city',
        text: 'Drop-off at your hotel, a restaurant, a mall or the airport.',
      },
    ],
    forWho: [
      'Families with children, because feeding a giraffe by hand is the part children talk about afterwards',
      'Visitors who want one wild experience and one close-up experience in the same half day',
      'Anyone who cannot make the fixed 11:00am Sheldrick slot but still wants an animal encounter',
      'People staying in Karen or Langata, since both stops are on their doorstep',
    ],
    notForWho:
      'If elephants are what you came for, take the Sheldrick combination instead, because the Giraffe Centre has no elephants and Nairobi National Park does not either.',
    costFactors: [
      'Group size, since the vehicle is priced per trip',
      'Kenya Wildlife Service park entry fees',
      'Giraffe Centre entrance, which is charged per person and differs for residents and non-residents',
      'Morning or afternoon slot and the traffic that comes with each',
      'Vehicle type and pickup distance',
    ],
    depth: [
      {
        heading: 'Why the Giraffe Centre is worth an hour of a half day',
        body: [
          'The Giraffe Centre exists because the Rothschild giraffe, also called the Nubian giraffe, was reduced to a very small Kenyan population. The African Fund for Endangered Wildlife established the Centre in Langata in 1979 to breed the subspecies and move calves into protected areas, and that translocation programme is still the point of the place.',
          'For a visitor, the practical draw is the raised wooden platform. It puts you level with a giraffe’s head, so feeding one is genuinely eye to eye rather than a hand held over a fence. That is a different experience from watching giraffe at 80 metres on the plains an hour earlier, which is exactly why the two work well in one tour.',
          'The Centre is open from 9:00am to 5:00pm every day, and it takes 45 minutes to an hour to do properly. Its education programme brings Kenyan schoolchildren through the same platform, so it is often busy with school groups mid-morning on weekdays.',
        ],
      },
      {
        heading: 'Morning version or afternoon version',
        body: [
          'The morning version starts at about 6:00am, runs the game drive through the best wildlife hours and reaches the Giraffe Centre around 10:30am, when school groups are most likely. It gives you the strongest game drive.',
          'The afternoon version starts around 12:30pm, does the Giraffe Centre first or last depending on traffic, and puts you in the park for the good evening light. It gives you the easier day.',
          'Tell us which matters more when you book and we will build the order around it, because the two stops can run in either sequence.',
        ],
      },
      {
        heading: 'What else sits within five minutes of the Giraffe Centre',
        body: [
          'Langata and Karen pack several attractions into a very small radius, which is why this half day can flex. The Karen Blixen Museum, the Kazuri Beads women’s cooperative and Bomas of Kenya are all close enough to add if your schedule stretches past six hours.',
          'If you want two or three of those on top of the park, that is the Nairobi city private tour or the full Nairobi day trip rather than this half day, because 4 to 6 hours does not stretch that far honestly.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Can you feed the giraffes at the Giraffe Centre?',
        a: 'Yes. Visitors are given giraffe pellets and feed the animals by hand from a raised platform that sits at giraffe head height. The Centre supplies the pellets at the platform.',
      },
      {
        q: 'What kind of giraffe are at the Giraffe Centre?',
        a: 'Rothschild giraffe, also known as Nubian giraffe, which is an endangered subspecies. The Centre breeds them and translocates young giraffe to protected areas in Kenya, and that programme is the reason the Centre was founded in 1979.',
      },
      {
        q: 'Is the Giraffe Centre the same as Giraffe Manor?',
        a: 'No. The Giraffe Centre is a conservation and education centre open to day visitors, while Giraffe Manor is a private hotel next door where guests pay to stay overnight. This tour visits the Giraffe Centre.',
      },
      {
        q: 'Is this tour good for young children?',
        a: 'Yes, and it is usually the better of the two combinations for them, because the Giraffe Centre is hands-on and has no fixed time slot, so a child who needs a break does not cost you the whole booking.',
      },
    ],
  },

  /* ===================================================================== */
  {
    slug: 'maasai-market-shopping-half-day',
    short: 'Maasai market shopping',
    h1: 'Half-Day Nairobi Shopping Adventure at the Maasai Markets',
    metaTitle: 'Half-Day Nairobi Maasai Market Shopping Tour | Nairobi Day Trips',
    metaDescription:
      'A 4 to 5 hour guided Maasai market shopping tour in Nairobi. Your guide finds the day’s market, handles the bargaining and helps you buy well rather than fast.',
    category: 'city',
    duration: '4 to 5 hours',
    startWindow: 'Flexible, set by which market is running that day',
    pickup: 'Nairobi hotels, Airbnbs and serviced apartments',
    answer:
      'This 4 to 5 hour guided shopping tour takes you to the Maasai market running that day in Nairobi, plus a craft centre or curio market. Because the Maasai market moves to a different part of the city on each day of the week, your guide confirms the location before pickup.',
    cardLine:
      'The market moves every day of the week. Your guide knows where it is and what things are worth.',
    art: 'market',
    highlights: [
      'The open-air Maasai market, which rotates around Nairobi through the week',
      'A guide who negotiates alongside you, because opening prices for visitors bear no relation to closing prices',
      'Beadwork, soapstone carving, kikoi and kanga cloth, wood carving, baskets and leather',
      'A second stop at a fixed-price craft centre or cooperative, so you can benchmark what fair looks like',
      'Help with what is genuinely handmade in Kenya and what is imported and re-labelled',
    ],
    included: [
      'Private vehicle and driver-guide for the duration',
      'Hotel or Airbnb pickup and drop-off inside Nairobi',
      'Guided bargaining and translation into Swahili where it helps',
      'Bottled drinking water',
      'Parking and fuel',
    ],
    notIncluded: [
      'Anything you buy, which is paid directly to the trader',
      'Market entry, where the day’s venue charges a small gate fee',
      'Meals and drinks',
      'Tips for your guide',
    ],
    timeline: [
      {
        time: 'Before pickup',
        label: 'We confirm the venue',
        text: 'The Maasai market rotates by day of the week around Nairobi car parks and mall grounds, and venues do change, so your guide confirms the day’s location before you are collected rather than driving you to a closed lot.',
      },
      {
        time: 'First 30 minutes',
        label: 'A walk before you buy',
        text: 'One loop of the market without buying anything. This is the single most useful thing you can do, because it shows you how many stalls sell the same carving and at what spread of prices.',
      },
      {
        time: 'Next 90 minutes',
        label: 'Buying properly',
        text: 'Your guide helps you open, counter and close. Bargaining here is expected and friendly, and walking away is a normal part of it rather than an insult.',
      },
      {
        time: 'Then 60 minutes',
        label: 'A fixed-price stop',
        text: 'A craft cooperative or curio centre where prices are marked, so you can see what you paid against what a shop charges. Kazuri Beads in Karen is a common choice, because you can watch the pottery being made.',
      },
      {
        time: 'Final leg',
        label: 'Back to the city',
        text: 'Drop-off at your hotel, or at a mall or restaurant if you want to keep going.',
      },
    ],
    forWho: [
      'Visitors buying gifts and souvenirs who would rather not be quoted a tourist opening price all afternoon',
      'Anyone who finds haggling uncomfortable, because having a local alongside changes the whole exchange',
      'Travellers on their last day in Nairobi with a suitcase to fill',
      'People who want to buy from the maker rather than from a hotel gift shop',
    ],
    notForWho:
      'If you want a quiet, air-conditioned, fixed-price shopping trip, say so and we will build the half day around craft centres and malls instead. The Maasai market is loud, crowded and hot, and that is the point of it.',
    costFactors: [
      'Group size, because the vehicle is priced per trip',
      'Which day you go, since some venues are further out than others',
      'How many stops you add beyond the market itself',
      'Whether you need a second vehicle run to carry large or fragile purchases',
    ],
    depth: [
      {
        heading: 'How the Maasai market rotation works',
        body: [
          'There is no single permanent Maasai market in Nairobi. Instead, traders set up in a different part of the city on each day of the week, using car parks and open ground at malls and civic buildings, then pack up at the end of the day. That is why a hotel concierge and a guidebook will sometimes give you two different answers.',
          'Venues shift over time as parking arrangements change, so a schedule printed two years ago can send you to an empty car park. We confirm the day’s location on the morning of your tour, which is most of the practical value of booking a guide for this rather than taking a taxi.',
          'If your dates are fixed and you want a specific area of Nairobi, tell us and we will tell you which day suits, because the market comes to you rather than the other way round.',
        ],
      },
      {
        heading: 'Bargaining, honestly explained',
        body: [
          'Opening prices at the Maasai market are a starting position rather than a valuation, and they are set higher for visitors because that is how the market has always worked. Nobody is cheating you, and nobody expects the first number to be the last one.',
          'The technique that works is simple. Look at everything first, decide what you actually want, then ask a price and counter well below it. Move in small steps, stay friendly, and be genuinely willing to walk. Prices fall fastest when you are leaving.',
          'Buying several things from one stall gets you a better rate than buying one thing from several stalls, so consolidate. And carry small Kenyan shilling notes, because change is a real friction point and a large note weakens your position.',
        ],
      },
      {
        heading: 'What is worth buying, and what to look at twice',
        body: [
          'Kenyan soapstone comes from Kisii in the west and is genuinely local, as is Maasai beadwork, kiondo sisal baskets, kikoi and kanga cloth, and olive-wood and jacaranda-wood carving. These are the things worth carrying home.',
          'Look twice at anything that seems machine-uniform, at "ebony" carvings that are actually stained soft wood, and at mass-produced items imported and sold as Kenyan craft. Your guide will tell you which stall is selling which, which is a conversation that is much easier to have in Swahili.',
          'Check your airline’s rules before buying anything heavy. Soapstone is dense, and a full set of carvings will eat a luggage allowance faster than people expect.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Where is the Maasai market in Nairobi today?',
        a: 'The Maasai market rotates to a different Nairobi venue on each day of the week, and venues change from time to time. We confirm the current day’s location before your pickup rather than relying on a published schedule that may be out of date.',
      },
      {
        q: 'How much should I pay at the Maasai market?',
        a: 'There is no fixed price, because every item is negotiated. Expect the opening price to be well above the closing price, and expect your guide to help you find the range that traders are actually accepting that day.',
      },
      {
        q: 'Can I pay by card or M-Pesa?',
        a: 'Most traders take M-Pesa and cash, and very few take cards. Bring Kenyan shillings in small notes, because change is limited and a small note gives you a stronger position when closing a price.',
      },
      {
        q: 'Is the Maasai market safe for visitors?',
        a: 'It is busy and crowded rather than dangerous, and normal city sense applies. Keep your phone and wallet in a front pocket or zipped bag, do not carry more cash than you plan to spend, and stay with your guide in the tighter aisles.',
      },
    ],
  },

  /* ===================================================================== */
  {
    slug: 'nairobi-walking-tour-half-day',
    short: 'Nairobi walking tour',
    h1: 'Half-Day Nairobi Walking Tour',
    metaTitle: 'Half-Day Nairobi City Walking Tour | Nairobi Day Trips',
    metaDescription:
      'A 4 hour guided walking tour of central Nairobi covering the KICC, City Market, Jeevanjee Gardens, the National Archives and the August 7th Memorial Park.',
    category: 'city',
    duration: '4 hours',
    startWindow: 'Morning start recommended, because the CBD is coolest and quietest early',
    pickup: 'Nairobi hotels, or meet your guide in the city centre',
    answer:
      'The half-day Nairobi walking tour is a 4 hour guided walk through the central business district, covering the Kenyatta International Convention Centre, City Market, Jeevanjee Gardens, the Kenya National Archives and the August 7th Memorial Park. You walk the city rather than drive past it.',
    cardLine:
      'Four hours on foot through the CBD, with a guide who can tell you what you are looking at.',
    art: 'city',
    highlights: [
      'The Kenyatta International Convention Centre, whose rooftop viewing deck gives the widest view of Nairobi',
      'City Market on Muindi Mbingu Street, a 1930s covered market that still trades every day',
      'Jeevanjee Gardens, donated to the city in 1906 and still the CBD’s public square',
      'The Kenya National Archives on Moi Avenue, holding the Murumbi collection of African art',
      'August 7th Memorial Park, on the site of the 1998 United States embassy bombing',
      'Street food, coffee and a genuinely local lunch stop if you want one',
    ],
    included: [
      'Professional walking guide for the full four hours',
      'Hotel pickup and drop-off inside Nairobi, or a city-centre meeting point',
      'Bottled drinking water',
      'Route planning around the day’s traffic and road closures',
    ],
    notIncluded: [
      'Entrance fees, including the KICC rooftop viewing deck and the National Archives',
      'Meals, coffee and street food',
      'Tips for your guide',
    ],
    timeline: [
      {
        time: '9:00am',
        label: 'Start',
        text: 'Pickup from your hotel or a meeting point in the CBD. A morning start matters, because the centre is coolest, least crowded and best for photographs before noon.',
      },
      {
        time: 'First hour',
        label: 'The civic centre',
        text: 'Parliament Road, City Hall and the Kenyatta International Convention Centre, including the rooftop deck if it is open, which is the single best orientation to the city you can get.',
      },
      {
        time: 'Second hour',
        label: 'Markets and gardens',
        text: 'City Market for flowers, produce and craft, then Jeevanjee Gardens and the streets around Biashara Street.',
      },
      {
        time: 'Third hour',
        label: 'History',
        text: 'The Kenya National Archives on Moi Avenue and the August 7th Memorial Park, which is a quiet and deliberately sober stop.',
      },
      {
        time: 'Fourth hour',
        label: 'Coffee and finish',
        text: 'A coffee or a plate of local food, then drop-off. Nairobi is a serious coffee-growing country and the CBD has the cafes to prove it.',
      },
    ],
    forWho: [
      'Visitors who want to understand Nairobi as a city rather than as a safari departure point',
      'Business travellers with a free morning between meetings',
      'Photographers and architecture enthusiasts',
      'Anyone who has done the park already and wants something completely different',
    ],
    notForWho:
      'If walking three to four kilometres over four hours in equatorial sun does not appeal, take the Nairobi city private tour instead, which covers similar ground with a vehicle between stops.',
    costFactors: [
      'Group size, because a walking guide is priced per group rather than per vehicle seat',
      'Whether you include the KICC rooftop and the National Archives, which charge entry',
      'Whether you want a food-focused version with several tasting stops',
      'Start time, since a morning walk is more comfortable than an afternoon one',
    ],
    depth: [
      {
        heading: 'What you actually learn on foot that you cannot learn from a car',
        body: [
          'Nairobi began in 1899 as a railway depot on the Uganda Railway, chosen because the swampy ground at the edge of the Athi plains was the last flat place before the escarpment. Almost everything about the CBD’s layout follows from that, and you can read it on foot in a way you cannot from a moving vehicle.',
          'Walking also puts you at street level with the parts of the city that make it work, which are the matatu stages, the hawkers, the newspaper vendors, the sidewalk cobblers and the lunch queues at 1:00pm. That is the texture the tour is for.',
          'A guide matters here more than on a game drive, because the buildings do not label themselves. The difference between a walk that is interesting and one that is just hot is entirely the person telling you what you are looking at.',
        ],
      },
      {
        heading: 'The route, and why it is ordered this way',
        body: [
          'The walk runs roughly north from the government quarter towards Moi Avenue, then loops back through the market streets. That order is deliberate, because the KICC rooftop early gives you a map in your head, and every stop after it makes more sense once you have seen the layout from above.',
          'The August 7th Memorial Park sits near the end on purpose. It marks the 1998 bombing of the United States embassy, which killed more than 200 people, most of them Kenyans. It is a quiet, planted garden rather than a monument, and it works better as a place to stop and finish than as something to walk into cold at the start.',
          'Routes flex around the day. Nairobi hosts state events, road closures and demonstrations like any capital city, so your guide adjusts rather than marches you into a closed street.',
        ],
      },
      {
        heading: 'Practical notes for walking in Nairobi',
        body: [
          'Nairobi sits at about 1,795 metres above sea level, so the sun is stronger than the temperature suggests. Bring a hat, sunscreen and water, and expect the middle of the day to be warm rather than hot, because the altitude keeps the ceiling down.',
          'Wear closed shoes you can walk four kilometres in, since pavement quality varies. Carry a small amount of cash for entry fees and coffee, keep your phone away when you are not using it, and follow your guide’s lead on where photography is and is not welcome, particularly around government buildings.',
          'Nairobi is a large capital and the CBD has the pickpocketing you would expect in any large capital, so the practical advice is ordinary rather than alarming. Walking with a guide who knows the streets is most of the answer.',
        ],
      },
    ],
    faqs: [
      {
        q: 'How far do you walk on the Nairobi walking tour?',
        a: 'Roughly three to four kilometres over four hours, at a slow pace with frequent stops. It is a strolling tour rather than a hike, and there is nowhere on the route that is steep.',
      },
      {
        q: 'Is it safe to walk around Nairobi city centre?',
        a: 'Yes, with normal city awareness and a guide who knows the streets. Keep valuables out of sight, do not walk with your phone in your hand, and stay with your guide. The CBD is busy and ordinary rather than dangerous during the day.',
      },
      {
        q: 'Can I go up the KICC tower?',
        a: 'The Kenyatta International Convention Centre has a rooftop viewing deck open to visitors for a fee, and it gives the best all-round view of Nairobi. Access depends on events being held in the building, so your guide checks on the day.',
      },
      {
        q: 'Can the walking tour include food?',
        a: 'Yes. Tell us when you book and we will build the route around street food, a local lunch and a proper Kenyan coffee stop rather than around monuments. The four hours stay the same.',
      },
    ],
  },

  /* ===================================================================== */
  {
    slug: 'nairobi-city-private-tour-half-day',
    short: 'Private city tour',
    h1: 'Half-Day Nairobi City Private Tour',
    metaTitle: 'Half-Day Private Nairobi City Tour | Nairobi Day Trips',
    metaDescription:
      'A private 4 to 6 hour Nairobi city tour with your own vehicle and guide. Build the route from the Karen Blixen Museum, Bomas of Kenya, the National Museum and Karura Forest.',
    category: 'city',
    duration: '4 to 6 hours',
    startWindow: 'Any start time you choose, morning or afternoon',
    pickup: 'Nairobi hotels, Airbnbs, JKIA and Wilson Airport',
    answer:
      'The half-day Nairobi city private tour gives you a vehicle, a driver-guide and 4 to 6 hours to spend on the Nairobi attractions you choose. Because the tour is private and nobody else is in the vehicle, the route is built around your interests rather than a fixed itinerary.',
    cardLine:
      'Your vehicle, your guide, your route. Four to six hours of Nairobi, arranged around you.',
    art: 'private',
    highlights: [
      'The Karen Blixen Museum, the farmhouse from Out of Africa, at the foot of the Ngong Hills',
      'Bomas of Kenya, where traditional homesteads and daily dance performances cover the country’s ethnic groups',
      'The Nairobi National Museum and the adjoining Nairobi Gallery',
      'Karura Forest, a 1,000-hectare urban forest with waterfalls, caves and walking trails',
      'Kazuri Beads, a Karen cooperative employing single mothers to make hand-painted ceramic beads',
      'The Railway Museum, which explains why Nairobi exists at all',
    ],
    included: [
      'Private vehicle with driver-guide for the full 4 to 6 hours',
      'Hotel, Airbnb or airport pickup and drop-off inside Nairobi',
      'A route planned with you before the day',
      'Bottled drinking water',
      'All fuel and parking',
    ],
    notIncluded: [
      'Entrance fees at each attraction, which are charged per person and differ for residents and non-residents',
      'Meals and drinks',
      'Tips for your guide',
    ],
    timeline: [
      {
        time: 'Before the day',
        label: 'We plan the route',
        text: 'You tell us what interests you and how much time you have, and we tell you honestly how many stops fit. Four to six hours is three stops done properly or five stops done badly.',
      },
      {
        time: 'Your chosen time',
        label: 'Pickup',
        text: 'From your hotel, apartment or the airport. Because the tour is private, the start time is whatever suits you.',
      },
      {
        time: 'Through the day',
        label: 'Your stops',
        text: 'Your guide handles parking, tickets and timing at each site, and adjusts the order live if traffic or a queue makes the plan worse.',
      },
      {
        time: 'Anytime',
        label: 'Change your mind',
        text: 'A private tour means you can drop a stop, extend one, add a lunch or head back early. Nothing is locked, because nobody else is waiting in the vehicle.',
      },
      {
        time: 'Finish',
        label: 'Drop-off',
        text: 'Hotel, restaurant, mall or airport, whichever helps your day most.',
      },
    ],
    forWho: [
      'Couples, families and small groups who would rather not share a vehicle with strangers',
      'Visitors with specific interests, whether that is colonial history, museums, forests or craft',
      'Business travellers with an unpredictable half day who need to be able to cut it short',
      'Repeat visitors who have already done Nairobi National Park',
    ],
    notForWho:
      'If you want wildlife, this is not the tour. Take a park game drive, or the full Nairobi day trip which covers both the park and the city.',
    costFactors: [
      'Group size, because the vehicle is priced per trip rather than per person',
      'How far apart your chosen stops are, since Karen and Gigiri are on opposite sides of the city',
      'Vehicle type, from a saloon car up to a Land Cruiser',
      'Entrance fees at the sites you pick, which vary widely between them',
      'Whether you want 4 hours or the full 6',
    ],
    depth: [
      {
        heading: 'How many stops actually fit in a half day',
        body: [
          'Three stops is the honest answer for four hours, and four stops for six, because Nairobi traffic is the variable that decides everything. Karen to the city centre can take 25 minutes at 10:00am and 70 minutes at 5:00pm, and no amount of planning changes that.',
          'The strongest half days are the ones that stay on one side of the city. A Karen and Langata route can take in the Karen Blixen Museum, Kazuri Beads and the Giraffe Centre without any long transfer. A city and north route can take in the Nairobi National Museum, the Railway Museum and Karura Forest just as tightly.',
          'Mixing the two sides is possible but it costs you an hour of road, so we will say so when we plan rather than let you find out in the vehicle.',
        ],
      },
      {
        heading: 'What each of the main stops gives you',
        body: [
          'The Karen Blixen Museum is the 1912 farmhouse where the Danish author of Out of Africa lived until 1931. The house is preserved with period furnishings and guided in about 45 minutes, and the Ngong Hills behind it are the view the book describes.',
          'Bomas of Kenya presents traditional homesteads from ethnic groups across the country plus a daily afternoon dance and music performance, so it is the stop that gives cultural range rather than a single story. The performance is the reason to go, and it sets the timing.',
          'The Nairobi National Museum holds Kenya’s paleontology, ethnography and natural-history collections, including hominid fossil material from the Turkana Basin. Karura Forest is the opposite kind of stop, which is 1,000 hectares of indigenous forest inside the city with waterfalls, caves used during the Mau Mau period and marked walking trails.',
        ],
      },
      {
        heading: 'Why private rather than shared',
        body: [
          'A shared city tour has to satisfy everyone in the vehicle, which means fixed stops, fixed timings and a pace set by the slowest person. That is fine when the itinerary matches what you wanted anyway.',
          'A private tour changes three things that matter. You set the departure time, you change the plan mid-day without asking anyone, and your guide answers your questions rather than the group’s. For a family with children or a traveller with a specific interest, those three things are usually worth more than the price difference.',
          'The vehicle also becomes yours for the day, so shopping bags, camera gear and a child who needs a nap all have somewhere to go.',
        ],
      },
    ],
    faqs: [
      {
        q: 'What can I see in Nairobi in half a day?',
        a: 'Three attractions comfortably in four hours, or four in six, as long as they sit on the same side of the city. A Karen route can cover the Karen Blixen Museum, Kazuri Beads and the Giraffe Centre. A city route can cover the Nairobi National Museum, the Railway Museum and Karura Forest.',
      },
      {
        q: 'Can I choose my own stops?',
        a: 'Yes, that is the point of a private tour. Send us the places you want and we will tell you honestly how many fit in your time window and in what order they work best given traffic.',
      },
      {
        q: 'Are entrance fees included?',
        a: 'No. Each attraction sets its own entry fee and most charge different rates for citizens, residents and non-residents. We list the fees for your chosen stops in writing before you confirm.',
      },
      {
        q: 'Can the private city tour include Nairobi National Park?',
        a: 'A game drive plus two or three city stops does not fit in a half day. That combination is the full Nairobi day trip, which runs 7 to 9 hours.',
      },
    ],
  },

  /* ===================================================================== */
  {
    slug: 'nairobi-day-trip',
    short: 'Full-day Nairobi day trip',
    h1: 'Full-Day Nairobi Day Trip',
    metaTitle: 'Full-Day Nairobi Day Trip, 7 to 9 Hours | Nairobi Day Trips',
    metaDescription:
      'A 7 to 9 hour Nairobi day trip combining a national park game drive, the Sheldrick elephant orphanage, the Giraffe Centre and the Karen Blixen Museum.',
    category: 'full-day',
    duration: '7 to 9 hours',
    startWindow: 'Pickup from 5:45am, finishing mid to late afternoon',
    pickup: 'Nairobi hotels, Airbnbs, JKIA and Wilson Airport',
    answer:
      'The full-day Nairobi day trip is a 7 to 9 hour tour that combines a Nairobi National Park game drive, the Sheldrick Wildlife Trust elephant orphanage, the Giraffe Centre and the Karen Blixen Museum. It is the itinerary for visitors with exactly one day in Nairobi.',
    cardLine:
      'One day, four stops: the park, the elephants, the giraffes and Karen. The whole of Nairobi’s highlight reel.',
    art: 'fullday',
    highlights: [
      'A full morning game drive in Nairobi National Park before the heat',
      'The Sheldrick Wildlife Trust orphanage during its 11:00am public hour',
      'Hand-feeding Rothschild giraffe at the Giraffe Centre in Langata',
      'The Karen Blixen Museum, the Out of Africa farmhouse below the Ngong Hills',
      'Lunch at a Karen restaurant, built into the schedule rather than squeezed around it',
      'All four stops within a compact radius, so transfers stay short',
    ],
    included: [
      'Private 4x4 or safari van with a pop-up roof for the whole day',
      'Professional driver-guide for 7 to 9 hours',
      'Hotel, Airbnb or airport pickup and drop-off inside Nairobi',
      'All transfers between the four stops',
      'Bottled drinking water throughout',
      'All fuel and parking',
    ],
    notIncluded: [
      'Kenya Wildlife Service park entry fees',
      'Sheldrick Wildlife Trust donation, booked directly with the Trust',
      'Giraffe Centre and Karen Blixen Museum entrance fees',
      'Lunch and drinks',
      'Tips for your guide',
    ],
    timeline: [
      {
        time: '5:45am',
        label: 'Pickup',
        text: 'Early, because the day is built around two fixed points, which are the 6:00am park gate opening and the 11:00am orphanage hour.',
      },
      {
        time: '6:15am to 10:15am',
        label: 'Nairobi National Park',
        text: 'Four hours of game driving through the best wildlife window, worked for rhino, lion, buffalo, giraffe and the plains game.',
      },
      {
        time: '11:00am to 12:00pm',
        label: 'Sheldrick Wildlife Trust',
        text: 'The orphaned elephant calves’ milk feed and mud bath, narrated by their keepers. This hour is fixed and everything else moves around it.',
      },
      {
        time: '12:30pm to 1:30pm',
        label: 'Lunch in Karen',
        text: 'A proper sit-down break rather than a sandwich in the vehicle. Karen has the restaurants and you have the time.',
      },
      {
        time: '2:00pm to 3:00pm',
        label: 'Giraffe Centre',
        text: 'The feeding platform, the warthogs and the forest boardwalk.',
      },
      {
        time: '3:15pm to 4:15pm',
        label: 'Karen Blixen Museum',
        text: 'The 1912 farmhouse and its gardens, guided, with the Ngong Hills behind it.',
      },
      {
        time: '4:30pm onwards',
        label: 'Back to the city',
        text: 'Drop-off at your hotel or the airport. Tell us your flight time and we will run the day to fit it.',
      },
    ],
    forWho: [
      'Visitors with a single full day in Nairobi, usually before or after a longer safari',
      'Long-layover passengers with 12 or more hours at Jomo Kenyatta International Airport',
      'First-time visitors who want the whole highlight reel rather than one piece of it',
      'Families, because the day has enough variety to hold children through it',
    ],
    notForWho:
      'If you would rather see one thing properly than four things briefly, take a half-day tour. Nine hours across four stops is a full day by any measure, and it is a lot for a very young child.',
    costFactors: [
      'Group size, because a private vehicle for a full day is split across everyone in it',
      'Kenya Wildlife Service park entry fees plus three separate attraction entries',
      'Vehicle type, since a full day in a Land Cruiser costs more than a van',
      'Whether you swap a stop, for example Bomas of Kenya instead of the Karen Blixen Museum',
      'Airport pickup or drop-off, which adds distance at either end',
    ],
    depth: [
      {
        heading: 'Why this specific order, and what is fixed',
        body: [
          'Two things in this day cannot move. Nairobi National Park opens its gates at 6:00am, and the Sheldrick Wildlife Trust opens to general visitors from 11:00am to noon only. Every other stop is arranged around those two fixed points, which is why the day starts before dawn.',
          'The remaining stops are ordered by geography rather than preference. Sheldrick, the Giraffe Centre and the Karen Blixen Museum all sit in the Langata and Karen area on the park’s northern edge, so once the game drive ends you barely drive again. That is what makes four stops possible in a day without the day becoming a car journey.',
          'Lunch sits at 12:30pm on purpose. It falls between the fixed morning and the flexible afternoon, so if the game drive runs long on a good sighting, lunch absorbs it rather than the afternoon collapsing.',
        ],
      },
      {
        heading: 'Doing this as an airport layover',
        body: [
          'Jomo Kenyatta International Airport sits about 20 minutes from the Nairobi National Park gate outside peak hours, which is why a long layover works here in a way it would not in most capital cities.',
          'You need 12 hours or more between landing and check-in to do the full day comfortably, and you need to be able to clear Kenyan immigration, which for most nationalities now means an approved electronic travel authorisation obtained before you fly. Check your own requirements well before the date, because that approval is not instant.',
          'Send us your flight numbers rather than just times. Your guide tracks the inbound flight, adjusts for delays, and builds a hard cut-off into the afternoon so you are back at the terminal with margin rather than hope.',
        ],
      },
      {
        heading: 'Swapping stops to suit you',
        body: [
          'The four-stop itinerary above is the standard version because it gives the widest range, but it is not compulsory. Common swaps include Bomas of Kenya in place of the Karen Blixen Museum for cultural performance, the Nairobi National Museum for paleontology and Kenyan history, and Kazuri Beads for a short craft and cooperative stop.',
          'You can also drop a stop entirely and spend longer in the park. A 5-hour game drive plus the orphanage plus lunch is a calmer day than four attractions, and for wildlife-focused visitors it is usually the better one.',
          'Tell us which of the four matters most when you enquire, because we would rather build the day around your priority than hand you a fixed list.',
        ],
      },
    ],
    faqs: [
      {
        q: 'How long is the Nairobi day trip?',
        a: '7 to 9 hours door to door, starting with a 5:45am pickup and finishing between 4:30pm and 6:00pm depending on how many stops you include and where you are staying.',
      },
      {
        q: 'Can I do the Nairobi day trip on a layover?',
        a: 'Yes, with 12 hours or more between flights and the right entry approval for Kenya. We collect you from the terminal, run the day with a hard cut-off, and return you in time to check in. Send your flight numbers when you book.',
      },
      {
        q: 'What is the difference between the day trip and a half-day tour?',
        a: 'A half-day tour is 4 to 6 hours and covers one thing well, usually a game drive or one part of the city. The full-day trip is 7 to 9 hours and covers four stops, which is the park, the elephant orphanage, the Giraffe Centre and Karen.',
      },
      {
        q: 'Is lunch included in the day trip?',
        a: 'Lunch is not included, but a lunch stop is built into the schedule at around 12:30pm in Karen. You choose the restaurant and pay for your own meal, and your guide will recommend options at whatever price level suits you.',
      },
    ],
  },
];

export const tourBySlug = (slug: string) => tours.find((t) => t.slug === slug);

export const categoryLabel: Record<Tour['category'], string> = {
  park: 'Nairobi National Park',
  combo: 'Park plus an animal stop',
  city: 'Nairobi city',
  'full-day': 'Full day',
};
