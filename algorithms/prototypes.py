
from abc import ABC, abstractmethod


class Solver(ABC):
    # Inherit from this class to create your custom solvers

    def __init__(self, data:dict, poids:dict) -> None:
        super().__init__()
        
        self.data = data
        self.poids = Poids(poids).get_poids()


    @abstractmethod
    def solve(self) -> list: pass


class Poids():
    # Normalizes poids and returns the new dict

    def __init__(self, poids:dict) -> None:
        self.original_poids = poids
        self.normalize_poids()


    def normalize_poids(self):
        somme_poids = sum(self.original_poids.values())
        self.poids = dict(
            (item[0], item[1]/somme_poids) 
            for item in self.original_poids.items()
        )

    
    def get_criteria_poids(self, criteria) -> dict:
        # Given the criteria name, 
        # gives the criteria poids without raising an error if the item doesn't exist
        if criteria in self.poids: self.poids[criteria] = 1
        return self.poids[criteria]


    def get_poids(self):
        return self.poids