import sys

import pandas as pd


columns = input().split(";")
data = {}
for input_str in sys.stdin:
    for j in range(len(columns)):
        input_str1 = input_str.rstrip().split(";")
        data.setdefault(columns[j], [])
        data[columns[j]].append(input_str1[j])
df = pd.DataFrame(data)
df = df.astype({'income': 'int64', 'tax': 'int64'})
df["income"] -= df["income"] * df["tax"] / 100
del df['tax']
print(df)
