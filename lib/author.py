class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        from .article import Article
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        from .article import Article
        return Article(self, magazine, title)   # create & return new Article
