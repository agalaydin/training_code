import json

# JSON string:
data_JSON = '{ "name": "John", "age": 23, "major": "Physics" }'

# JSON to Python Object (it becomes a dictionary)
data = json.loads(data_JSON)

# Use the data dict like any other dict in Python:
print(data["major"])


