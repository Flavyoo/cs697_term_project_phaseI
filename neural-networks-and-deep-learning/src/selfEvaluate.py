import os

def selfEvaluate(e, mb, eta, hl):
    if mb == 1:
        # check quality rate for 1
        return
    # run the program
    prev_average_quality_rate = 0.0
    EPOCHS = e
    MB_SIZE = mb # powers
    ETA = eta
    HIDDEN_LAYER = hl
    """os.system("python run_experiment.py " + str(EPOCHS) + " " \
              + str(MB_SIZE) + " " + str(ETA) + " " + str(HIDDEN_LAYER) + " > selfEvaluate.txt")"""
    fileInput = open("selfEvaluate.txt")
    content = fileInput.read().splitlines();
    temp = content[10:-3]
    temp = [l.split() for l in temp]
    average_quality_rate = 0.0
    total = len(temp)
    for line in temp:
        # quality rate line
        if len(line) != 0:
            qr = line[6].replace(",", '')
        try:
            float(qr)
            average_quality_rate += float(qr)
        except ValueError:
            total -= 1
            continue

    average_quality_rate = average_quality_rate / (total * 1.0)
    #if prev_quality_rate != 0.0:
    # keep changing batch size until it increases to a max but then decreases
    if average_quality_rate > prev_average_quality_rate:
        prev_quality_rate = average_quality_rate
        MB_SIZE = MB_SIZE / 2
        selfEvaluate(EPOCHS, MB_SIZE, ETA, HIDDEN_LAYER)
    elif average_quality_rate < prev_average_quality_rate:
        return MB_SIZE * 2


selfEvaluate(5, 200, .01, 100)
