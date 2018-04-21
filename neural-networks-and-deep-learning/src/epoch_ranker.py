from operator import attrgetter

class EpochRanker(object):
    """ Stores epochs with their weights and biases, ranks them by
    quality rate and detect rate and produces the best one """
    def __init__(self):
        self.epochs = []

    def add_epoch(self, weights, biases, qr, dr):
        self.epochs.append(self.Epoch(weights, biases,
                                      qr, dr, len(self.epochs)))

    def best_epoch(self):
        self.__give_rankings("qr", self.epochs)
        self.__give_rankings("dr", self.epochs)
        for epoch in self.epochs:
            epoch.score = -1 * (epoch.qr_rank + epoch.dr_rank)
        self.__give_rankings("score", self.epochs)
        top_score = self.epochs[0].score
        best_epochs = []
        # Get epochs with top score
        for epoch in self.epochs:
            if epoch.score == top_score:
                best_epochs.append(epoch)
        # Chose epoch with best quality rate
        return self.__give_rankings("qr", best_epochs)[-1]

    def __give_rankings(self, attr, epochs):
        sorted_epochs = sorted(epochs, key=attrgetter(attr))
        for i in range(len(sorted_epochs)):
            setattr(sorted_epochs[i], "%s_rank" % attr, i)
        return sorted_epochs

    class Epoch(object):
        """ Epoch with weights and biases, quality and detection rates
        as well as rankings"""
        def __init__(self, weights, biases, qr, dr, id):
            self.weights = weights
            self.biases  = biases
            self.qr = qr
            self.dr = dr
            self.score = 0
            self.qr_rank = 0
            self.dr_rank = 0
            self.score_rank = 0
            self.id = "Epoch(%s)" % id

        def __repr__(self):
            return "%s -- (QR=%s,DR=%s,SCR=%s), RANKS(%s, %s, %s)" % \
                    (self.id,self.qr,self.dr,self.score,
                     self.qr_rank,self.dr_rank,self.score_rank)

if __name__ == "__main__":
    er.add_epoch(None,None,.90,.95)
    er.add_epoch(None,None,.95,.90)
    er.add_epoch(None,None,.63,.98)
    er.add_epoch(None,None,.78,.89)
    er.add_epoch(None,None,.04,.04)
    best = er.best_epoch()
    print best
