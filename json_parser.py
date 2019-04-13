import sys
import os
import json

def parse_categories(jsonfile):
    infile = open(jsonfile, 'r')

    lines = []
    for line in infile: # there should just be one line but whatever
        lines.append(line)

    line = lines[0]

    event_list = json.loads(line)

    categories = set()
    for event in event_list:
        for category in event['categories']:
            categories.add(category)

    outfilename = 'categories.txt'
    os.system('touch {}'.format(outfilename))
    outfile = open(outfilename, 'w')
    
    categories_list = list(categories)
    categories_list.sort()
    for thing in categories_list:
        print(thing)
        print(thing, file=outfile)


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 {} file.json'.format(sys.argv[0]))
        quit()
    jsonfile = sys.argv[1]
    parse_categories(jsonfile)

if __name__ == '__main__':
    main()
