import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.author import Author
from lib.article import Article
from lib.magazine import Magazine



import pytest
from lib.author import Author
from lib.article import Article
from lib.magazine import Magazine

def test_article_belongs_to_author_and_magazine():
    author = Author("Brian")
    mag = Magazine("Daily News", "News")
    article = Article(author, mag, "Breaking News")
    assert article.author == author
    assert article.magazine == mag
    assert article.title == "Breaking News"
