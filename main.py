import sys
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
    if len(sys.argv) > 1:
        read_file(sys.argv[1])
    else:
        print("Please provide a filename as argument")

if __name__ == "__main__":
    main()
