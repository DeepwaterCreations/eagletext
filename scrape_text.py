#!/usr/bin/env python3

import sys

import requests
from bs4 import BeautifulSoup

eagletime_url = "http://eagle-time.com"

def get_author_posts_from_all_pages(threadid):
    """Return a list of post text written by the thread's author
    across all pages in the thread
    """
    author_name = None
    posts = []
    url = get_url_with_suffix(threadid)
    while True:
        html = requests.get(url).text
        soup = BeautifulSoup(html, "lxml")
        if author_name is None:
            author_name = get_author_name(soup)

        posts += get_author_posts(soup, author_name)

        next_button = soup.find(class_="pagination_next")
        if next_button is None:
            break
        else:
            url = eagletime_url + "/" + next_button['href']
    return posts

def get_url_with_suffix(threadid, pagenum=1):
    """Build and return an url for a given page of a thread on Eagle Time with the given thread id"""
    return eagletime_url + "/showthread.php?tid={0}&page={1}".format(threadid, pagenum)

def get_author_name(soup):
    """Return the name of the thread's author"""
    return soup.find(class_="username").string

def get_author_posts(soup, author_name):
    """Return a list of post text written by the given author"""
    def author_filter(tag):
        return tag.has_attr('class') and "username" in tag['class'] and tag.string == author_name
    author_labels = soup.find_all(author_filter)
    post_string_gens = [label.find_next(class_="post_body").stripped_strings for label in author_labels]
    posts = []
    for string_gen in post_string_gens:
        post = [s for s in string_gen]
        posts.append(post)
    return posts

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: {} thread-id".format(sys.argv[0]))

    threadid = sys.argv[1]
    posts = get_author_posts_from_all_pages(threadid)

    print(posts)
