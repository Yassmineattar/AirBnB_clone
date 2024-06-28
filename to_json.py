import json


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'])


# Serialize
obj = MyClass("Alice", 30)
obj_dict = obj.to_dict()
json_str = json.dumps(obj_dict)

# Deserialize
data = json.loads(json_str)
new_obj = MyClass.from_dict(data)
