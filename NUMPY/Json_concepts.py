import json

py_obj = {"name": "Jitu", "isprogrammer": "true"}
json_str = json.dumps(py_obj)
print(type(json_str), json_str)
