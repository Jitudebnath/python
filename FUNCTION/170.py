"""Write a  function that takes a list of numbers and prints the sum
and average of these numbers"""


def sum_avg_list(lst):
    total = 0
    for num in lst:
        total = total + num
    print(f"Total of all numbers={total}")
    avg = total / len(lst)
    print(f"Average of the list is {avg}")


sum_avg_list([1, 2, 3, 4000, 5])
