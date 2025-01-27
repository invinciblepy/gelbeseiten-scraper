import argparse
from gelbeseiten.scraper import GelbeSiten

def main():
    parser = argparse.ArgumentParser(description="Gelbe Seiten Scraper CLI")
    parser.add_argument('-k', '--keyword', required=True, help='Industry keyword (e.g. IT)')
    parser.add_argument('-l', '--location', required=True, help='Leads location (e.g. berlin)')
    
    args = parser.parse_args()
    
    scraper = GelbeSiten(keyword=args.keyword, location=args.location)
    scraper.scrape()

if __name__ == "__main__":
    main()
