# Tuchuzy Scraper

Simple Scrapy app to extract products info:
<br>
<br>
Required fields:
  * Product Name
  * Brand 
  * Category
  * Image links 
  * Price
  * Sale Price

## Installation:

  1. Create virtual enviroment <p> `python3 -m venv directory`
  2. Activate it <p> `source directory/bin/active`
  3. Install requirements <p> `pip3 install -r requirements.txt`
  4. Run scraper <p> `scrapy crawl tuchuzy -o output.json`
  5. Enjoy!
    
To change the number of scraped items, change the `CLOSESPIDER_ITEMCOUNT` in `settings.py` and `LIMIT` in `pipelines.py` with desired number
