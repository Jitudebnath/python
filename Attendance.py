class_held=int(input("Enter a class held:"))
class_attended=int(input("Enter a class attended:"))

class_percentage=(class_attended/class_held)*100

print(f"you are attending class percentage is {class_percentage:.2f}%")

if class_percentage>75:
    print("You are allowed for your upcomming exam")
else:
    print("You are not allowed for your upcomming exam")