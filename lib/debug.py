from ipdb import set_trace
from .author import Author
from .magazine import Magazine
from .article import Article

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
    set_trace()
