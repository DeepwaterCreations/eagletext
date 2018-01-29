#!/usr/bin/env python3

"""Print a list of long strings in a pleasing manner"""

import sys

from scrape_text import get_author_posts_from_all_pages

def print_posts_to_console(posts):
    """Output posts to console separated by lines for easy reading with
    your favorite paginator
    """
    for post in posts:
        for line in post:
            print(line)
        print()
        print("=====+++=====")
        print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: {} thread-id".format(sys.argv[0]))

    threadid = sys.argv[1]
    posts = get_author_posts_from_all_pages(threadid)

    print_posts_to_console(posts)
