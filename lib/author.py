class Author:
    def __init__(self, name: str):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Name must be a non-empty string.")
        self._name = name.strip()

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"<Author {self._name!r}>"

    def articles(self):
        # delayed import to avoid circular import
        from .article import Article
        return [a for a in Article.all() if a.author is self]

    def magazines(self):
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        # delayed import to avoid circular import
        from .article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        cats = {m.category for m in mags}
        return list(cats)
