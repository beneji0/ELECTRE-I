
from algorithms.Electre.Electre import ElectreSolver
from tools.Loader import Loader

loader = Loader("assets/analyse.csv")

settings = {
    "algorithm": ElectreSolver,
    "data": loader.get_data(),
    "poids": loader.get_poids()
}


class Solution:

    def get():
        return settings["algorithm"](
            settings["data"],
            settings["poids"]
        ).solve()