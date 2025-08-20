class Magazine:
    _all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all.append(self)

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
        from .article import Article
        return [a for a in Article.all() if a.magazine is self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        arts = self.articles()
        return [a.title for a in arts] if arts else None

    def contributing_authors(self):
        from collections import Counter
        counts = Counter(a.author for a in self.articles())
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
        counts = {}
        for a in Article.all():
            counts[a.magazine] = counts.get(a.magazine, 0) + 1
        return max(counts, key=counts.get)
