import networkx as nx
import matplotlib.pyplot as plt


class DominationGraph:

    # Shows the result graph, given a list of domination values

    def __init__(self, solved_list:list) -> None:
        self.liste = solved_list
        self.graph = nx.DiGraph(self.liste)
        self.prepare_graph_dict()


    def prepare_graph_dict(self) -> dict:
        fig, ax = plt.subplots()
        nx.draw_networkx(self.graph, ax=ax)
        ax.set_title("Graphe final de résolution par méthode ELECTRE I")

    
    def show(self):
        plt.show()


