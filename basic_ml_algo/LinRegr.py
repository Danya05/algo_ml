import pandas_tasks as pd


class MyLineReg:
    def __init__(self, n_iter=100, learning_rate=0.1):
        self.n_iter = n_iter
        self.learning_rate = learning_rate
        self.weights = []

    def __str__(self):
        return f"MyLineReg class: n_iter={self.n_iter}, learning_rate={self.learning_rate}"

    def __repr__(self):
        return f"MyLineReg class: n_iter={self.n_iter}, learning_rate={self.learning_rate}"

    def fit(self, X: pd.DataFrame, y: pd.Series, verbose=False):
        """
        :param X: все фичи в виде датафрейма пандаса.
        :param y: целевая переменная в виде пандасовской серии.
        :param verbose: указывает на какой итерации выводить лог. Например, значение 10 означает, что на каждой 10
        итерации градиентного спуска будет печататься лог. Значение по умолчанию: False (т.е. ничего не выводится).
        :return:
        """
        row_count = X.shape[0]
        column_count = X.shape[1]
        X.insert(0, "col_of_1", [1] * row_count)
        row_count += 1
        column_count += 1
        self.weights = [1] * row_count
        for i in range(self.n_iter):
            for j in range(row_count):
                prediction = sum([self.weights.at[i] * X.loc[j].at[i] for i in range(column_count)])
                print(prediction)


ml = MyLineReg(1, 0.1)
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
y = pd.Series([1, 1, 1])
ml.fit(df, y)
