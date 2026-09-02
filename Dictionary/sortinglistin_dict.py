marks={
    "akshy":[23,34,45,67,78],
    "kunal":[23,84,48,67,78],
    "dhiman":[43,34,49,67,78],
    "ankur":[23,64,45,97,78],
    "salman":[23,44,90,67,78],
}

ans = dict(sorted(marks.items(),key=lambda x:sum(x[1]),reverse=True))
print(ans)