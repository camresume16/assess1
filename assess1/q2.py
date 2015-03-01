import os
import zipfile
import sys
from optparse import OptionParser

def main():
    try:
        parser = OptionParser()
        (options, args) = parser.parse_args()
        inF = args[0]
        printResults(inF)
    except IndexError:
        print "**Please provide a .zip file as an argument."
        sys.exit(2)

def printResults(inF):
    
    zipF= zipfile.ZipFile(inF)
    res = []
    for zipInfo in zipF.infolist():
        size = zipInfo.file_size
        name = zipInfo.filename
        if name.endswith('/') == False:
            fName = os.path.basename(name)
            res.append((fName, form(size)))

    # sort by max width of fname string
    maxW = sorted(res, key=lambda res: len(res[0])).pop()
    width = len(maxW[0])
    pad = " "*width
    # adjust each item to align printing
    for item in res:
        print "{}{}".format(item[0], item[1].rjust(width + (width - len(item[0]))))


def form(size):
    if size > 1000000:
        return "{} {}".format((size/1000000), 'MB')
    elif size > 1000:
        return "{} {}".format((size/1000), 'KB')
    else:
        return "{} {}".format(size, 'bytes')

if __name__ == "__main__":
    main()

