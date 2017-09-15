Data-Con-Scrape
===============

## These are the companion materials for my python webscraping workshop from [Boston Data-Con 2014](http://data-con.org/schedule/), an excellent conference that was put on by the good people of the [Boston Data Community](https://twitter.com/bostondatacomm). 

The session was advertised as: "A tutorial on python for web scraping, covering BeautifulSoup, and when and how to use Selenium for dynamic pages and comment loading." What *actually* happened was a lively workshop with great questions, interactive bloopers, and very very little Selenium. Thank you to everyone who stayed to the very end to scrape some data with me. Here are the materials and some extras. ~Enjoy

(video of the session is posted [here](https://www.youtube.com/watch?v=oOr1dlC4-Kc))

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">It&#39;s like trespassing and organizing your desk. <a href="https://twitter.com/laurieskelly">@laurieskelly</a> explains joy of web scraping. <a href="https://twitter.com/hashtag/bdc14?src=hash">#bdc14</a> <a href="https://twitter.com/hashtag/python?src=hash">#python</a> Scrape <a href="http://t.co/CRfkv5sGgk">http://t.co/CRfkv5sGgk</a></p>&mdash; Mike Combs (@mike3d0g) <a href="https://twitter.com/mike3d0g/status/511247516202201088">September 14, 2014</a></blockquote>




##Contents: 

**For all notebooks:**
* Links here in the README will take you to the published/non-interactive version of the notebooks. 
* Clone this repo and run .ipynb files using [ipython notebook][6] to play with them interactively.

###[/][15]
*  [Data-Con_Scrape.ipynb][4]: Scraping a "[faces sheet][19]" of the speakers from the conference using data we scrape from the [conference website][5]. 

###[/metacritic][16]
* [Data-Con-metacritic.ipynb][7]: Scraping the site metacritic.com to get information about new releases and produce links to visit and get detailed info on each one

* [Data-Con-metacritic2.ipynb][8]: Digging into details on the movie links created in the first metacritic scraper

###[/selenium][17]
* [Data-Con_Selenium.ipynb][9]: Tried to find more cool examples for Selenium, ended up finding another workaround and getting totally distracted making a scraper for datatau

###[/datatau_scraper][18]
* [Data-Con_tauscraper.ipynb][10]: Said distraction, which turned out pretty cool. 

------

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

* XPATH selector resources
  - [w3schools][12] reference
  - [oldschool-looking and awesome][13] tutorial 

* And a [helper][14] for CSS selectors

### What did I forget? 
remind [me on twitter][11] or make a pull request : ) 


[1]: http://selenium-python.readthedocs.org/en/latest/
[2]: http://selenium-python.readthedocs.org/en/latest/waits.html
[3]: https://docs.python.org/2/library/urlparse.html
[4]: http://nbviewer.ipython.org/github/laurieskelly/Data-Con-Scrape/blob/master/Data-Con_Scrape.ipynb
[5]: http://data-con.org/
[6]: http://ipython.org/notebook.html
[7]: http://nbviewer.ipython.org/github/laurieskelly/Data-Con-Scrape/blob/master/metacritic/Data-Con_metacritic.ipynb
[8]: http://nbviewer.ipython.org/github/laurieskelly/Data-Con-Scrape/blob/master/metacritic/Data-Con_metacritic2.ipynb
[9]: http://nbviewer.ipython.org/github/laurieskelly/Data-Con-Scrape/blob/master/selenium/Data-Con_Selenium.ipynb
[10]: http://nbviewer.ipython.org/github/laurieskelly/Data-Con-Scrape/blob/master/datatau_scraper/Data-Con_tauscraper.ipynb
[11]: https://twitter.com/laurieskelly
[12]: http://www.w3schools.com/xpath/xpath_syntax.asp
[13]: http://zvon.org/xxl/XPathTutorial/Output/example1.html
[14]: http://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048
[15]: https://github.com/laurieskelly/Data-Con-Scrape 
[16]: https://github.com/laurieskelly/Data-Con-Scrape/tree/master/metacritic
[17]: https://github.com/laurieskelly/Data-Con-Scrape/tree/master/selenium
[18]: https://github.com/laurieskelly/Data-Con-Scrape/tree/master/datatau_scraper
[19]: https://github.com/laurieskelly/Data-Con-Scrape/blob/master/facesheet.md
