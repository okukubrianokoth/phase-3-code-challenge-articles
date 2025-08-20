# Phase 3 Code Challenge: Articles

This is the **Phase 3 Code Challenge** project for the Magazine domain.  

We are modeling relationships between **Author**, **Article**, and **Magazine**:

- An **Author** has many Articles.  
- A **Magazine** has many Articles.  
- An **Article** belongs to both an Author and a Magazine.  

---

## 🗂 Project Structure

---

## ⚙️ Setup & Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/okukubrianokoth/phase-3-code-challenge-articles.git
   cd phase-3-code-challenge-articles
python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
pip install pytest
pytest -v
tests/article_test.py::test_article_belongs_to_author_and_magazine PASSED
tests/author_test.py::test_author_has_name PASSED
tests/author_test.py::test_author_can_write_articles PASSED
tests/magazine_test.py::test_magazine_has_name_and_category PASSED

##Author
Okuku
tests/magazine_test.py::test_magazine_can_have_articles PASSED
