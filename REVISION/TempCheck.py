"""Check the temperature and print "cold","warm","hot","""

temp = float(input("Enter the temperature value:"))

if temp <= 0:
    print("It is cold water.")
elif temp > 0 and temp <= 99:
    print("It is warm water.")
else:
    print("It is hot water.")
