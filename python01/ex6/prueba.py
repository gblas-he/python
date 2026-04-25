class Plant:
    @classmethod
    def anonima(cls):
        return cls("Unknown plant", 0, 0)
    
p = Plant.anonima()
print(p.show())