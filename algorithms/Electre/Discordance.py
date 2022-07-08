
from .Matrix import ElectreMatrix


class DiscordanceMatrix(ElectreMatrix):

    # Creates the discordance matrix used in the Electre algorithm

    def __init__(self, data, poids, coeff=0.3) -> None:
        super().__init__(data, poids, coeff)

        self.init_delta()
        self.init_discordance_matrix()
        self.init_result_matrix()


    def init_delta(self):
        # Calculates the delta factor of the discordance matrix

        maximum = max(max(x.values()) for x in self.data.values())
        minimum = min(min(x.values()) for x in self.data.values())
        self.delta = maximum - minimum


    def get_coeff_domination_condition(self, column):
        return column[1] <= self.coeff


    def init_discordance_matrix(self):
        self.coeffs_matrix = dict(
            (line[0], dict(
                (
                    column[0], 
                    get_dominated_comparison_value(line, column, self.delta)
                ) 
                for column in self.data.items() if(line != column)

            )) for line in self.data.items()
        )


def get_dominated_comparison_value(line, column, delta):
    # Returns for a specific element the criterias
    # where he dominates other elements 

    list_of_differences = [(column[1][x] - line[1][x]) for x in line[1].keys() if (line[1][x] < column[1][x])]
    
    if(not list_of_differences): return 0
    
    return (1/delta) * max(list_of_differences)