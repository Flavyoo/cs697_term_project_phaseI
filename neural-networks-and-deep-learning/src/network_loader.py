import cPickle as pickle
import theano
import theano.tensor as T
import crater_loader as cl

IMAGE_SIZE = 28

network_pickle = 'Pickles/elu-network28x28.pkl'
dataset= "non_rotated_28x28.pkl"

def predict():
    """
    An example of how to load a trained model and use it
    to predict labels.
    """

    # load the saved model
    classifier = pickle.load(open(network_pickle))

    # compile a predictor function
    predict_model = theano.function(
        inputs=[classifier.x],
        outputs=classifier.layers[-1].y_out)

    # We can test it on some examples from test test
    datasets = cl.load_crater_data_phaseII_wrapper(dataset, IMAGE_SIZE)
    test_set_x, test_set_y = datasets[2]
    test_set_x = test_set_x.get_value()

    predicted_values = predict_model(test_set_x[0])
    print("Predicted values for the first 10 examples in test set:")
    print(predicted_values)

if __name__ == '__main__':
    classifier = pickle.load(open(network_pickle))
    datasets = cl.load_crater_data_phaseII_wrapper(dataset, IMAGE_SIZE)
    test_set_x, test_set_y = datasets[0]
    # # test_set_x = test_set_x.get_value()
    # classifier.test_data = []
    # for i in range(100):
    #     print classifier.test_mb_predictions(i)

    i = T.lscalar()
    pred = theano.function(
        [i], classifier.layers[-1].y_out,
        givens={
            classifier.x:
            test_set_x[i*classifier.mini_batch_size: (i+1)*classifier.mini_batch_size]
        })
    for i in range(100):
        print pred(i)
    #predict()
