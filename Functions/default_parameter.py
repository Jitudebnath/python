# Default Parameters in python
def total_marks(physics=0, maths=0, science=0, english=0, hindi=0):
    print(f"your marks in physics={physics}")
    print(f"your marks in maths={maths}")
    print(f"your marks in science={science}")
    print(f"your marks in english={english}")
    print(f"your marks in hindi={hindi}")
    total = physics + maths + science + english + hindi
    print(f"your total marks={total}")


total_marks(maths=45, english=89)
