"""Content for Nairobi.guide.

All copy here is original. Listings carry no star ratings: we describe what a
place is and who it suits, and leave live ratings, prices and hours to the
venue's own channels. Price bands: 1 = budget, 2 = mid-range, 3 = upmarket,
4 = splurge.
"""

SITE = {
    "name": "Nairobi.guide",
    "domain": "nairobi.guide",
    "tagline": "The city, properly explained",
    "description": (
        "An independent guide to Nairobi: where to eat, sleep, explore and go out, "
        "neighbourhood by neighbourhood, written by people who live here."
    ),
}

# Top-level sections. Each one is a listing category with its own sub-types.
SECTIONS = {
    "eat": {
        "title": "Eat",
        "headline": "Where to eat in Nairobi",
        "intro": (
            "Nairobi eats well at every price. Roadside nyama choma joints, Swahili "
            "kitchens, long Sunday brunches in Karen and serious tasting menus in "
            "Westlands all share the same few square kilometres."
        ),
        "blurb": "Nyama choma, brunch, Swahili kitchens and fine dining",
        "tone": "ochre",
        "types": {
            "nyama-choma": "Nyama choma & grills",
            "kenyan": "Kenyan & Swahili",
            "brunch-cafes": "Brunch & cafés",
            "fine-dining": "Fine dining",
            "international": "International",
        },
    },
    "stay": {
        "title": "Stay",
        "headline": "Where to stay in Nairobi",
        "intro": (
            "Choosing a base in Nairobi is mostly about traffic. Pick the area first "
            "(Westlands for nightlife, Karen for gardens, the CBD for history, "
            "Langata for the park) and the hotel second."
        ),
        "blurb": "Historic hotels, garden cottages and camps by the park",
        "tone": "forest",
        "types": {
            "historic": "Historic hotels",
            "boutique": "Boutique & design",
            "safari-style": "Safari-style stays",
            "budget": "Budget & backpacker",
        },
    },
    "visit": {
        "title": "Visit",
        "headline": "Things to see in Nairobi",
        "intro": (
            "Nairobi is the only capital city with a national park inside its "
            "limits, and plenty more besides: forests with waterfalls, elephant "
            "orphans, colonial-era museums and a skyline you can watch from a rooftop "
            "helipad."
        ),
        "blurb": "Wildlife, forests, museums and viewpoints",
        "tone": "savanna",
        "types": {
            "wildlife": "Wildlife",
            "nature": "Forests & outdoors",
            "museums": "Museums & history",
            "culture": "Culture & crafts",
        },
    },
    "play": {
        "title": "Play",
        "headline": "Going out in Nairobi",
        "intro": (
            "Nairobi goes out late and dresses up for it. Westlands is the "
            "centre of the action. Live music, theatre and quieter garden bars are "
            "spread across the rest of the city."
        ),
        "blurb": "Bars, live music, theatre and weekends out",
        "tone": "dusk",
        "types": {
            "bars": "Bars & lounges",
            "live-music": "Live music & clubs",
            "arts": "Theatre & arts",
            "active": "Active & outdoors",
        },
    },
}

# Neighbourhoods. `vibe` is a one-liner; `body` is the long description.
AREAS = [
    {
        "slug": "westlands",
        "name": "Westlands",
        "vibe": "Malls, offices and the city's busiest nightlife",
        "body": (
            "Westlands is Nairobi's second downtown: glass office towers, the Sarit "
            "and Westgate malls, and more restaurants and bars per street than "
            "anywhere else in the city. Stay here if you want to walk to dinner and "
            "take a short ride home after a late night. Traffic on Waiyaki Way "
            "builds early, so leave extra time for airport runs."
        ),
        "good_for": ["Nightlife", "Restaurants", "Business trips"],
    },
    {
        "slug": "karen",
        "name": "Karen",
        "vibe": "Leafy, quiet and close to the giraffes",
        "body": (
            "Named after the Danish author Karen Blixen, whose farmhouse is now a "
            "museum here, Karen is big plots, old trees and garden restaurants. It's "
            "the most relaxed base in the city and handy for the Giraffe Centre, "
            "Sheldrick elephant orphanage and the Ngong Hills. Expect to drive "
            "everywhere, and allow an hour or more to reach Westlands at rush hour."
        ),
        "good_for": ["Families", "Garden dining", "Wildlife"],
    },
    {
        "slug": "kilimani",
        "name": "Kilimani",
        "vibe": "Apartments, cafés and local favourites",
        "body": (
            "Kilimani sits between the CBD and Lavington. It's a residential "
            "neighbourhood of apartment blocks, serviced flats and some of the city's "
            "best-loved everyday restaurants. It suits longer stays, and Yaya Centre "
            "and Prestige Plaza cover the basics."
        ),
        "good_for": ["Long stays", "Local food", "Value"],
    },
    {
        "slug": "cbd",
        "name": "City Centre (CBD)",
        "vibe": "Historic hotels, markets and the old city",
        "body": (
            "Nairobi's Central Business District holds the city's history: the "
            "Stanley and Norfolk hotels, the national archives, City Market and "
            "KICC tower. It's busy and best explored by day. For a first look, "
            "walk Kenyatta Avenue to Kimathi Street, then go up the KICC helipad "
            "for the view."
        ),
        "good_for": ["History", "Markets", "First-time visitors"],
    },
    {
        "slug": "langata",
        "name": "Langata",
        "vibe": "Next door to Nairobi National Park",
        "body": (
            "Langata runs along the northern edge of Nairobi National Park. "
            "It's home to Carnivore, Bomas of Kenya and the Giraffe Centre, along "
            "with several camps where you can hear the park at night. Stay here "
            "for an early game drive, since the main gate is minutes away."
        ),
        "good_for": ["Safari", "Families", "Early starts"],
    },
    {
        "slug": "gigiri",
        "name": "Gigiri",
        "vibe": "Diplomatic quarter on the northern edge",
        "body": (
            "Gigiri is home to the UN Office at Nairobi and most of the embassies. "
            "It's green and well secured, and Village Market has shops, cinemas and "
            "restaurants. It's a calm base for official visits and close to Karura "
            "Forest."
        ),
        "good_for": ["Business trips", "Quiet stays", "Karura Forest"],
    },
    {
        "slug": "upper-hill",
        "name": "Upper Hill",
        "vibe": "Corporate towers between the CBD and Ngong Road",
        "body": (
            "Upper Hill is Nairobi's banking and hospital district, a ridge of "
            "headquarters and big international hotels. It's well placed for both "
            "the CBD and Kilimani, and quieter at weekends."
        ),
        "good_for": ["Business trips", "Big-brand hotels"],
    },
    {
        "slug": "parklands",
        "name": "Parklands",
        "vibe": "Old Nairobi, Indian kitchens and the Arboretum side",
        "body": (
            "Parklands, just east of Westlands, is one of the city's older "
            "neighbourhoods and the heart of Nairobi's South Asian community. Come "
            "for vegetarian thalis, sweet shops and City Park, a forest remnant "
            "with a resident troop of Sykes' monkeys."
        ),
        "good_for": ["Indian food", "City Park", "Value"],
    },
]

# Listings. Facts here are deliberately stable (what a place is, where, why go).
# Live details (hours, prices, ratings) belong on the venue's own channels.
LISTINGS = [
    # ---------------- EAT ----------------
    {
        "section": "eat", "type": "nyama-choma", "slug": "carnivore",
        "name": "Carnivore", "area": "langata", "price": 3,
        "summary": "Nairobi's best-known meat feast, carved at your table off Maasai swords.",
        "body": (
            "Carnivore has been on every first-timer's list for decades. Waiters "
            "carry roasted meats around the room on long skewers and keep carving "
            "until you lower the paper flag on your table. It's theatrical, loud "
            "and great fun in a group. Vegetarians get their own menu, and the "
            "Simba Saloon next door turns into a club later on."
        ),
        "tips": ["Arrive hungry and pace yourself", "Book ahead on weekends", "Combine with an afternoon at Nairobi National Park"],
        "tags": ["nyama choma", "groups", "classic"],
    },
    {
        "section": "eat", "type": "kenyan", "slug": "mama-oliech",
        "name": "Mama Oliech", "area": "kilimani", "price": 1,
        "summary": "Whole fried tilapia and ugali, the plain-spoken Luo classic.",
        "body": (
            "Mama Oliech is a Nairobi institution for one dish: whole deep-fried "
            "tilapia, served with ugali, sukuma wiki and kachumbari, and eaten with "
            "your hands. The room is simple and the service is quick. This is a fish "
            "restaurant first, so skip it if fish isn't your thing."
        ),
        "tips": ["Wash your hands at the basin and eat with them", "Lunchtime gets very busy"],
        "tags": ["fish", "local favourite", "budget"],
    },
    {
        "section": "eat", "type": "kenyan", "slug": "kosewe",
        "name": "Kosewe Ranalo Foods", "area": "cbd", "price": 1,
        "summary": "No-frills downtown canteen for fish, ugali and greens.",
        "body": (
            "Kosewe has been feeding downtown office workers for years with "
            "western-Kenyan home cooking: fish stews, ugali, managu and omena. "
            "Service is fast and bills are small, and it's the best way to see the "
            "CBD at lunchtime."
        ),
        "tips": ["Go between 12:00 and 14:00 for the full buzz", "Order the fish wet-fry if you prefer a sauce"],
        "tags": ["fish", "downtown", "budget"],
    },
    {
        "section": "eat", "type": "nyama-choma", "slug": "nyama-mama",
        "name": "Nyama Mama", "area": "westlands", "price": 2,
        "summary": "Playful, colourful take on Kenyan comfort food.",
        "body": (
            "Nyama Mama takes kiosk and home-kitchen favourites like mandazi, "
            "chapati, pilau and choma and gives them a modern, fun treatment in a "
            "riot of colour. It's an easy introduction to Kenyan flavours if you're "
            "nervous of street food, and good for groups."
        ),
        "tips": ["Try the cocktails built on Kenyan ingredients", "Good for a relaxed first-night dinner"],
        "tags": ["modern kenyan", "groups", "cocktails"],
    },
    {
        "section": "eat", "type": "brunch-cafes", "slug": "java-house",
        "name": "Java House", "area": "westlands", "price": 1,
        "summary": "The homegrown coffee chain you'll find on every corner.",
        "body": (
            "Java House started in Nairobi in 1999 and is now the default for "
            "reliable Kenyan coffee, full breakfasts and working lunches with Wi-Fi. "
            "There's a branch in almost every mall and at the airport. It isn't "
            "exciting, but it's always dependable."
        ),
        "tips": ["Order a Kenyan AA filter", "Branches at JKIA are handy before an early flight"],
        "tags": ["coffee", "breakfast", "wifi"],
    },
    {
        "section": "eat", "type": "brunch-cafes", "slug": "talisman",
        "name": "The Talisman", "area": "karen", "price": 3,
        "summary": "Long, lazy garden lunches in a converted Karen farmhouse.",
        "body": (
            "The Talisman is a Karen stalwart. Its rooms open onto a garden, the "
            "fusion menu travels from East Africa to Asia, and the crowd stays all "
            "afternoon. It's a classic stop after the Giraffe Centre or the Blixen "
            "Museum, and the fireplace makes it cosy on cool July evenings."
        ),
        "tips": ["Book for Sunday lunch", "Pair with the Karen Blixen Museum nearby"],
        "tags": ["garden", "brunch", "karen"],
    },
    {
        "section": "eat", "type": "fine-dining", "slug": "cultiva",
        "name": "Cultiva", "area": "karen", "price": 3,
        "summary": "Farm-to-table cooking from its own Karen kitchen garden.",
        "body": (
            "Cultiva grows much of what it serves in the garden around the "
            "restaurant. The seasonal menu leans on wood-fire cooking and Kenyan "
            "produce. It's one of the city's best places for a long, unhurried "
            "dinner."
        ),
        "tips": ["Ask for a garden-side table", "Menus change with the harvest"],
        "tags": ["farm to table", "seasonal", "date night"],
    },
    {
        "section": "eat", "type": "fine-dining", "slug": "about-thyme",
        "name": "About Thyme", "area": "westlands", "price": 3,
        "summary": "Garden dining in a quiet corner of Westlands.",
        "body": (
            "About Thyme sits in a house and garden off a busy Westlands street. It "
            "has a broad international menu, a solid wine list and a fire pit on "
            "cool nights. It's a dependable choice for client dinners and "
            "celebrations."
        ),
        "tips": ["Outdoor tables fill first", "Good for a calm business dinner"],
        "tags": ["garden", "wine", "business"],
    },
    {
        "section": "eat", "type": "international", "slug": "haandi",
        "name": "Haandi", "area": "westlands", "price": 3,
        "summary": "North Indian cooking from the tandoor, a city favourite for decades.",
        "body": (
            "Haandi is the place Nairobi goes for a big North Indian meal: "
            "tandoori platters, rich curries and fresh naan from a kitchen you can "
            "watch through glass. Nairobi's long Indian heritage means the standard "
            "is high, and Haandi has held its place for a long time."
        ),
        "tips": ["Order breads for the table", "Weekend evenings are busy, so book"],
        "tags": ["indian", "groups", "vegetarian friendly"],
    },
    {
        "section": "eat", "type": "kenyan", "slug": "swahili-plate",
        "name": "Swahili food in Parklands", "area": "parklands", "price": 1,
        "summary": "Biryani, pilau and samosas: coastal flavours without the flight.",
        "body": (
            "The coast's Swahili kitchen made its way up to Nairobi a long time "
            "ago. Around Parklands and Highridge, small family places serve "
            "biryani, pilau, bhajia and samosas for very little money. Follow the "
            "lunchtime crowds and order what the next table is having."
        ),
        "tips": ["Fridays bring special biryani", "Many places close for midday prayers on Friday"],
        "tags": ["swahili", "budget", "street food"],
    },

    # ---------------- STAY ----------------
    {
        "section": "stay", "type": "historic", "slug": "fairmont-the-norfolk",
        "name": "Fairmont The Norfolk", "area": "cbd", "price": 4,
        "summary": "Opened in 1904, the grande dame of colonial Nairobi.",
        "body": (
            "The Norfolk opened in 1904, which makes it almost as old as Nairobi. "
            "Its Lord Delamere Terrace was once the departure point for "
            "colonial-era safaris. Today it has landscaped courtyards, a "
            "spa and some of the city's most storied bars. It's close to the "
            "National Theatre and the University of Nairobi."
        ),
        "tips": ["Have a drink on the Delamere Terrace even if you're not staying", "Ask about the hotel's history displays"],
        "tags": ["historic", "luxury", "city centre"],
    },
    {
        "section": "stay", "type": "historic", "slug": "sarova-stanley",
        "name": "The Sarova Stanley", "area": "cbd", "price": 3,
        "summary": "Downtown landmark since 1902, home of the Thorn Tree café.",
        "body": (
            "The Stanley has stood at the corner of Kimathi Street and Kenyatta "
            "Avenue since 1902. Its Thorn Tree Café, named for the acacia that "
            "travellers once used as a message board, is still a downtown meeting "
            "point. It's the best base for exploring the CBD on foot."
        ),
        "tips": ["Breakfast at the Thorn Tree Café", "Good base for walking tours of the CBD"],
        "tags": ["historic", "city centre", "walkable"],
    },
    {
        "section": "stay", "type": "safari-style", "slug": "giraffe-manor",
        "name": "Giraffe Manor", "area": "langata", "price": 4,
        "summary": "The 1930s manor where Rothschild giraffes join you for breakfast.",
        "body": (
            "Giraffe Manor is a 1930s house on land shared with the Giraffe Centre. "
            "Its resident Rothschild giraffes poke their heads through the windows "
            "at breakfast. It's small, very expensive and booked up months in "
            "advance, and it's on plenty of bucket lists for good reason."
        ),
        "tips": ["Book as early as you can", "If it's full, visit the Giraffe Centre next door instead"],
        "tags": ["bucket list", "wildlife", "luxury"],
    },
    {
        "section": "stay", "type": "safari-style", "slug": "emakoko",
        "name": "The Emakoko", "area": "langata", "price": 4,
        "summary": "A lodge inside Nairobi National Park, across the river from the city.",
        "body": (
            "The Emakoko is one of very few places to sleep inside Nairobi National "
            "Park. It's set on a river valley on the park's southern side, so "
            "lions and rhinos are your neighbours and the skyline feels a world "
            "away. Game drives go straight from the door, and the airport is close "
            "for arrival or departure days."
        ),
        "tips": ["Ideal first or last night of a Kenyan safari", "Rates usually include game drives, so check what's covered"],
        "tags": ["safari", "luxury", "airport-friendly"],
    },
    {
        "section": "stay", "type": "boutique", "slug": "hemingways-nairobi",
        "name": "Hemingways Nairobi", "area": "karen", "price": 4,
        "summary": "Colonial-style suites with views of the Ngong Hills.",
        "body": (
            "Hemingways is an all-suite boutique hotel in Karen with plantation-style "
            "architecture, big verandas and views west to the Ngong Hills. It's "
            "quiet, polished and close to Karen's attractions."
        ),
        "tips": ["Ask for a hills-facing suite", "Sundowners on the terrace are worth it"],
        "tags": ["boutique", "karen", "luxury"],
    },
    {
        "section": "stay", "type": "boutique", "slug": "tribe-hotel",
        "name": "Tribe Hotel", "area": "gigiri", "price": 3,
        "summary": "Design hotel beside Village Market with a big African art collection.",
        "body": (
            "Tribe is a contemporary design hotel next to Village Market in Gigiri, "
            "filled with art and objects from across the continent. It's popular "
            "with diplomats and business travellers, and the rooftop and pool are "
            "good places to unwind."
        ),
        "tips": ["Walk straight into Village Market for shopping and dining", "Close to the UN complex and Karura Forest"],
        "tags": ["design", "business", "gigiri"],
    },
    {
        "section": "stay", "type": "safari-style", "slug": "ole-sereni",
        "name": "Ole Sereni", "area": "langata", "price": 3,
        "summary": "Hotel terraces overlooking Nairobi National Park.",
        "body": (
            "Ole Sereni sits on Mombasa Road right on the park's northern boundary. "
            "Its terraces look out over the plains, so you might watch "
            "giraffes or buffalo with your breakfast. It's quick to reach from "
            "JKIA, which makes it practical for short layovers."
        ),
        "tips": ["Ask for a park-view room", "Good for overnight transits via JKIA"],
        "tags": ["park views", "airport-friendly"],
    },
    {
        "section": "stay", "type": "budget", "slug": "wildebeest-eco-camp",
        "name": "Wildebeest Eco Camp", "area": "langata", "price": 1,
        "summary": "Tents, dorms and a sociable garden for safari-goers on a budget.",
        "body": (
            "Wildebeest Eco Camp offers garden tents, cottages and dorm beds in "
            "Langata. It's a favourite meeting point for budget travellers before "
            "and after group safaris. It's relaxed and friendly, with lots of "
            "people swapping trip notes."
        ),
        "tips": ["Many budget safari operators pick up from here", "Book the en-suite tents early in peak season"],
        "tags": ["budget", "backpacker", "social"],
    },

    # ---------------- VISIT ----------------
    {
        "section": "visit", "type": "wildlife", "slug": "nairobi-national-park",
        "name": "Nairobi National Park", "area": "langata", "price": 2,
        "summary": "Lions, rhinos and giraffes with the skyline behind them.",
        "body": (
            "Gazetted in 1946, Nairobi National Park was Kenya's first national "
            "park. It's mostly open grassland, fenced on the city side and open to "
            "the south so animals can move. It's one of the best places in "
            "the country to see black rhino, and lions, buffalo, giraffes and big "
            "herds of plains game are regulars. Pictures of giraffes in front "
            "of the skyline are the reason people come."
        ),
        "tips": ["Go at gate opening for the best sightings", "Entry is cashless, so pay via the official KWS channels", "Half a day is enough for a good loop"],
        "tags": ["safari", "rhino", "half day"],
    },
    {
        "section": "visit", "type": "wildlife", "slug": "sheldrick-elephant-orphanage",
        "name": "Sheldrick Elephant Orphanage", "area": "langata", "price": 2,
        "summary": "Orphaned baby elephants at their midday mud bath and feed.",
        "body": (
            "The Sheldrick Wildlife Trust rescues orphaned elephants and rhinos "
            "from across Kenya and raises them at its nursery inside Nairobi "
            "National Park. Visitors can watch the babies' daily feed and mud bath "
            "while keepers talk about each orphan's story. Visiting slots are "
            "limited and must be booked in advance on the trust's own website."
        ),
        "tips": ["Book online before you go, as walk-ins aren't accepted", "Fostering an orphan gets you an evening visit too"],
        "tags": ["elephants", "conservation", "families"],
    },
    {
        "section": "visit", "type": "wildlife", "slug": "giraffe-centre",
        "name": "Giraffe Centre", "area": "langata", "price": 1,
        "summary": "Feed endangered Rothschild giraffes from a raised platform.",
        "body": (
            "The Giraffe Centre is run by the African Fund for Endangered Wildlife "
            "(Kenya), which has bred and released Rothschild giraffes since the "
            "1970s. You climb a platform to meet them at eye level and hand over "
            "food pellets. A short nature trail across the road makes a nice "
            "add-on."
        ),
        "tips": ["Mornings are quieter", "Pair with the Sheldrick orphanage the same day"],
        "tags": ["giraffes", "families", "conservation"],
    },
    {
        "section": "visit", "type": "nature", "slug": "karura-forest",
        "name": "Karura Forest", "area": "gigiri", "price": 1,
        "summary": "Trails, a waterfall and Mau Mau caves inside the city.",
        "body": (
            "Karura is one of the largest urban forests in the world. It was saved "
            "from developers thanks to campaigners led by Nobel laureate Wangari "
            "Maathai. Walking and cycling trails lead to a waterfall, "
            "caves used during the Mau Mau struggle, and a quiet riverside café. "
            "Bikes are available to hire at the main gate."
        ),
        "tips": ["Go early on weekends before it gets busy", "Bring a small amount of cash or M-Pesa for entry"],
        "tags": ["hiking", "cycling", "free-ish"],
    },
    {
        "section": "visit", "type": "nature", "slug": "ngong-hills",
        "name": "Ngong Hills", "area": "karen", "price": 1,
        "summary": "A ridge walk with Rift Valley views on one side and the city on the other.",
        "body": (
            "The Ngong Hills rise just beyond Karen. A ridge trail runs along their "
            "knuckled peaks, with the Great Rift Valley dropping away to the west "
            "and Nairobi spread out to the east. It's a half-day walk at a steady "
            "pace, and the wind farm along the ridge is a striking sight."
        ),
        "tips": ["Hike with a guide or ranger, which is easily arranged at the gate", "Start early and bring water and a windproof layer"],
        "tags": ["hiking", "views", "half day"],
    },
    {
        "section": "visit", "type": "museums", "slug": "nairobi-national-museum",
        "name": "Nairobi National Museum", "area": "cbd", "price": 1,
        "summary": "Kenya's story from early humans to independence.",
        "body": (
            "The National Museum on Museum Hill covers prehistory (East Africa's "
            "fossil finds are world-famous), birds, culture and the road to "
            "independence. The botanical gardens and snake park on the same ticket "
            "are good for a gentle afternoon."
        ),
        "tips": ["Allow two to three hours", "The snake park is a hit with children"],
        "tags": ["history", "rainy day", "families"],
    },
    {
        "section": "visit", "type": "museums", "slug": "karen-blixen-museum",
        "name": "Karen Blixen Museum", "area": "karen", "price": 1,
        "summary": "The farmhouse of the author of Out of Africa.",
        "body": (
            "This farmhouse was home to the Danish writer Karen Blixen from 1917 to "
            "1931, the years behind her memoir Out of Africa. Guided tours "
            "go through her rooms and furniture, and the gardens look towards "
            "the Ngong Hills she wrote about."
        ),
        "tips": ["Tours are short; combine with lunch in Karen", "Read a few pages of Out of Africa first"],
        "tags": ["history", "literature", "karen"],
    },
    {
        "section": "visit", "type": "museums", "slug": "nairobi-railway-museum",
        "name": "Nairobi Railway Museum", "area": "cbd", "price": 1,
        "summary": "Steam engines from the railway that founded the city.",
        "body": (
            "Nairobi began in 1899 as a depot on the Uganda Railway, and this museum "
            "beside the old station tells that story. You can climb aboard vintage "
            "locomotives and carriages in the yard. It's a must for train fans and "
            "a good insight into why the city exists at all."
        ),
        "tips": ["Climb into the engines in the yard", "Allow about 90 minutes"],
        "tags": ["history", "trains", "families"],
    },
    {
        "section": "visit", "type": "culture", "slug": "bomas-of-kenya",
        "name": "Bomas of Kenya", "area": "langata", "price": 1,
        "summary": "Traditional homesteads and daily dance performances.",
        "body": (
            "Bomas recreates the traditional homesteads of many of Kenya's "
            "communities and stages afternoon performances of music and dance "
            "from across the country. It's a quick introduction to Kenya's "
            "cultural diversity, close to the national park."
        ),
        "tips": ["Time your visit for the afternoon performance", "Combine with the Giraffe Centre"],
        "tags": ["culture", "dance", "families"],
    },
    {
        "section": "visit", "type": "culture", "slug": "kazuri-beads",
        "name": "Kazuri Beads", "area": "karen", "price": 1,
        "summary": "Watch hand-made ceramic beads being shaped and painted.",
        "body": (
            "Kazuri began in 1975 as a small workshop employing single mothers and "
            "now employs hundreds of artisans. A free tour follows the beads from "
            "clay to kiln to paint, and the shop sells the finished jewellery and "
            "pottery."
        ),
        "tips": ["Tours are free", "Good place for gifts that support local jobs"],
        "tags": ["crafts", "shopping", "social enterprise"],
    },
    {
        "section": "visit", "type": "culture", "slug": "kicc-rooftop",
        "name": "KICC Rooftop", "area": "cbd", "price": 1,
        "summary": "360° views of the city from a helipad on Nairobi's iconic tower.",
        "body": (
            "The Kenyatta International Convention Centre, with its cylindrical "
            "tower and conical amphitheatre, is a landmark of 1970s Nairobi. "
            "Visitors can go up to the rooftop helipad for the best panorama in "
            "town. On clear days, look for the Ngong Hills and even Mount Kenya."
        ),
        "tips": ["Go late afternoon for the light", "Bring ID for security checks"],
        "tags": ["views", "architecture", "city centre"],
    },
    {
        "section": "visit", "type": "culture", "slug": "maasai-market",
        "name": "Maasai Market", "area": "cbd", "price": 1,
        "summary": "A travelling craft market: beadwork, kikoys, carvings and baskets.",
        "body": (
            "The Maasai Market moves around the city through the week, setting up "
            "at different malls and open spaces on different days. Expect "
            "beadwork, kiondo baskets, soapstone, kikoys and carvings. Prices "
            "start high and haggling is normal and expected."
        ),
        "tips": ["Check which location it's at that day", "Haggle with a smile and decide your top price first"],
        "tags": ["shopping", "crafts", "souvenirs"],
    },

    # ---------------- PLAY ----------------
    {
        "section": "play", "type": "bars", "slug": "westlands-strip",
        "name": "The Westlands strip", "area": "westlands", "price": 2,
        "summary": "A dense run of bars, rooftops and clubs for a big night out.",
        "body": (
            "Most of Nairobi's big nights start and end in Westlands. Lounges, "
            "rooftop bars, sports bars and clubs are packed into a few blocks, and "
            "the busiest nights run Thursday to Saturday. It's easy to hop between "
            "places, but use a ride-hailing app between venues late at night."
        ),
        "tips": ["Things get going late, after 22:00", "Use Uber or Bolt between venues at night"],
        "tags": ["nightlife", "rooftops", "clubs"],
    },
    {
        "section": "play", "type": "live-music", "slug": "alchemist",
        "name": "The Alchemist", "area": "westlands", "price": 2,
        "summary": "Open-air bar, food trucks and DJs in a converted yard.",
        "body": (
            "The Alchemist mixes food trucks, open-air bars and a stage in one big "
            "yard. You'll get DJs most nights, live acts and the occasional market "
            "by day. It's young, creative and one of the easiest places to see "
            "where Nairobi's music scene is heading."
        ),
        "tips": ["Check their socials for the week's line-up", "Weekend daytime events are more relaxed"],
        "tags": ["live music", "food trucks", "dj"],
    },
    {
        "section": "play", "type": "arts", "slug": "kenya-national-theatre",
        "name": "Kenya National Theatre", "area": "cbd", "price": 1,
        "summary": "Plays, poetry and performance opposite the Norfolk.",
        "body": (
            "The Kenya National Theatre, across from the Norfolk Hotel, hosts drama, "
            "dance, spoken word and festival seasons in English and Kiswahili. It's "
            "a good way to see contemporary Kenyan storytelling up close."
        ),
        "tips": ["Look for school-holiday productions and festivals", "Pair with a drink at the Norfolk"],
        "tags": ["theatre", "culture", "evening"],
    },
    {
        "section": "play", "type": "active", "slug": "ngong-racecourse",
        "name": "Ngong Racecourse", "area": "karen", "price": 1,
        "summary": "Sunday horse racing with a picnic crowd.",
        "body": (
            "Ngong Racecourse has hosted horse racing since the 1950s, with "
            "meetings on selected Sundays. The atmosphere is relaxed and social. "
            "It also hosts concerts and festivals on its large grounds."
        ),
        "tips": ["Check the fixture list before you go", "Bring a hat and sunscreen"],
        "tags": ["sport", "weekend", "events"],
    },
    {
        "section": "play", "type": "active", "slug": "city-park",
        "name": "City Park", "area": "parklands", "price": 1,
        "summary": "Forest walks and Sykes' monkeys a few minutes from Westlands.",
        "body": (
            "City Park is a patch of indigenous forest that has survived inside "
            "the city. It has walking paths, a historic cemetery and a lively troop "
            "of Sykes' monkeys. It's an easy breath of green between meetings."
        ),
        "tips": ["Don't feed the monkeys, however much they ask", "Weekday mornings are calmest"],
        "tags": ["walks", "monkeys", "free"],
    },
]

EXPERIENCES = [
    {
        "slug": "early-game-drive",
        "name": "Sunrise game drive in Nairobi National Park",
        "duration": "4–5 hours",
        "category": "Wildlife",
        "summary": "Out at gate opening, back for a late breakfast, with rhino and lion the main hopes.",
    },
    {
        "slug": "elephants-and-giraffes",
        "name": "Elephants & giraffes day",
        "duration": "Half day",
        "category": "Wildlife",
        "summary": "The Sheldrick orphanage's midday feed followed by the Giraffe Centre, with lunch in Karen.",
    },
    {
        "slug": "cbd-walking-tour",
        "name": "Old Nairobi walking tour",
        "duration": "3 hours",
        "category": "Culture",
        "summary": "From the railway station to the Stanley, City Market and the KICC helipad.",
    },
    {
        "slug": "street-food-crawl",
        "name": "Street-food crawl",
        "duration": "3 hours",
        "category": "Food",
        "summary": "Mutura, smokies, samosas, mandazi and chai, eaten where Nairobians eat them.",
    },
    {
        "slug": "naivasha-day-trip",
        "name": "Lake Naivasha & Hell's Gate",
        "duration": "Full day",
        "category": "Day trip",
        "summary": "Cycle through Hell's Gate gorge, then take a boat among Naivasha's hippos. About two hours each way.",
    },
    {
        "slug": "karura-cycle",
        "name": "Karura Forest by bike",
        "duration": "2–3 hours",
        "category": "Outdoors",
        "summary": "Hire a bike at the gate and ride shaded trails to the waterfall and Mau Mau caves.",
    },
    {
        "slug": "ngong-hike",
        "name": "Ngong Hills ridge hike",
        "duration": "Half day",
        "category": "Outdoors",
        "summary": "Seven knuckles of ridge with the Rift Valley on one side and the city on the other.",
    },
    {
        "slug": "kibera-community",
        "name": "Community-led neighbourhood walk",
        "duration": "3 hours",
        "category": "Culture",
        "summary": "Choose walks run by residents' own organisations, where the fee stays in the community.",
    },
]

# Long-form guides. `sections` is a list of (heading, paragraphs[]).
GUIDES = [
    {
        "slug": "getting-around-nairobi",
        "title": "Getting around Nairobi",
        "dek": "Ride-hailing, matatus, the Expressway and the new trains: how to beat the traffic.",
        "sections": [
            ("Ride-hailing is the default", [
                "Uber, Bolt and local alternatives cover the whole city and are the "
                "simplest way to get around. Fares are shown upfront and you can pay by "
                "card, cash or M-Pesa. Confirm the plate number before you get in.",
            ]),
            ("Matatus: the city's real network", [
                "Matatus are privately run minibuses, often painted in loud graffiti "
                "with music to match. They're cheap and cover everywhere. Routes are "
                "numbered, most fares are paid by M-Pesa or cash to the conductor, and "
                "they're best for daytime trips on routes you've had explained.",
            ]),
            ("The Nairobi Expressway", [
                "The elevated toll road links JKIA to Westlands along Mombasa Road and "
                "Uhuru Highway. It can turn an hour-long airport transfer into "
                "twenty minutes. Most drivers will ask whether you want to take it, "
                "since the toll is added to the fare.",
            ]),
            ("Trains", [
                "Commuter trains run from the central station to the suburbs, and the "
                "Madaraka Express (SGR) runs from Nairobi Terminus at Syokimau to "
                "Mombasa in about five to six hours. Book SGR tickets in advance on the "
                "official Kenya Railways platform.",
            ]),
            ("Traffic rules of thumb", [
                "Rush hour runs roughly 06:30–09:30 and 16:30–20:00. Plan meetings "
                "in one area per day, and allow at least 90 minutes to reach JKIA from "
                "Westlands or Karen in the evening.",
            ]),
        ],
    },
    {
        "slug": "arriving-at-jkia",
        "title": "Arriving at JKIA",
        "dek": "Entry paperwork, SIM cards, money and getting into town.",
        "sections": [
            ("Before you fly: the eTA", [
                "Most visitors need an Electronic Travel Authorisation (eTA) before "
                "boarding. Apply only through the official government portal, a few "
                "days ahead of travel, and keep a copy of the approval on your phone. "
                "Rules and fees change, so check the portal rather than relying on "
                "third-party sites.",
            ]),
            ("SIM cards & M-Pesa", [
                "Safaricom and Airtel have counters in arrivals. You'll need your "
                "passport to register a SIM. Ask to set up M-Pesa at the same time, "
                "since it's the most useful thing on your phone in Kenya.",
            ]),
            ("Money", [
                "The currency is the Kenyan shilling (KES). Cards are widely accepted "
                "in hotels, malls and restaurants, while M-Pesa covers almost "
                "everything else. ATMs are in arrivals, and it's worth carrying some "
                "small notes for tips.",
            ]),
            ("Into the city", [
                "Pre-booked hotel transfers and ride-hailing apps are the easiest "
                "options. Use the official pickup zones. With the Expressway, "
                "Westlands is often 30 minutes away outside rush hour.",
            ]),
        ],
    },
    {
        "slug": "best-time-to-visit-nairobi",
        "title": "Best time to visit Nairobi",
        "dek": "Nairobi is mild all year. Here's what each season means for your trip.",
        "sections": [
            ("The climate in brief", [
                "At about 1,700 metres above sea level, Nairobi is rarely hot. Days are "
                "usually warm and nights cool. The long rains come roughly March to "
                "May and the short rains around November.",
            ]),
            ("June to October: dry and cool", [
                "This is the classic safari season, and also the coolest stretch in "
                "Nairobi. July mornings can be grey and chilly, so pack a fleece. It's "
                "the busiest and priciest time for lodges, especially when the "
                "migration is in the Masai Mara.",
            ]),
            ("January to February: warm and dry", [
                "These are the warmest, sunniest weeks of the year, with good game "
                "viewing and fewer crowds than mid-year. It's a sweet spot for a city "
                "break with a safari attached.",
            ]),
            ("The rains", [
                "Rain usually comes in afternoon downpours rather than all-day "
                "drizzle. Parks turn green, rates drop and photographers love the "
                "skies, but traffic gets worse when it pours.",
            ]),
        ],
    },
    {
        "slug": "staying-safe-in-nairobi",
        "title": "Staying safe in Nairobi",
        "dek": "Plain, practical advice for a city that's friendlier than its reputation.",
        "sections": [
            ("Everyday sense", [
                "Like any big city, Nairobi rewards a little awareness. Keep phones "
                "out of sight on busy streets, carry only what you need, and use "
                "ride-hailing after dark rather than walking.",
            ]),
            ("Getting about", [
                "Book rides in the app rather than accepting street offers, check the "
                "plate before getting in, and keep car windows up in slow traffic.",
            ]),
            ("Wildlife & nature", [
                "In parks, stay in the vehicle unless you're in a marked area. On hikes "
                "such as the Ngong Hills, go with a guide or ranger.",
            ]),
            ("Before you go", [
                "Check your government's current travel advice, register with your "
                "embassy if that's recommended, and get travel insurance that covers "
                "medical evacuation.",
            ]),
        ],
    },
    {
        "slug": "day-trips-from-nairobi",
        "title": "Day trips from Nairobi",
        "dek": "Lakes, gorges and big-game country, all within a few hours of the city.",
        "sections": [
            ("Lake Naivasha & Hell's Gate (≈2 hours)", [
                "This is the classic day out. Cycle among zebras and giraffes through "
                "Hell's Gate gorge, then take a boat ride among Naivasha's hippos and "
                "fish eagles. Crescent Island is a walking safari with no predators.",
            ]),
            ("Lake Nakuru (≈3 hours)", [
                "A fenced park that's strong on rhinos, both black and white, with "
                "flamingos on the lake in some seasons. It's a long day, but doable.",
            ]),
            ("Amboseli (≈4 hours)", [
                "Big elephant herds with Kilimanjaro behind them. It's possible as a "
                "very long day trip, but much better with one night.",
            ]),
            ("Lake Magadi (≈2 hours)", [
                "A soda lake in the southern Rift with pink-tinged flats, hot springs "
                "and seasonal flamingos. The drive down the escarpment is half the "
                "fun.",
            ]),
            ("Ol Donyo Sabuk & Fourteen Falls (≈1.5 hours)", [
                "A small mountain park with buffalo and forest walks, plus a broad "
                "waterfall nearby that's at its best after the rains.",
            ]),
        ],
    },
    {
        "slug": "nairobi-on-a-budget",
        "title": "Nairobi on a budget",
        "dek": "How to see the best of the city without safari-lodge prices.",
        "sections": [
            ("Eat where locals eat", [
                "A plate of fish and ugali, a biryani in Parklands or a chapati "
                "and beans lunch costs a fraction of mall dining, and it's often "
                "better food.",
            ]),
            ("Cheap and free sights", [
                "City Park and the Arboretum are free or close to it. Karura Forest, "
                "the Railway Museum and the Giraffe Centre all have modest entry fees, "
                "and Kazuri's workshop tour costs nothing.",
            ]),
            ("Share the safari", [
                "Group half-day trips into Nairobi National Park split the vehicle "
                "cost. Budget camps in Langata are where many shared safaris start.",
            ]),
            ("Pay like a local", [
                "Use M-Pesa for matatus, markets and small shops, and ask for "
                "resident or East African rates where they apply to you.",
            ]),
        ],
    },
]
