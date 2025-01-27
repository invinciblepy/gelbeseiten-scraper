# 🟡 GelbeSeiten Scraper Germany 🇩🇪

Scrape business listings from [GelbeSeiten.de](https://www.gelbeseiten.de) — the official Yellow Pages of Germany. This open-source Python scraper allows you to extract B2B contact information by keyword and location.

**Get German business data fast — ideal for freelancers, lead generators, market researchers, and data engineers.**

---

## 🔍 Features

- ✅ Search by business type and city (e.g. `"Zahnarzt", "Berlin"`)
- ✅ Extract:
  - Business Name
  - Address
  - Phone Number
  - Fax (if listed)
  - Website URL
  - Email (if listed)
  - Address
- ✅ Handles pagination
- ✅ Export results to CSV
- ✅ Built with `requests` and `BeautifulSoup`
- ✅ Easily extendable for more fields or automation

---

## 🚀 Getting Started

### 1. Clone this repo
```bash
git clone https://github.com/invinciblepy/gelbeseiten-scraper-germany.git
cd gelbeseiten-scraper
pip install -r requirements.txt
python main.py -k apotheken -l berlin
```

All scraped data will be saved to the `output` directory located in the project’s base folder.  
An example output file is included for reference.
