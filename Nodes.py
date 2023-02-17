class Node:
    def __init__(self, name, parents, cpt):
        self.name = name
        self.parents = parents
        self.cpt = cpt

    def watch_node_info(self):
        print(f'Name: {self.name}\nParents: {self.parents}\nCpt: {self.cpt}')

    def set_node(self, name, parents, cpt):
        self.name = name
        self.parents = parents
        self.cpt = cpt
