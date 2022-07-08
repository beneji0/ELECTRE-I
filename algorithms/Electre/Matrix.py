

class ElectreMatrix:
    # Class to inherit from to create the electre matrixs

    def __init__(self, data, poids, coeff) -> None:
        self.data = data
        self.poids = poids
        self.coeff = coeff


    def get_coeff_domination_condition(self, column): pass


    def init_result_matrix(self):
        # Inits the matrixes that contains 
        # lists of elements dominating other ones

        self.result_matrix = []
        for line in self.coeffs_matrix.items():
            for column in line[1].items():
                if self.get_coeff_domination_condition(column):
                    self.result_matrix.append([line[0], column[0]])


    def get_coeffs_matrix(self):
        return self.coeffs_matrix