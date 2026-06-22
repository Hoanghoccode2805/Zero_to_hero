import math
# Ex1: 
class Miniscaler:
    def __init__ (self):
        self.mean = None
        self.std = None

    def fit(self,data):
        self.mean = sum(data) / len(data)
        variance = sum((x - self.mean) ** 2 for x in data) / len(data)
        self.std = math.sqrt(variance)
        print(f"La moyenne des données est {self.mean:.2f}")
        print(f"Écart-type des données est {self.std:.2f}")
        return self.mean, self.std
    
    def transform(self,data):
        if self.std == 0:
            return [0.0 for _ in data]
        new_data = [((x - self.mean)/self.mean) for x in data]
        return new_data

my_data = [1, 2, 3, 4, 5]
scaler = Miniscaler()
scaler.fit(my_data)
print(f'Liste apres tranformation : {scaler.transform(my_data)}')