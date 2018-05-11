import cPickle
import theano
import theano.tensor as T

class CraterClassifier(object):

    def __init__(self, network_pickle, images):
        """ Makes an object that takes a list of images and classifies
            them as either craters or non-craters. """
        self.network = cPickle.load(open(network_pickle, 'rb'))
        self.images = images
        self.num_imgs = self.images.shape[0].eval()
        i = T.lscalar()
        self.classify_fn = theano.function(
            [i], self.network.layers[-1].y_out,
            givens={
                self.network.x:
                self.images[i*self.network.mini_batch_size: (i+1)*self.network.mini_batch_size]
            })

    def get_classifications(self):
        """ Perform classifications on image data set. Returns an array of
            classifications (1 or 0) for each image in the list. """
        classifications = []
        for i in range(self.num_imgs):
            classifications.append(self.classify_fn(i)[0])
        return classifications

if __name__ == '__main__':
    import crater_loader as cl
    network_pickle = 'Pickles/elu-network28x28.pkl'
    dataset= "non_rotated_28x28.pkl"
    image_size = 28
    classifier = cPickle.load(open(network_pickle))
    datasets = cl.load_crater_data_phaseII_wrapper(dataset, image_size)
    test_set_x, test_set_y = datasets[0]
    cc = CraterClassifier(network_pickle, test_set_x)
    print cc.get_classifications()
