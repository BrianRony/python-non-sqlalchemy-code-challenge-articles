class Article:
    _all = []

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def find_author_by_name(cls, name):
        for article in cls._all:
            if article.author.name == name:
                return article.author
        return None

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self._author.articles().append(self)
        self._magazine.articles().append(self)
        Article._all.append(self)  # Ensure each instance is added to _all

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        self._magazine = magazine

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        topic_areas = {article.magazine.category for article in self._articles}
        return list(topic_areas) if topic_areas else None
    
    
class Magazine:
    _all = []

    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def top_publisher(cls):
        if not cls._all:
            return None
        return max(cls._all, key=lambda magazine: len(magazine.articles()))

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        self._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    def articles(self):
        return self._articles

    def contributors(self):
        contributors_list = []
        for article in self._articles:
            if article.author not in contributors_list:
                contributors_list.append(article.author)
        return contributors_list

    def article_titles(self):
        titles = [article.title for article in self._articles]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None



