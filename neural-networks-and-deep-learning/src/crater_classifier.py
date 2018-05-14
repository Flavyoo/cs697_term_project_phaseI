import cPickle
import theano
import theano.tensor as T
import numpy as np

class CraterClassifier(object):

    def __init__(self, network_pickle, images):
        """ Makes an object that takes a list of images and classifies
            them as either craters or non-craters. """

        print images[:5]
        self.network = cPickle.load(open(network_pickle, 'rb'))
        self.images = self.shared(images)
        self.num_imgs = self.images.shape[0].eval()
        print "NUMBER OF IMGS = %s" % self.num_imgs
        i = T.lscalar()
        self.classify_fn = theano.function(
            [i], self.network.layers[-1].y_out,
            givens={
                self.network.x:
                self.images[i*self.network.mini_batch_size: (i+1)*self.network.mini_batch_size]
            })

    def shared(self, data):
        """Place the data into shared variables.  This allows Theano to copy
        the data to the GPU, if one is available.
        """
        shared_x = theano.shared(
            np.asarray(data, dtype=theano.config.floatX), borrow=True)
        return shared_x

    def get_classifications(self):
        """ Perform classifications on image data set. Returns an array of
            classifications (1 or 0) for each image in the list. """
        print self.images
        classifications = []
        for i in range(self.num_imgs):
            classifications.append(self.classify_fn(i)[0])
        return classifications

if __name__ == '__main__':
    import crater_loader as cl
    network_pickle = 'Pickles/ELU-ntwk-e0-val0.9709-tst0.9643.pkl'
    dataset= "101x101.pkl"
    image_size = 101
    print "Loading network..."
    classifier = cPickle.load(open(network_pickle))
    print "Getting Labels...."
    images, labels = cPickle.load(open(dataset))[2]
    print images[:5]
    print "Making classifier..."
    cc = CraterClassifier(network_pickle, images)
    print "Making classifications with network..."
    results = cc.get_classifications()
    # for tup in zip(results, labels):
    #     print tup
    print results
