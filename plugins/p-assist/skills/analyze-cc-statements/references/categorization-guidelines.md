# Categorization Guidelines

Use these rules to categorize credit card transactions based on the `description` field. Descriptions often contain abbreviated, garbled, or Indonesian merchant names — use pattern matching and inference.

## Categories

### Food & Drinks

Split into two sub-categories:

**Essential** — groceries, daily necessities, home cooking supplies:
- Restaurants: any "RM" (Rumah Makan), "Warung", "Restoran", "Restaurant", "Kitchen", "Eatery"
- Supermarkets: Superindo, Indomaret, Alfamart, Alfamidi, Giant, Hypermart, Transmart, Ranch Market, Farmers Market, Lotte Mart, Hero
- Grocery/wet markets: Pasar, Sayurbox, TaniHub, Segari, HappyFresh
- Bakeries: BreadTalk, Holland Bakery, Tous Les Jours, Roti O
- Convenience stores: Circle K, FamilyMart, Lawson, 7-Eleven

**Social** — food delivery, cafes, bars:
- Cafes/coffee: Starbucks, Kopi Kenangan, Fore Coffee, Janji Jiwa, Tomoro, Flash Coffee, "Cafe", "Coffee", "Kopi"
- Food delivery: GrabFood, GoFood, ShopeeFood — look for "GRAB*FOOD", "GOFOOD", "SHOPEEFOOD" patterns in description
- Fast food: McDonalds, KFC, Burger King, Pizza Hut, Dominos, Hokben, CFC, Yoshinoya
- Bars/nightlife: "Bar", "Pub", "Lounge", "Club"

### Transport

- Ride-hailing: Grab (transport, not food), Gojek (not recurring), Maxim — look for "GRAB*TRANSPORT", "GRAB*CAR", "GRAB*BIKE", "MAXIM"
- Fuel: Shell, Pertamina, Total, BP, SPBU, Vivo
- Parking: "Parking", "Parkir"
- Tolls: "Toll", "Tol", "E-Toll", "Mandiri E-Money"
- Public transit: Transjakarta, KRL, MRT, LRT, "Commuter"
- Airlines/travel: Garuda, Lion Air, Citilink, Batik Air, Traveloka, Tiket.com

**Disambiguating Grab entries:** The description determines which category:
- Contains "FOOD" or "F-" → Food & Drinks (Social)
- Contains "TRANSPORT", "CAR", "BIKE", or just "GRAB*" with a trip reference → Transport
- If ambiguous, default to Transport (more common for card transactions)

### Shopping

- E-commerce: Shopee, Tokopedia, Lazada, Blibli, Bukalapak, JD.ID — look for "SHOPEE*", "TOKOPEDIA", "LAZADA"
- Retail/fashion: Uniqlo, H&M, Zara, Cotton On, Miniso, IKEA, ACE Hardware
- Electronics: iBox, Erafone, Digimap, Electronic City, "Apple Store"
- Marketplaces: Amazon, eBay, AliExpress
- Others: GOPAY transactions

### Subscriptions

- Streaming: Netflix, Spotify, YouTube Premium, Disney+, HBO Max, Vidio, WeTV, Viu
- Software/SaaS: iCloud, Google One, Apple, Microsoft 365, Adobe, Notion, ChatGPT, Claude
- Gaming: Steam, PlayStation, Xbox, Nintendo, App Store, Google Play (recurring)
- Fitness memberships: Celebrity Fitness, Gold's Gym, Anytime Fitness (if recurring monthly)
- **Cloud services / Infrastructure**: Alibaba Cloud, Biznet NEO, AWS, Google Cloud, Azure, Cloudflare, DigitalOcean, Vultr, Linode, Heroku, Vercel, Netlify
- **Domain/Hosting**: Namecheap, GoDaddy, Domain.com, hosting services
- **Other SaaS tools**: Canva, Figma, Dropbox, Notion, Monday.com, Zo Computer

**Identifying subscriptions:** Look for recurring charges with identical amounts across months. Common patterns include ".COM", "APPLE.COM/BILL", "RECURRING", "SUBSCRIPTION", "PREMIUM", "PLUS", "PRO", "CLOUD", "HOSTING" in the description.

**Cloud services specific:** Any transaction containing "CLOUD", "HOSTING", "SERVER", "INFRASTRUCTURE" should be categorized here, NOT as Transport. Examples:
- "ALIBABA CLOUD" → Subscriptions (NOT Transport)
- "ANYCLOUD" → Subscriptions
- "CLOUD SERVICES" → Subscriptions
- "PROTON" (ProtonVPN/ProtonMail) → Subscriptions
- "NANONOBLE" → Subscriptions (software/SaaS)

### Health

- Pharmacies: Kimia Farma, Century, Guardian, Watsons, K-24, Apotek
- Clinics/hospitals: Siloam, RS (Rumah Sakit), Klinik, Prodia, BioMedika, Halodoc
- Fitness (one-time): gym day passes, sports equipment
- Supplements/wellness: "Vitamin", "Supplement", "Wellness"

### Bills & Utilities

- Electricity: PLN, "Listrik", "Token Listrik"
- Water: PDAM, "Air"
- Internet/telecom: IndiHome, Biznet, First Media, Telkomsel, XL, Indosat, Smartfren
- Insurance: AIA, Prudential, Manulife, Allianz, Asuransi, BCA Life
- Phone bills: "Pulsa", "Paket Data"
- Rent/housing: Rukita

### Other

Anything that does not clearly fit the above categories. Use sparingly — prefer a specific category when there's reasonable evidence. Only use "Other" for genuinely ambiguous entries like:
- Government fees/taxes
- ATM/bank fees
- Charity/donations
- Gifts
- One-off services that don't fit elsewhere

## Special Cases

### Installments

**CRITICAL**: Installment transactions should be categorized based on the MERCHANT, not as "Other".

The `installment_info` field (e.g., "5/12", "Final Settlement", "Cicilan") indicates payment status but does NOT determine category.

**Examples:**
- "CICILAN BCA SMARTPHONE" → Shopping (electronics installment)
- "CICILAN MATAHARI" → Shopping (department store installment)
- "CICILAN ELEKTRONIK" → Shopping (electronics)
- "INSTALLMENT APPLE" → Shopping
- "CICILAN HOTEL" → Other (travel/accommodation doesn't fit main categories)
- "ANGSURAN TOKOPEDIA" → Shopping (e-commerce)

**Rule:** Look at the merchant name in the description. If it's a store/retailer → Shopping. If it's unclear, use context clues.

## Common Miscategorizations to Avoid

| Transaction Pattern | WRONG Category | CORRECT Category |
|---------------------|----------------|------------------|
| "ALIBABA CLOUD" | Transport | Subscriptions |
| "ANYCLOUD" | Transport | Subscriptions |
| "PROTON" (ProtonVPN/Mail) | Transport | Subscriptions |
| "NANONOBLE" | Transport | Subscriptions |
| "CLOUD.*HOSTING" | Transport | Subscriptions |
| "CICILAN.*" (installments) | Other | Depends on merchant (usually Shopping) |
| "GRAB*FOOD" | Transport | Food & Drinks (Social) |
| "APPLE.COM/BILL" | Shopping | Subscriptions (if app subscription) |
| "GOOGLE *STORE" | Shopping | Subscriptions (if Google One, etc.) |

## Ambiguity rules

1. **When uncertain between two categories**, prefer the more specific one over "Other"
2. **When a merchant spans categories** (e.g., a supermarket that also has a cafe), categorize by the most likely purchase type based on the amount — small amounts at a supermarket are more likely groceries
3. **When the description is completely garbled**, check if any recognizable brand substring exists. If not, categorize as "Other"
4. **Amounts can provide signal**: very small amounts (<Rp 50,000) at ambiguous merchants lean toward food/transport; very large amounts lean toward shopping/bills
