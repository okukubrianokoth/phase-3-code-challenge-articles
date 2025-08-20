import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.author import Author
from lib.article import Article
from lib.magazine import Magazine


import pytest
from lib.author import Author
from lib.article import Article
from lib.magazine import Magazine

def test_author_has_name():
    author = Author("Brian")
    assert author.name == "Brian"

def test_author_can_write_articles():
    author = Author("Brian")
    mag = Magazine("Tech Times", "Technology")
    article = author.add_article(mag, "AI in 2025")
    assert isinstance(article, Article)
    assert article in author.articles()
