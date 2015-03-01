from collections import defaultdict
import operator
import re
import sys
from optparse import OptionParser
import string

# parse command line arguments
def parseArgs():
    try:
        parser = OptionParser()
        (options, args) = parser.parse_args()
        return args[0]
    except IndexError:
        print "**Please provide a .txt file as an argument."
        sys.exit(2)

# (sentence, sum) tuple of sentence with largest sum
def highestSum(charTable, inF):
    sentenceMap = {}
    f = open(inF,'r')
    regexp = re.compile(r'[a-zA-Z]')
    for line in f:
        for sentence in line.split('.  '):
            sum = 0
            for c in list(sentence):
                if re.match(regexp,c):
                    x = charTable[c.lower()]
                    sum+=x
            sentenceMap[sentence] = sum
                
    return maxCount (sentenceMap)

    
# return max of [(sentence, count)]
def maxCount(sentenceMap):
    ordered = sorted(sentenceMap.items(), key=operator.itemgetter(0))
    return ordered.pop()


# build a table of {char, int}
def buildCharTable():
    charTable = {}
    for c in string.letters:
        charTable[c.lower()] = ord(string.lower(c)) - ord('a') + 1
    return charTable

if __name__ == "__main__":

    inF = parseArgs()
    charTable = buildCharTable()
    max = highestSum(charTable, inF)
    print max[0] + ', ' + str(max[1])
