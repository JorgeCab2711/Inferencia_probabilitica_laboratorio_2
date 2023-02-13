import numpy as np


class Infer():
    def __init__(self):
        self.events = {}
        pass
    def add_event(self, event:str, prob: float):
        if event not in self.events:
            self.events[event] = prob
        else:
            print("Warning: Adding event that already exists.", 'Event Name:', event)



inf = Infer()
inf.add_event('A',0.5)
inf.add_event('B',0.5)

print(inf.events)


