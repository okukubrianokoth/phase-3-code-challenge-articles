class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        from .article import Article
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})
