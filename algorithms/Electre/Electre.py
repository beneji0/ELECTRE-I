
from ..prototypes import Solver
from .Concordance import ConcordanceMatrix
from .Discordance import DiscordanceMatrix


class ElectreSolver(Solver):

    # Solves a multi-criteria problem using the ELECTRE I method


    def solve(self) -> dict:
        # Calculates the result and returns it

        self.concordance_matrix = ConcordanceMatrix(self.data, self.poids)
        self.discordance_matrix = DiscordanceMatrix(self.data, self.poids)
        return self.get_result_matrix()


    def get_result_matrix(self):
        return list(x for x in self.concordance_matrix.result_matrix if x in self.concordance_matrix.result_matrix)

