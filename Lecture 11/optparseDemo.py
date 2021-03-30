from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest='filename', help='file')
    parser.add_option("-a", "--action", dest='filename', help='file')

    options, remainder = parser.parse_args()
    print(options.filename)

main()