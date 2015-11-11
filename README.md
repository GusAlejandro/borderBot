# borderBot
A Twitter Bot that uses a web scraper to tweet out wait times at the San Ysidro-Tijuana border.

This Twitter bot was written in python, using the BeautifulSoup library for the web scraping and the Tweepy library to interface with Twitter.  

The border crossing wait times are web scraped from the California Institute for Telecommunications and Information Technology at the University of California, San Diego. Afterwards, the string that results is clipped so only the wait time is left. Finally, the tweets are shown in the account <a href="https://twitter.com/SY_BORDER">@SY_Border</a> (currently offline). 
