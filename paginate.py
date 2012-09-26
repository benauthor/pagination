from __future__ import division
from math import ceil

class OutOfRange(Exception):
    pass

def paginate(text, page, chars_per_page):
    """ Paginate chunks of text """
    if chars_per_page > len(text):
        total = 1
        result = text
    else:
        foo = (page - 1) * chars_per_page
        bar = page * chars_per_page
        total = int(ceil(len(text) / chars_per_page))
        result = text[foo:bar]

    if page > total:
        raise OutOfRange
    else:
        return total, result

def wordpaginate(text, page, chars_per_page):
    """ Paginate, ending on spaces """
    # can do same with list of chunks of html
    if chars_per_page > len(text):
        total = 1
        result = text
    else:
        total = 0
        result = ''
        chunks = text.split()
        chunks.reverse()
        while chunks:
            total += 1
            a_page = ''
            while len(a_page) < chars_per_page:
                a_page += chunks.pop()
            if total == page:
                result = a_page

    if page > total:
        raise OutOfRange
    else:
        return total, result
