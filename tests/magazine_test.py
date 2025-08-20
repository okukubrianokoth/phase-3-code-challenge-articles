import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.author import Author
from lib.article import Article
from lib.magazine import Magazine


import pytest
from lib.author import Author
from lib.article import Article
from lib.magazine import Magazine

def test_magazine_has_name_and_category():
    mag = Magazine("Tech Weekly", "Technology")
    assert mag.name == "Tech Weekly"
    assert mag.category == "Technology"

def test_magazine_can_have_articles():
    author = Author("Brian")
    mag = Magazine("Health Journal", "Health")
    article = author.add_article(mag, "Wellness Tips")
    assert article in mag.articles()
