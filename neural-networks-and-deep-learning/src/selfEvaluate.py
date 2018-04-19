import os

def selfEvaluate(e, mb, eta, hl):
    # run the program
    intitial_quality_rate = 0.0
    EPOCHS = e
    MB_SIZE = mb # powers
    ETA = eta
    HIDDEN_LAYER = hl
    """os.system("python run_experiment.py " + str(EPOCHS) + " " \
              + str(MB_SIZE) + " " + str(ETA) + " " + str(HIDDEN_LAYER) + " > selfEvaluate.txt")"""
    fileInput = open("selfEvaluate.txt")
    content = fileInput.readlines();
    quality_rate = content[-1].split(" ")
    try:
        float(element)
    except ValueError:
        print "Not a float"
        print "Continuing"
    if quality_rate > intitial_quality_rate:
        intitial_quality_rate = quality_rate
        selfEvaluate(EPOCHS, MB_SIZE, ETA, HIDDEN_LAYER)
    elif quality_rate < intitial_quality_rate:
        MB_SIZE = MB_SIZE / 2




selfEvaluate(1, 200, .01, 100)
