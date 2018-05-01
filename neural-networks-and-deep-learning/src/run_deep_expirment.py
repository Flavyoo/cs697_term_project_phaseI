from sys import argv as args
from crater_deep_network import run_experiments

# Default settings
#EPOCHS = 20
#MB_SIZE = 10
#ETA = .03

#if len(args) > 1:
#    if args[1] != '.': EPOCHS = int(args[1])
#if len(args) > 2:
#    if args[2] != '.': MB_SIZE = int(args[2])
#if len(args) > 3:
#    if args[3] != '.': ETA = float(args[3])

def main():
#  print "Making Network...."
#  print "Parameters: "
#  print "  Epochs  = %s" % EPOCHS
#  print "  MB_Size = %s" % MB_SIZE
#  print "  Eta     = %s" % ETA
#  run_experiments(EPOCHS, MB_SIZE, ETA)
  run_experiments()

if __name__ == "__main__":
  main()
