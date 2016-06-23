## Homework 10, “Scraping and Saving”

Very interesting homework!

Files for the assignment:
* Scraper.py = Reddit Part One: Getting Data
* Mailer.py = Reddit Part Two: Sending data
* crontab.txt = a copy of the server schedule

Other files:
* Homework-10-Ronga.ipynb = Jupyter Notebook version of both .py files
* reddit-2016-06-23.csv = sample data
* workaround.py = auto-call example

I had troubles with the “instability” of the reddit homepage.

I'm wondering what could be the best workaround to deal with reddit’s countermeasures. Maybe the script could call itself with a 5 minutes delay: `os.system("sleep 300; python3 Scraper.py;")` (See the workaround.py test script)
