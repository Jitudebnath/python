"""Acessing the items using python programing in dictionary"""

marks={
    "science":98,
    "mathematics":99,
    "computer":99,
    "hindi":90,
    "history":71,
}

#print(marks.items())

#for i in marks.items():
    #print(i)

# for detail in marks.items():
#     sub=detail[0]
#     mark=detail[1]
#     print(sub,mark)   

for sub,mark in marks.items():
    print(sub,mark)