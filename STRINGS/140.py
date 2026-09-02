"""Take a sentence as input . Split it into words ad print how many numbers start with a vowel"""

def count_vowel_words(sentence:str):
    vowels = "aeiouAEIOU"
    count = 0
    words = sentence.split()
    for word in words:
        if word[0] in vowels:
            count+=1
    return count

sentence = input("Enter a sentence : ")
print(count_vowel_words(sentence))            