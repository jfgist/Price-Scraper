Amazon-Scraper
==============

Uses Beautiful Soup to scrape Amazon for current prices.

###Dependencies
* bs4 (included)
 
### Current State

This is currently in a very rough state.  The input and output file are both hardcoded and the only output is to the command line. 

### Planned Updates

* Set the ap to run at some specified interval
* Cache the current lowest price for each item and only email if that price has been beat
* Send email to user if price break happens
* Make the output and input files a little more dynamic (maybe an input)
