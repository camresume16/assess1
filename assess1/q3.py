import sys
from optparse import OptionParser

def main():
    try:
        parser = OptionParser()
        (options, args) = parser.parse_args()
        wholeNum = int(args[0])
        print "{} {}".format("hex is -- ", hex(wholeNum))
        print "{} {}".format("bin is -- ", bin(wholeNum))
    except IndexError:
        print "**Please provide a natural number as an argument."
        sys.exit(2)

if __name__ == "__main__":
    main()
