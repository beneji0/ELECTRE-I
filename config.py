
from algorithms.Electre.Electre import ElectreSolver
from tools.Loader import Loader

loader = Loader("assets/analyse.csv")

settings = {
    # This is where all the configuration should go
    "algorithm": ElectreSolver,
    "data": loader.get_data(),
    "poids": loader.get_poids()
}


class Solution:

    # Returns the solution based on the settings dict

    def get():
        return settings["algorithm"](
            settings["data"],
            settings["poids"]
        ).solve()