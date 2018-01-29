#! /usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

eagletime_url = "http://eagle-time.com"
thread_url_suffix = "showthread.php?tid="

def get_author_name(soup):
    """Return the name of the thread's author"""
    return soup.find(class_="username").string

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: {} thread-id".format(sys.argv[0]))

    threadid = sys.argv[1]
    url = eagletime_url + "/" + thread_url_suffix + threadid

    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")

    author_name = get_author_name(soup)
    def author_filter(tag):
        return tag.has_attr('class') and "username" in tag['class'] and tag.string == author_name
    author_labels = soup.find_all(author_filter)
    post_string_gens = [label.find_next(class_="post_body").stripped_strings for label in author_labels]
    posts = []
    for string_gen in post_string_gens:
        post = ""
        for s in string_gen:
            post += " " + s
        posts.append(post)

    print(posts)
