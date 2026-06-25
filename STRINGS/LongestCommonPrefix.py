"""Find the lonngest common prefix"""
def lcp(strs):
    result=''
    if len(strs) == 0:
        return ''
    base = strs[0]
    for i in range(0,len(base)):
        for word in strs[1:]:
            if i == len(word) or word[i] != base[i]:
                return result
        result += base[i]    
    return result        
strs = input("Enter strings using comma : ").split(',')
print("Here the longest common prefix is : ",lcp(strs))



    