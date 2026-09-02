"""iteration using python programming lagauge"""

my_tuple=(12,23,45,"Jitu","Debnath",99)

n=len(my_tuple)

for i in range(0,n):
    print(my_tuple[i],end=" ")


for index,value in enumerate(my_tuple):
    print(f"Index = {index} and value = {value}")