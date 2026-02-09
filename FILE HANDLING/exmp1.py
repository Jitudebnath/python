file_name = input("Enter a file name(with out extension):")
file_name = file_name + ".txt"
with open(file_name, "w") as f:
    while True:
        sentence = input("Enter a sentence =")
        if sentence == "end" or sentence == "finish":
            break
        f.write(sentence)
        f.write("\n")
