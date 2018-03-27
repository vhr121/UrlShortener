# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from urllib.parse import urlparse

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse



from Shortener.views import worker

# Model tests
# Form tests
# View tests

def test_worker_shortens_url_with_google():
    url = "http://7bna.net/wallpapers/cat-pictures.html"
    host = "Google"

    shortened_url = worker(url, host)

    assert url_validator(shortened_url)
    assert len(shortened_url) < len(url)

def test_worker_shortens_url_with_bitly():
    url = "http://7bna.net/wallpapers/cat-pictures.html"
    host = "Bitly"

    shortened_url = worker(url, host)

    assert url_validator(shortened_url)
    assert len(shortened_url) < len(url)

def test_worker_shortens_url_with_madwire():
    url = "http://7bna.net/wallpapers/cat-pictures.html"
    host = "Madwire"

    shortened_url = worker(url, host)

    assert url_validator(shortened_url)
    assert len(shortened_url) < len(url)


def url_validator(url):
    try:
        result = urlparse(url)
        return True if [result.scheme, result.netloc, result.path] else False
    except:
        return False
