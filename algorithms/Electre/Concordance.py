
from .Matrix import ElectreMatrix


class ConcordanceMatrix(ElectreMatrix):

    def __init__(self, data, poids, coeff=0.7) -> None:
        super().__init__(data, poids, coeff)

        self.init_dominance_matrix()
        self.init_concordance_matrix()
        self.init_result_matrix()


    def init_dominance_matrix(self):
        # Inits the dominance matrix

        self.dominance_matrix = dict(
            (line[0], dict(
                (
                    column[0], get_domination_comparison_line(line, column)
                ) for column in self.data.items() 
                if(line != column)

            )) for line in self.data.items()
        )


    def init_concordance_matrix(self):
        # Converts the dominance matrix to a coeffs matrix

        self.coeffs_matrix = dict((
            line[0], dict(
                (column[0], sum(self.poids[criteria] for criteria in column[1]))

            for column in line[1].items())

        ) for line in self.dominance_matrix.items())


    def get_coeff_domination_condition(self, column):
        return column[1] >= self.coeff

    
    def get_dominance_matrix(self):
        return self.dominance_matrix



def get_domination_comparison_line(line, column):
    # Returns for a specific element the criterias
    # where he dominates other elements 

    return [
        criteria[0] for criteria in column[1].items()
        if(criteria[1] <= line[1][criteria[0]])
    ]