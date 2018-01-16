#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "http://eagle-time.com/showthread.php?tid=1223"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")

    author_name = soup.find(class_="username").string
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
