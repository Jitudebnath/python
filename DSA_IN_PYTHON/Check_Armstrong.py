n = int(input("Enter a number:"))
num = n
total = 0
nod = len(str(n))
while num > 0:
    last_digit = num % 10
    total = total + (last_digit**nod)
    num = num // 10
if total == n:
    print("Armstrong Number")
else:
    print("Not a armstrong")
