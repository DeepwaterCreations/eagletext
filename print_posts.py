#!/usr/bin/env python3

"""Print a list of long strings in a pleasing manner"""

import sys

from scrape_text import get_author_posts_from_all_pages


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: {} thread-id".format(sys.argv[0]))

    threadid = sys.argv[1]
    posts = get_author_posts_from_all_pages(threadid)

    print(posts)
