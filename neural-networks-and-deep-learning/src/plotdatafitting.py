"""
Flavio Andrade 5-11-18

This programs plots the test and validation accuracies.
"""
import matplotlib.pyplot as plt
import matplotlib as mpl

def plotDataFit(testData, validationData, EPOCHS):
    mpl.style.use('seaborn')
    plt.title("Test vs Validation Accuracy", color='C0')
    plt.axis([0, EPOCHS, 0, 100])
    plt.ylabel('Accuracy')
    plt.xlabel('Epochs')
    epochs = list(range(EPOCHS))
    line1, = plt.plot(epochs, testData)
    line2, = plt.plot(epochs, validationData)
    plt.legend([line1, line2], ['Test Data', 'Validation Data'])
    plt.show()

if __name__ == '__main__':
    test = list(range(15))
    vals = list(range(15, 30))
    plotDataFit(test, vals, 15)
