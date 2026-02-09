try:
    my_list = [2, 3, 4, 5, 6, 7]
    # print(my_list[76])
    # print(my_list[0] / my_list[-1])
    my_list = my_list * "abc"
except IndexError:
    print("Invaid index")
except ZeroDivisionError:
    print("You cant divide by zero")
except:
    print("Some error occured")
finally:
    print("This is a finally clause")
