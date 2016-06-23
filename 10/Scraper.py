import requests
import time, datetime
import pandas as pd
from bs4 import BeautifulSoup

# Global variables
data = []
https = 'https:'
base_url = 'https://www.reddit.com'


# it seems the most important is in fact to avoid sending too many requests from the same IP address
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0'}
response = requests.get("https://www.reddit.com", headers)
doc = BeautifulSoup(response.text, 'html.parser')
if doc.find('title') == 'Too Many Requests':
    print('Reddit sent a “Too Many Requests” response.')


# Functions

def get_title(post_div):
    title = post.select('a.title')
    if len(title) > 0: # else: "it looks like you haven't subscribed..."
        return title[0].string
    else:
        return False

def get_votes(post_div):
    votes = post.select('div.unvoted div.unvoted')
    if len(votes) > 0:
        try:
            votes_nb = int(votes[0].string)
            return votes_nb
        except ValueError:
            return 'No vote';
    else:
        return False

def get_comments_nb(post_div):
    comments_list = post_div.select('ul.flat-list .first a')
    if len(comments_list) > 0:
        comment_str = comments_list[0]
        if comment_str.string == 'comment':
            return 0
        else:
            try:
                comments_nb = int(comment_str.string[0:-8])
                return comments_nb
            except ValueError:
                return False;
            else:
                return
    else:
        return False

def get_subreddit(post_div):
    subreddit = post_div.select('.tagline a.subreddit')
    if len(subreddit) > 0:
        return subreddit[0].string
    else:
        return False

def get_date(post_div):
    date = post_div.select('p.tagline time') #  att:title
    if len(date)>0:
        return date[0].get('title')
    else:
        return False

def get_url(post_div):
    url_list = post_div.select('a.title')
    if len(url_list) > 0: # else: "it looks like you haven't subscribed..."
        url = url_list[0].get("href")
        if url[0:4] == 'http': # absolute url
            return url
        else:
            return base_url + url
    else:
        return False

def get_thumbnail(post_div):
    img = post_div.select('a.thumbnail img')
    if len(img) > 0:
        return https + img[0].get('src')
    else:
        return '' # No thumbnail

posts = doc.select('div.sitetable div.thing')
print(len(posts), "posts found…")
for post in posts:
    # These are the columns we want to store in our CSV file:
    # title|votes|comments|parent|date|url|img
    title = get_title(post)
    if title:
        votes = get_votes(post)
        comments = get_comments_nb(post)
        subreddit = get_subreddit(post)
        date = get_date(post)
        url = get_url(post)
        thumbnail = get_thumbnail(post)

        dic = {'title': title, 'votes': votes, 'comments': comments, 'subreddit': subreddit, 'date': date, 'url': url, 'thumbnail': thumbnail}
        data.append(dic)

print(len(data), "posts scrapped.")
if len(data) < 1:
    data.append('The server denied the page request.')


# Saving the file

datestring = time.strftime("%Y-%m-%d")
filename = "reddit-" + datestring + ".csv"

posts_df = pd.DataFrame(data)
posts_df.to_csv(filename)
print("Data saved to", filename)
