#!/usr/bin/python
from operator import attrgetter

QUALITY_WEIGHT = 1.2

class EpochRanker(object):
    """ Stores epochs with their weights and biases, ranks them by
    quality rate and detect rate and produces the best one """
    def __init__(self):
        self.epochs = []

    def add_epoch(self, weights, biases, qr):
        self.epochs.append(self.Epoch(weights, biases,
                                      qr, len(self.epochs)))

    def best_epoch(self):
        ranked_epochs = self.__give_rankings("qr", self.epochs)
        return ranked_epochs[-1] # Last epoch is highest qual rate

    def __give_rankings(self, attr, epochs):
        sorted_epochs = sorted(epochs, key=attrgetter(attr))
        for i in range(len(sorted_epochs)):
            setattr(sorted_epochs[i], "%s_rank" % attr, i)
        return sorted_epochs

    class Epoch(object):
        """ Epoch with weights and biases, quality and detection rates
        as well as rankings"""
        def __init__(self, weights, biases, qr, id):
            self.weights = weights
            self.biases  = biases
            self.qr = qr
            self.score = 0
            self.qr_rank = 0
            self.id = "Epoch(%s)" % id

        def __repr__(self):
            return "%s -- (QR=%s)" % (self.id,self.qr)

if __name__ == "__main__":
    er = EpochRanker()
    er.add_epoch(None,None,.90)
    er.add_epoch(None,None,.95)
    er.add_epoch(None,None,.63)
    er.add_epoch(None,None,.78)
    er.add_epoch(None,None,.04)
    best = er.best_epoch()
    print best
