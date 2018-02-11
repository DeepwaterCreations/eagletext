#!/usr/bin/env python3

"""Print a list of long strings in a pleasing manner"""

import sys

from scrape_text import get_author_posts_from_all_pages

def parse_for_console_output(posts):
    """Build plaintext output from posts"""
    document = ""
    for post in posts:
        for line in post:
            document += (line)
        document += ('\n')
        document += ("=====+++=====")
        document += ('\n')
    return document

def parse_for_html_output(posts):
    """Build HTML output from posts"""
    document = ""
    for post in posts:
        for line in post:
            formatted_line = "<p>{}</p>".format(line)
            document += formatted_line
        document += "<hr />"
    return document

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: {} [thread-id]".format(sys.argv[0]))

    threadid = sys.argv[1]
    posts = get_author_posts_from_all_pages(threadid)

    print(parse_for_console_output(posts))
    # print(parse_for_html_output(posts))
