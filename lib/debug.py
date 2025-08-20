from .author import Author
from .magazine import Magazine
from .article import Article

if __name__ == "__main__":
    author1 = Author("Brian")
    author2 = Author("Alice")

    mag1 = Magazine("Tech Daily", "Technology")
    mag2 = Magazine("Health Weekly", "Health")

    Article(author1, mag1, "AI in 2025")
    Article(author2, mag1, "Future of Robotics")
    Article(author1, mag2, "Wellness Hacks")

    print("Author1 Articles:", author1.articles())
    print("Mag1 Contributors:", mag1.contributors())
