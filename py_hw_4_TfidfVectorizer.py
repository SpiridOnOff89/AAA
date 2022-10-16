from math import log
from typing import List


class CountVectorizer:
    """
    Конвертирует список текстовых строк в числовой двумерный массив
    """

    def __init__(self, lowercase=True):
        self.lowercase = lowercase
        self.features = []

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Создает список слов, встречающихся в тексте (self.features).
        Возвращает двумерный массив, в котором для каждой строки
        создается вложенный числовой массив. Элементы вложенных массивов
        отражают количество вхождения каждого уникального слова в строку.
        """

        corpus = [string.lower().split() if self.lowercase else string.split() for string in corpus]

        for string in corpus:
            for word in string:
                if word not in self.features:
                    self.features.append(word)

        matrix = [[0 for i in range(len(self.features))] for j in range(len(corpus))]

        for i in range(len(corpus)):
            for j in range(len(self.features)):
                for k in range(len(corpus[i])):
                    if corpus[i][k] == self.features[j]:
                        matrix[i][j] += 1

        return matrix

    def get_feature_names(self) -> List[str]:
        return self.features


class TfidfTransformer():
    def tf_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        """makes a term frequency matrix"""

        sums = map(sum, count_matrix)
        tf_matrix = [[round(num / sum, 3) for num in vector] for vector, sum in zip(count_matrix, sums)]

        return tf_matrix

    def idf_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        """makes a inverse document-frequency matrix"""

        docs_total = len(count_matrix)
        tf_matrix_by_words = list(map(list, zip(*count_matrix)))
        tf_matrix_by_docs = [sum(map(lambda x: bool(x), word)) for word in tf_matrix_by_words]
        idf_matrix = [round(log((docs_total + 1) / (num + 1)) + 1, 3) for num in tf_matrix_by_docs]

        return idf_matrix

    def fit_transform(cls, count_matrix: List[List[int]]) -> List[List[float]]:
        """makes a tf-idf matrix"""

        tf_matrix = cls.tf_transform(count_matrix)
        idf_matrix = cls.idf_transform(count_matrix)
        tfidf_matrix = [[round(tf * idf, 3) for tf, idf in zip(tf_matrix[i], idf_matrix)]
                        for i in range(len(tf_matrix))]

        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tf_idf = TfidfTransformer()

    def fit_transform(self, corpus: List[str]) -> List[List[float]]:
        """makes a tf-idf matrix from the text corpus"""
        count_matrix = super().fit_transform(corpus)
        return self.tf_idf.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())
