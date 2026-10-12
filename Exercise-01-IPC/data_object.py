class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def __repr__(self):
        return f"DataObject(name={self.name!r}, values={self.values!r})"
