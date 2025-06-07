import sys
import argparse
from CacheSimulator import CacheSimulator

def read_file(fname, config_type):
    cs = CacheSimulator(config_type=config_type)
    
    with open(fname, 'r') as file:
        line_num = 1
        for line in file:
            line = line[1:].strip()  # Remove first character and trim whitespace
            address = int(line, 16)  # Convert hex string to integer
            
            cs.config_step(address, line_num)
            line_num += 1
    
    # cs.print_info()

def main():
    # Config str
    config_str = """Configuration type:\n
    1. 2KB, direct mapped, 1-word blocks\n
    2. 2KB, direct mapped, 2-word blocks\n
    3. 2KB, direct mapped, 4-word blocks\n
    4. 2KB, 2-way set associative, 1-word blocks\n
    5. 2KB, 4-way set associative, 1-word blocks\n
    6. 2KB, 4-way set associative, 4-word blocks\n
    7. 4KB, direct mapped, 1-word blocks\n
    all. Run all configurations"""

    parser = argparse.ArgumentParser(
                    prog='CacheSimulator',
                    description='Simulates a multilevel cache')
    parser.add_argument("filename", help="Name of the input address file")
    parser.add_argument("config_type", 
                        choices=["1", "2", "3", "4", "5", "6", "7", "all"],
                        help=config_str)
    args = parser.parse_args()
    
    # If config_type is not provided, print available configurations and exit
    if args.config_type is None:
        print(config_str)
        sys.exit(1)
    
    # Update read_file to accept config_type parameter
    read_file(args.filename, args.config_type)

if __name__ == "__main__":
    main()
