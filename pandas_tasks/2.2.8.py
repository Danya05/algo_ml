import pandas as pd


def change_me(data, changes):
    df = pd.DataFrame(data)
    for i in changes:
        df.at[i[0], i[1]] = i[2]
    return df


data1 = {'col1': [1, 1, 1], 'col2': [2, 2, 2]}
changes1 = [[0, 'col1', 1000], [1, 'col2', 100000]]

change_me(data1, changes1)