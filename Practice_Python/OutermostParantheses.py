"""Remove the outermmost parantheses"""

def remove_outer_parentheses(s):
    result = ""
    count = 0
    for ch in s:
        if ch == "(":
            if count > 0:
                result += ch
            count += 1
        elif ch == ")":
            count -= 1
            if count > 0:
                result += ch
        else:
            result += ch
    return result


s = input("Enter a string with parentheses: ")
print(remove_outer_parentheses(s))
