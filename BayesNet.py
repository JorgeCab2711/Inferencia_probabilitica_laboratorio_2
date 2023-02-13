class BYNetwork:
    def __init__(self):
        self.events = {}
        self.probs = {}

    def add_event(self, event: str, prob: float, parents: list):
        # Checks if  the event name is non-empty
        if len(event) <= 0:
            raise Exception('Event name must be a non-empty string.')
        # If probability is greater than one or less than zero it will raise an exception.
        if prob < 0 or prob > 1:
            raise Exception('Probability must be between 0 and 1.')
        # Handles the probability
        if event[0] != '-':
            # adds the negated event
            Nprob = 1 - prob
            self.events[event] = [prob, Nprob, parents]
        # handle negation of probability
        elif event[0] == '-':
            # adds the non negated event
            not_negation = event.replace('-', '')
            # adds the negated event
            Nprob = 1 - prob
            self.events[not_negation] = [prob, Nprob, parents]

        for i in parents:
            if i not in self.events.keys():
                print('\nWarning: Parent'+' "' +
                      i + '" '+'is not in events.\n')


class Node:
    def __init__(self, name, prob, parents):
        self.name = name
        self.probability = prob
        self.parents = parents
        self.parent_n_node_events = {}


# TODO:  This will be the main.py
inf = BYNetwork()
inf.add_event('homicida', 0.01, [])
inf.add_event('sangre', 0.8, ['homicida'])

print(inf.events)
