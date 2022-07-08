import csv

class Loader:

    # Loads the data from an csv file

    def __init__(self, path:str) -> None:
        self.path = path
        self.load()


    def get_data(self)->dict:
        return self.data


    def get_poids(self) -> dict:
        return self.poids


    def load(self):
        with open(self.path) as file:
            self.data = list(
                csv.DictReader(file)
            )
            self.data, self.poids, self.types = Formatter(self.data).get_attributes()
        

class Formatter:

    # Formats the data in the correct format

    def __init__(self, data:dict) -> None:
        self.data = data
        self.format()
        self.params_format()


    def convert_values(self, value):
        if(value in ['max', 'min']):
            return value
        return float(value)

    
    def format(self):
        self.data = dict((
            x['__algorithm_criteria_name__'], 
            dict(
                (key.strip(), self.convert_values(value.strip())) 
                for key, value in x.items() if key != '__algorithm_criteria_name__'
            )
        ) for x in self.data)


    def params_format(self):
        self.poids, self.data = PoidsFormatter(self.data).get_attributes()
        self.types, self.data = CriteriaTypeFormatter(self.data).get_attributes()


    def get_attributes(self):
        return self.data, self.poids, self.types


class PoidsFormatter:

    # Formats the poids parm correctly

    def __init__(self, data) -> None:
        self.data = data
        self.handle_empty_poids()
        self.poids = self.data['__algorithm_poids__']
        del self.data['__algorithm_poids__']    


    def handle_empty_poids(self):
        self.poids = {}
        if not '__algorithm_poids__' in self.data and len(self.data):
            self.data['__algorithm_poids__'] = dict((x, 1) for x,y in list(self.data.values())[0].items())

    
    def get_attributes(self):
        return self.poids, self.data


class CriteriaTypeFormatter:

    # Normalizes the criteria to minimise values for the electre algorithm

    def __init__(self, data) -> None:
        self.data = data
        self.handle_empty_criteria_type()
        self.types = self.data['__algorithm_criteria_type__']
        del self.data['__algorithm_criteria_type__']
        self.normalize_min_cols()

    
    def handle_empty_criteria_type(self):
        self.types = {}
        if not '__algorithm_criteria_type__' in self.data and len(self.data):
            self.data['__algorithm_criteria_type__'] = dict((x, 'max') for x,y in list(self.data.values())[0].items())


    def get_attributes(self):
        return self.types, self.data


    def normalize_min_cols(self):
        liste_max = [(x[0], self.get_max(x[0])) for x in self.types.items() if x[1] == "min"]

        for item in self.data.items():
            for criteria in liste_max:
                item[1][criteria[0]] = criteria[1] - item[1][criteria[0]]

    
    def get_max(self, criteria):
        return max(x[1][criteria] for x in self.data.items())
