def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")


Ammount = int(input("Please enter your ammount:"))
converter(Ammount)
