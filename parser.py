import sys
import xml.etree.ElementTree as ET

SEPARATOR = ","

def xmltocsv(filename, columns):
    """
    Get xml data from the file given as first argument and convert 
    it to a csv following the columns given as secound argument
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    results = []
    for row in root:
        line = ""
        attributes = row.attrib
        for col in columns:
            if col in attributes:
                line += attributes[col].replace(",", " ").replace("\n", " ")
            line+=","
        results.append(line[:-1] + "\n")
    
    return results


def writecsv(filename, data, columns):
    """
    Write csv in a file
    """
    fn = '.'.join(filename.split(".")[:-1]) + ".csv"

    file = open(fn, 'w')
    file.write(columns + '\n')
    for d in data:
        file.write(d)
    
    file.close()


if __name__ == "__main__":
    filename = sys.argv[1]
    columns = sys.argv[2]
    data = xmltocsv(filename, columns.split(','))

    writecsv(filename, data, columns)
