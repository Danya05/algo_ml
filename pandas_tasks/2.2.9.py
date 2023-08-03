import pandas as pd


def transform(data):
    df = pd.DataFrame(data, columns=['code', 'stage', 'result'])
    df = df.astype({'code': 'int16', "result": 'float32'})
    return df


data1 = {'code': [1, 2, 3], 'stage': ['a', 'b', 'c'], 'result': [2.0, 2.1, 2.2]}

print(transform(data1))