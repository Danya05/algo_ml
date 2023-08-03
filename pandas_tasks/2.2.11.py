import pandas as pd


def yummy_cakes(data, select):
    df = pd.DataFrame(data, columns=['cake_name', 'weight_in_gramm', 'price_in_rubles'])
    df.index += 1
    select = list(map(lambda x: x - 1, select))
    df = df.astype({'cake_name': 'str',
                    'weight_in_gramm': 'int',
                    'price_in_rubles': 'int'})
    df = df.iloc[select]
    return df


data1 = [["Napoleon", 900, 1250],
         ['RedVelvet', 1200, 1400],
         ['HoneyCake', 1300, 1300],
         ['Aida', 1000, 1000]]
select = [2, 1, 3]

print(yummy_cakes(data1, select))
