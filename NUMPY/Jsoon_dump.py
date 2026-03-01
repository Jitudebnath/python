import json

data = {"name": "Jitu", "isprogrammer": "true", "Age": 27}

with open("NUMPY\data.json", "w") as f:
    json.dump(data, f)
