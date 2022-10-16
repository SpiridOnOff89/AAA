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

if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(corpus))
    print(vectorizer.get_feature_names())