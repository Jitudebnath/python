"""Top 3 subjects with higest marks"""

subjects={
    "science":98,
    "mathematics":99,
    "computer":99,
    "hindi":90,
    "history":71,
}
ans = sorted(subjects.items(),key=lambda x:x[1],reverse=True)
result=ans[0:3]
for sub,mark in result:
    print(f"sub={sub},marks={mark}")