from core.legal.models.article import LegalArticle


def test_article_creation():

    article = LegalArticle(id=1, article_number="1", text="sample", legislation_id=10)

    assert article.article_number == "1"
