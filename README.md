# top40

Overview:
This project tracks popular music via America's TOP 40 hits website.
There are 4 sub-modules that perform this.
"top40Scraper" goes to the at40.com site and grabs raw data on a weekly basis.
"top40Facade" is a higher level interface for the web scraping from top40Scraper. "top40db" takes data obtained from the earlier modules and writes it to a local database. "top40Analytics" performs interesting analytics on said database.

For tests, please see the Test folder.
Also, sqliteBrowser is an awesome tool that can be used to quickly check out what a sqlite db looks like.
For source code, please use the src folder.

Enjoy.
