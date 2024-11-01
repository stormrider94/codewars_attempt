class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

class God:
    def __init__(self):
        self.creation()
    
    def creation(self):
        self.humans = [Man("Adam"), Woman("Eve")]
    
    def __getitem__(self, index):
        return self.humans[index]
    
    def __len__(self):
        return len(self.humans)