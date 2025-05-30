import sys
import argparse
from CacheSimulator import CacheSimulator

def read_file(fname):
    cs = CacheSimulator()
    
    with open(fname, 'r') as file:
        line_num = 1
        for line in file:
            line = line[1:].strip()  # Remove first character and trim whitespace
            address = int(line, 16)  # Convert hex string to integer
            
            cs.config_step(address, line_num)
            line_num += 1
    
    cs.print_info()

def main():
    parser = argparse.ArgumentParser(
                    prog='CacheSimulator',
                    description='Sumulates a multilevel cache')
    parser.add_argument("filename", help="Name of the input address file")
    args = parser.parse_args()
    read_file(args.filename)

if __name__ == "__main__":
    main()
