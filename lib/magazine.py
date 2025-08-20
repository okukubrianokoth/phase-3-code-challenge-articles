from collections import Counter

class Magazine:
    _all = []

    def __init__(self, name, category):
        # use property setters to validate
        self.name = name
        self.category = category
        Magazine._all.append(self)

    def __repr__(self):
        return f"<Magazine {self._name!r} ({self._category!r})>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value.strip()) <= 16):
            raise Exception("Name must be a string 2–16 chars long.")
        self._name = value.strip()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = value.strip()

    def articles(self):
        # delayed import
        from .article import Article
        return [a for a in Article.all() if a.magazine is self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        arts = self.articles()
        return [a.title for a in arts] if arts else None

    def contributing_authors(self):
        arts = self.articles()
        if not arts:
            return None
        counts = Counter(a.author for a in arts)
        top = [auth for auth, n in counts.items() if n > 2]
        return top if top else None

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def top_publisher(cls):
        from .article import Article
        if not Article.all():
            return None
        counts = Counter(a.magazine for a in Article.all())
        # return the magazine instance with most articles
        top_mag, _ = counts.most_common(1)[0]
        return top_mag
