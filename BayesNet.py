from Nodes import Node


class BayesianNetwork:
    def __init__(self):
        self.nodes = []

    def add_nodes(self, nodes):
        for i in nodes:
            self.nodes.append(i)

    def infer(self, query_node, observed):
        # TODO: implement inference algorithm
        pass

    # Checks if the first node is dependent of the second node
    def isDependent(self, node: Node, node2: Node):
        if node.cpt[0] == node2.cpt[0] or len(node2.cpt) == 1:
            return False
        else:
            return True

    # Returns a list of the results of inference given a node from its parents

    def get_parents_results(self, node_name):
        results = []
        node = Node('', [], ())
        single_parent = Node('', [], ())
        oneParent = False
        parents = []
        node_parents = []
        for i in self.nodes:
            if i.name == node_name:
                node = i
        if len(node.parents) == 0:
            raise ValueError('Node has no parents.')
        elif len(node.parents) == 1:
            oneParent = True
            for i in self.nodes:
                if i.name == node.parents[0]:
                    single_parent.set_node(i.name, i.parents, i.cpt)
        elif len(node.parents) > 1:
            parents = node.parents.copy()
            for nodi in self.nodes:
                if nodi.name in parents:
                    parents.remove(nodi.name)
                    parents.append(nodi)

        # Infer with one parent
        if oneParent:
            # P(A|B) = P(B|A)P(A) / P(B)
            # P(B) = P(B|A)P(A) + P(B|-A)P(-A)
            prob_child = (node.cpt[0][0]*single_parent.cpt[0]) + \
                (node.cpt[1][0]*single_parent.cpt[1])
            # P(-B)
            notprob_child = 1-prob_child

            # P(A|B) = P(B|A)P(A) / P(B)
            parent_given_child = (
                node.cpt[0][0]*single_parent.cpt[0])/prob_child
            # P(-A|B) = P(B|-A)P(-A) / P(B)
            not_parent_given_child = 1-notprob_child

            # P(A|-B) = P(-B|A)P(A) / P(-B)
            parent_given_not_child = (
                node.cpt[0][1] * single_parent.cpt[0]) / notprob_child

            # P(-A|-B) = P(-B|-A)P(-A) / P(-B)
            not_parent_given_not_child = 1 - parent_given_not_child

            # Appending all results into the result list
            # P(B)
            results.append(Node(f'P({node.name})', [], round(prob_child, 5)))
            # P(-B)
            results.append(
                Node(f'P(-{node.name})', [], round(notprob_child, 5)))
            # P(A|B)
            results.append(
                Node(f'P({single_parent.name}|{node.name})', [], round(parent_given_child, 5)))
            # P(-A|B)
            results.append(
                Node(f'P(-{single_parent.name}|{node.name})', [], round(not_parent_given_child, 5)))
            # P(A|-B)
            results.append(
                Node(f'P({single_parent.name}|-{node.name})', [], round(parent_given_not_child, 5)))
            # P(-A|-B)
            results.append(Node(
                f'P(-{single_parent.name}|-{node.name})', [], round(not_parent_given_not_child, 5)))

        elif not oneParent:
            while parents != []:
                print('This is a parent: ', parents[0])
                # P(A|B) = P(B|A)P(A) / P(B)
                # P(B) = P(B|A)P(A) + P(B|-A)P(-A)
                prob_child = (node.cpt[0][0]*parents[0].cpt[0]) + \
                    (node.cpt[1][0]*parents[0].cpt[1])
                # P(-B)
                notprob_child = 1-prob_child

                # P(A|B) = P(B|A)P(A) / P(B)
                parent_given_child = (
                    node.cpt[0][0]*parents[0].cpt[0])/prob_child
                # P(-A|B) = P(B|-A)P(-A) / P(B)
                not_parent_given_child = 1-notprob_child

                # P(A|-B) = P(-B|A)P(A) / P(-B)
                parent_given_not_child = (
                    node.cpt[0][1] * parents[0].cpt[0]) / notprob_child

                # P(-A|-B) = P(-B|-A)P(-A) / P(-B)
                not_parent_given_not_child = 1 - parent_given_not_child

                # Appending all results into the result list
                # P(B)
                results.append(
                    Node(f'P({node.name})', [], round(prob_child, 5)))
                # P(-B)
                results.append(
                    Node(f'P(-{node.name})', [], round(notprob_child, 5)))
                # P(A|B)
                results.append(
                    Node(f'P({parents[0].name}|{node.name})', [], round(parent_given_child, 5)))
                # P(-A|B)
                results.append(
                    Node(f'P(-{parents[0].name}|{node.name})', [], round(not_parent_given_child, 5)))
                # P(A|-B)
                results.append(
                    Node(f'P({parents[0].name}|-{node.name})', [], round(parent_given_not_child, 5)))
                # P(-A|-B)
                results.append(Node(
                    f'P(-{parents[0].name}|-{node.name})', [], round(not_parent_given_not_child, 5)))

                parents.remove(parents[0])

        return results


# B = Name , parents , B given A is true, B given A is false
nodes = [
    Node('A', [], ((0.01, 0.99))),
    Node('C', [], ((0.01, 0.99))),
    #       (( P(B|A) , P(-B|A) )  , ( P(B|-A) , P(-B|-A) ))
    Node('B', ['A', 'C'], ((0.8, 0.2), (0.1, 0.9)))
]

bayes = BayesianNetwork()

bayes.add_nodes(nodes)

result = bayes.get_parents_results('B')

for node in result:
    node.watch_node_info()
