# debug script: runnable as module (python -m lib.debug) or directly (python lib/debug.py)
try:
    # prefer package-style imports when run as module
    from .author import Author
    from .magazine import Magazine
    from .article import Article
except Exception:
    # fallback for direct execution
    from author import Author
    from magazine import Magazine
    from article import Article

def seed():
    a1 = Author("Brian")
    a2 = Author("Okuku")

    m1 = Magazine("Nation", "News")
    m2 = Magazine("Techie", "Tech")

    Article(a1, m1, "Kenya Politics Today")
    Article(a1, m2, "AI in Africa Now")
    Article(a2, m2, "Women in Tech")

    return a1, a2, m1, m2

if __name__ == "__main__":
    a1, a2, m1, m2 = seed()
    print("Seeded objects:")
    print("Authors:", a1, a2)
    print("Magazines:", m1, m2)
    print("Articles total:", len(Article.all()))
    print("a1 articles:", a1.articles())
    print("a1 magazines:", a1.magazines())
    print("a1 topic areas:", a1.topic_areas())
    print("m2 article titles:", m2.article_titles())
    print("m1 contributors:", m1.contributors())
    top = Magazine.top_publisher()
    print("Top publisher:", top)
