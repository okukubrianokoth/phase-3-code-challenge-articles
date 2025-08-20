from .author import Author
from .magazine import Magazine

class Article:
    _all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("author must be Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title.strip()) <= 50):
            raise Exception("title must be string 5–50 chars")

        self._author = author
        self._magazine = magazine
        self._title = title.strip()
        Article._all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("magazine must be Magazine instance")
        self._magazine = value

    @classmethod
    def all(cls):
        return cls._all
