import json

with open("NUMPY\data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)
    print(type(py_obj))
