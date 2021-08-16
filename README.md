# Web-Scrapper
A web scrapper to scrape academic data from the internet.

Usage:

A) To Scrape data from Research Gate Website
  1. Move into the PaperScrap\PaperScrap\spiders\ directory and open Quote_spider.py
  2. Change the start_url to your research paper url.
  3. Move back to PaperScrap\PaperScrap\
  4. Start Scrapy by command: scrapy crawl quotes  //quotes is the default spider name

B) To Scrape data from other Website
  1. Using Scrapy shell in directory PaperScrap\PaperScrap\
  2. Start Shell by command: scrapy shell "your_url"
