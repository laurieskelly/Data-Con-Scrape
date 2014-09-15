Data-Con-Scrape
===============

##Contents: 

*  [Data-Con_Scrape.ipynb][4]: Scraping a "faces sheet" of the speakers from the conference using data we scrape from the [conference website][5]. Clicking on the name here will take you to the published version of the notebook. Clone this repo and run it using [ipython notebook][6] to play with it interactively.

* [Data-Con-metacritic.ipynb][7]: Scraping the site metacritic.com to get information about new releases and produce links to visit and get detailed info on each one

* [Data-Con-metacritic2.ipynb][8]: Digging into details on the movie links created in the first metacritic scraper

* [Data-Con_Selenium.ipynb][9]: Tried to find more cool examples for Selenium, ended up finding another workaround and getting totally distracted making a scraper for datatau

* [Data-Con_tauscraper.ipynb][10]: Said distraction, which turned out pretty cool. 

##Web Scraping Tips

* If possible for your data collecting project, use an API instead of scraping. It is kinder to the nice people creating the data that you are collecting, more resistant to breaking, and usually more efficient to code. Scraping is "for" cases when APIs are not provided. 

* If possible for your web scraping project, avoid using Selenium. It is more complex to develop scraper code using Selenium, and slower to run. If you can get what you need without Selenium, it is usually better. 

* When you're poking through a website to scrape it, it's a great idea to open the page in *Incognito Mode* so that your active sessions, plug-ins, etc, do not make the content that you see differ systematically from the content "seen" by Requests. 

* Websites change. When they do scrapers typically break. There are ways to write your selectors or build your scraping logic to be robust to minor changes, but broken scrapers are part of the game. You can't go around them, you can't go under them, so to live through them: 
  1. Make your code noisy. Include tests and checks that can detect changes, and notify yourself when something changes. 
  2. Save raw html. "Space is cheap," as they say, so saving raw html can allow you retroactively patch the  holes in your longitudinal scraping data after you hvae adjusted to a change in page format.
  3. For this reason, ugly sites make great scraping targets. If a page looks like it hasn't been updated since 1998, you might infer that it is less likely to be re-styled and re-structured every 3-6 months. 


##Random Tips

* `urlparse.urljoin()` is a handy way to stick parts of a url together without messing it up and having too many or too few slashes up in there. [module docs][3]

##Resources

* Selenium [docs](1)
  - I think that [Waits][2] are the trickiest part of using Selenium. 







[1]: http://selenium-python.readthedocs.org/en/latest/
[2]: http://selenium-python.readthedocs.org/en/latest/waits.html
[3]: https://docs.python.org/2/library/urlparse.html
[4]: http://nbviewer.ipython.org/github/laurieskelly/Data-Con-Scrape/blob/master/Data-Con_Scrape.ipynb
[5]: http://data-con.org/
[6]: http://ipython.org/notebook.html
[7]: http://nbviewer.ipython.org/github/laurieskelly/Data-Con-Scrape/blob/master/Data-Con-metacritic.ipynb
[8]: http://nbviewer.ipython.org/github/laurieskelly/Data-Con-Scrape/blob/master/Data-Con_metacritic2.ipynb
[9]: http://nbviewer.ipython.org/github/laurieskelly/Data-Con-Scrape/blob/master/Data-Con_Selenium.ipynb
[10]: http://nbviewer.ipython.org/github/laurieskelly/Data-Con-Scrape/blob/master/Data-Con_tauscraper.ipynb