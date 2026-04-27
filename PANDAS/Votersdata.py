"""use pandas print that weither that person can vote or not"""

import pandas as pd


# creating a voter data

data = {
    "Name": ["Rahul", "Mohit", "jitu", "kedar", "Nhar"],
    "Age": [12, 34, 23, 45, 10],
}
df = pd.DataFrame(data)

print("-----eligible voters-----")
eligible = df[df["Age"] >= 18]
print(eligible)

print("-----youngest voters-----")
print("Youngest:\n", df.loc[df["Age"].idxmin()])
print("-----oldest voters")
print("Oldest:\n", df.loc[df["Age"].idxmax()])
