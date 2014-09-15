Data-Con-Scrape
===============

##Tips

* If possible for your data collecting project, use an API instead of scraping. It is kinder to the nice people creating the data that you are collecting, more resistant to breaking, and usually more efficient to code. Scraping is "for" cases when APIs are not provided. 

* If possible for your web scraping project, avoid using Selenium. It is more complex to develop scraper code using Selenium, and slower to run. If you can get what you need without Selenium, it is usually better. 

* When you're poking through a website to scrape it, it's a great idea to open the page in *Incognito Mode* so that your active sessions, plug-ins, etc, do not make the content that you see differ systematically from the content "seen" by Requests. 

* Websites change. When they do scrapers typically break. There are ways to write your selectors or build your scraping logic to be robust to minor changes, but broken scrapers are part of the game. You can't go around them, you can't go under them, so to live through them: 
  - Make your code noisy. Include tests and checks that can detect changes, and notify yourself when something changes. 
  - Save raw html. "Space is cheap," as they say, so saving raw html can allow you retroactively patch the  holes in your longitudinal scraping data after you hvae adjusted to a change in page format.
  - For this reason, ugly sites make great scraping targets. If a page looks like it hasn't been updated since 1998, you might infer that it is less likely to be re-styled and re-structured every 3-6 months. 


##Resources

* Selenium [docs][1]
  - I think that [Waits][2] are the trickiest part of using Selenium. 



[1](http://selenium-python.readthedocs.org/en/latest/)
[2](http://selenium-python.readthedocs.org/en/latest/waits.html)