"""file type check from user input"""


def check_file(filename:str):
    if filename.endswith(".pdf") or filename.endswith("..docx") or filename.endswith(".txt"):
        return"Valid file"
    else:
        return"Invalid file"

filename=input("Enter your file type :")
print(check_file(filename))        