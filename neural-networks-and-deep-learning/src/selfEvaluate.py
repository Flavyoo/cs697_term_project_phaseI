import os


def selfevaluateBatchSize(e, mb, eta, hl, pvqr):
    if mb == 1 or mb == 0:
        return (pvqr, mb * 2)
    prev_average_quality_rate = pvqr
    EPOCHS = e
    MB_SIZE = mb
    ETA = eta
    HIDDEN_LAYER = hl
    os.system("python run_experiment.py " + str(EPOCHS) + " " \
              + str(MB_SIZE) + " " + str(ETA) + " " + str(HIDDEN_LAYER) + " > selfEvaluate.txt")
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

    fileInput.close()
    average_quality_rate = average_quality_rate / (total * 1.0)
    print (average_quality_rate, MB_SIZE)
    # keep changing batch size until it increases to a max but then decreases
    if average_quality_rate >= prev_average_quality_rate:
        prev_average_quality_rate = average_quality_rate
        MB_SIZE = MB_SIZE / 2
        return selfevaluateBatchSize(EPOCHS, MB_SIZE, ETA, HIDDEN_LAYER, prev_average_quality_rate)
    elif average_quality_rate < prev_average_quality_rate:
        return (prev_average_quality_rate, MB_SIZE * 2)

def selfEvaluateEta(e, mb, eta, hl, qr):
    if eta == .3:
        return (qr, eta)
    prev_average_quality_rate = qr
    EPOCHS = e
    MB_SIZE = mb
    ETA = eta
    HIDDEN_LAYER = hl
    os.system("python run_experiment.py " + str(EPOCHS) + " " \
              + str(MB_SIZE) + " " + str(ETA) + " " + str(HIDDEN_LAYER) + " > selfEvaluate.txt")
    fileInput = open("selfEvaluate.txt")
    content = fileInput.read().splitlines();
    temp = content[10:-3]
    temp = [l.split() for l in temp]
    average_quality_rate = 0.0
    total = len(temp)
    print total
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

    fileInput.close()
    #print "TOTAL AGAIN"
    #print total
    average_quality_rate = average_quality_rate / (total * 1.0)
    print (average_quality_rate, ETA)
    # keep changing batch size until it increases to a max but then decreases
    if average_quality_rate >= prev_average_quality_rate:
        print "GREATER THAN"
        prev_average_quality_rate = average_quality_rate
        ETA = ETA + .05
        return selfEvaluateEta(EPOCHS, MB_SIZE, ETA, HIDDEN_LAYER, prev_average_quality_rate)
    elif average_quality_rate < prev_average_quality_rate:
        print "LESS THAN"
        return (prev_average_quality_rate, ETA - 0.1)



EPOCHS = 4
MB_SIZE = 4
ETA = 0.1
HIDDEN_LAYERS = 100
#bs_results = selfevaluateBatchSize(EPOCHS, MB_SIZE, ETA, HIDDEN_LAYERS, 0.0)
#print bs_results
#print "FINAL BATCH SIZE RESULTS"
eta_results = selfEvaluateEta(EPOCHS, MB_SIZE, ETA, HIDDEN_LAYERS, 0.0)
print eta_results
print "FINAL ETA RESULTS"
