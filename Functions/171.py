"""Write a function that takes a string and prints the frequency of
each character in the string."""


def charCount(string):
    my_dict = dict()
    for ch in string:
        if ch not in my_dict:
            my_dict[ch] = 1
        else:
            my_dict[ch] += 1

    for k, v in my_dict.items():
        print(f"{k} occurs {v}times")


charCount("HELLO")
