"""make a function which return min and max"""

def min_max(lst):
    #logic 
    mini=min(lst)
    maxi=max(lst)
    return mini,maxi


ans1,ans2 = min_max([1,2,3,4,5,6,7,8,9])
print(f"minimum number is {ans1}")
print(f"maximum number is {ans2}")