from collections import defaultdict
import operator
import sys
import re
from optparse import OptionParser

# parse command line arguments
def parseArgs():
    try:
        parser = OptionParser()
        (options, args) = parser.parse_args()
        return args[0]
    except IndexError:
        print "**Please provide a .txt file as an argument."
        sys.exit(2)

# (word, count) tuple of most frequent word
def mostFreq(inF):
    countDict = defaultdict(int)
    f = open(inF,'r')
    regexp = re.compile(r'(?![,])|(?![.])')
    for line in f:
        for word in line.split():
            if re.match(regexp,word):
                countDict[word.lower()] += 1
    return maxCount (countDict)

# return max of [(word, count)]
def maxCount(countDict):
    ordered = sorted(countDict.items(), key=operator.itemgetter(0))
    return ordered.pop()


if __name__ == "__main__":

    inF = parseArgs()
    max = mostFreq(inF)
    print "max word was -- " + max[0]
    print "max count was -- " + str(max[1])
