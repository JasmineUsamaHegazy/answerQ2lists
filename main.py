sample_dict = {"name": "Kelly",
                "age": 25,
                "salary": 8000,
                "city": "New york"}

keys = ["name", "salary"]

for item in keys:
    sample_dict.pop(item)

print(sample_dict)

