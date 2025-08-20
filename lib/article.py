class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    def __repr__(self):
        return f"<Article '{self.title}' by {self.author.name} in {self.magazine.name}>"
