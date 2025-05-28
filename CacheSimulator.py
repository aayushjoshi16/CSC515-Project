class CacheSimulator:
    
    def __init__(self):
        self.initialize()
    
    def config_step(self, address, line_num):
        self.config1_step(address)
        self.config2_step(address)
        self.config3_step(address)
        self.config4_step(address, line_num)
        self.config5_step(address, line_num)
        self.config6_step(address, line_num)
        self.config7_step(address)
        self.config_total += 1
    
    # Tag Index Block Byte
    # 21    9     0    2
    def __init__(self):
        self.config_total = 0
        
        # Config 1
        self.config1_data_size = 2048            # 2 KB
        self.config1_ass = 1
        self.config1_block_size = 1              # 1 Word
        
        self.config1_byte_offset = 2
        self.config1_block_offset = 0
        self.config1_index_offset = 9
        
        self.config1_tag = [0] * (2 ** self.config1_index_offset)
        self.config1_hits = 0
        
        # Config 2
        self.config2_data_size = 2048            # 2 KB
        self.config2_ass = 1
        self.config2_block_size = 2              # 2 Word
        
        self.config2_byte_offset = 2
        self.config2_block_offset = 1
        self.config2_index_offset = 8
        
        self.config2_tag = [0] * (2 ** self.config2_index_offset)
        self.config2_hits = 0
        
        # Config 3
        self.config3_data_size = 2048            # 2 KB
        self.config3_ass = 1
        self.config3_block_size = 4              # 4 Word
        
        self.config3_byte_offset = 2
        self.config3_block_offset = 2
        self.config3_index_offset = 7
        
        self.config3_tag = [0] * (2 ** self.config3_index_offset)
        self.config3_hits = 0
        
        # Config 4
        self.config4_data_size = 2048            # 2 KB
        self.config4_ass = 2
        self.config4_block_size = 1              # 1 Word
        
        self.config4_byte_offset = 2
        self.config4_block_offset = 0
        self.config4_index_offset = 8
        
        self.config4_tag_1 = [[0, 0] for _ in range(2 ** self.config4_index_offset)]
        self.config4_tag_2 = [[0, 0] for _ in range(2 ** self.config4_index_offset)]
        self.config4_hits = 0
        
        # Config 5
        self.config5_data_size = 2048            # 2 KB
        self.config5_ass = 4
        self.config5_block_size = 1              # 1 Word
        
        self.config5_byte_offset = 2
        self.config5_block_offset = 0
        self.config5_index_offset = 7
        
        self.config5_tag_1 = [[0, 0] for _ in range(2 ** self.config5_index_offset)]
        self.config5_tag_2 = [[0, 0] for _ in range(2 ** self.config5_index_offset)]
        self.config5_tag_3 = [[0, 0] for _ in range(2 ** self.config5_index_offset)]
        self.config5_tag_4 = [[0, 0] for _ in range(2 ** self.config5_index_offset)]
        self.config5_hits = 0
        
        # Config 6
        self.config6_data_size = 2048            # 2 KB
        self.config6_ass = 4
        self.config6_block_size = 4              # 4 Word
        
        self.config6_byte_offset = 2
        self.config6_block_offset = 2
        self.config6_index_offset = 5
        
        self.config6_tag_1 = [[0, 0] for _ in range(2 ** self.config6_index_offset)]
        self.config6_tag_2 = [[0, 0] for _ in range(2 ** self.config6_index_offset)]
        self.config6_tag_3 = [[0, 0] for _ in range(2 ** self.config6_index_offset)]
        self.config6_tag_4 = [[0, 0] for _ in range(2 ** self.config6_index_offset)]
        self.config6_hits = 0
        
        # Config 7
        self.config7_data_size = 4096            # 4 KB
        self.config7_ass = 1
        self.config7_block_size = 1              # 1 Word
        
        self.config7_byte_offset = 2
        self.config7_block_offset = 0
        self.config7_index_offset = 10
        
        self.config7_tag = [0] * (2 ** self.config7_index_offset)
        self.config7_hits = 0
        
        self.initialize()
    
    def config1_step(self, address):
        index = (address // (2 ** (self.config1_block_offset + self.config1_byte_offset))) % (2 ** self.config1_index_offset)
        tag = address >> (self.config1_byte_offset + self.config1_block_offset + self.config1_index_offset)
        
        if self.config1_tag[index] == tag:
            self.config1_hits += 1
        else:
            self.config1_tag[index] = tag
    
    def config2_step(self, address):
        index = (address // (2 ** (self.config2_block_offset + self.config2_byte_offset))) % (2 ** self.config2_index_offset)
        tag = address >> (self.config2_byte_offset + self.config2_block_offset + self.config2_index_offset)
        
        if self.config2_tag[index] == tag:
            self.config2_hits += 1
        else:
            self.config2_tag[index] = tag
    
    def config3_step(self, address):
        index = (address // (2 ** (self.config3_block_offset + self.config3_byte_offset))) % (2 ** self.config3_index_offset)
        tag = address >> (self.config3_byte_offset + self.config3_block_offset + self.config3_index_offset)
        
        if self.config3_tag[index] == tag:
            self.config3_hits += 1
        else:
            self.config3_tag[index] = tag
    
    def config4_step(self, address, line_num):
        index = (address // (2 ** (self.config4_block_offset + self.config4_byte_offset))) % (2 ** self.config4_index_offset)
        tag = address >> (self.config4_byte_offset + self.config4_block_offset + self.config4_index_offset)
        
        if self.config4_tag_1[index][1] == tag:
            self.config4_hits += 1
            self.config4_tag_1[index][0] = line_num
        elif self.config4_tag_2[index][1] == tag:
            self.config4_hits += 1
            self.config4_tag_2[index][0] = line_num
        else:
            if self.config4_tag_1[index][0] < self.config4_tag_2[index][0]:
                self.config4_tag_1[index][0] = line_num
                self.config4_tag_1[index][1] = tag
            else:
                self.config4_tag_2[index][0] = line_num
                self.config4_tag_2[index][1] = tag
    
    def config5_step(self, address, line_num):
        index = (address // (2 ** (self.config5_block_offset + self.config5_byte_offset))) % (2 ** self.config5_index_offset)
        tag = address >> (self.config5_byte_offset + self.config5_block_offset + self.config5_index_offset)
        
        if self.config5_tag_1[index][1] == tag:
            self.config5_hits += 1
            self.config5_tag_1[index][0] = line_num
        elif self.config5_tag_2[index][1] == tag:
            self.config5_hits += 1
            self.config5_tag_2[index][0] = line_num
        elif self.config5_tag_3[index][1] == tag:
            self.config5_hits += 1
            self.config5_tag_3[index][0] = line_num
        elif self.config5_tag_4[index][1] == tag:
            self.config5_hits += 1
            self.config5_tag_4[index][0] = line_num
        else:
            table_num = self.config5_get_table_num(index)
            if table_num == 1:
                self.config5_tag_1[index][0] = line_num
                self.config5_tag_1[index][1] = tag
            elif table_num == 2:
                self.config5_tag_2[index][0] = line_num
                self.config5_tag_2[index][1] = tag
            elif table_num == 3:
                self.config5_tag_3[index][0] = line_num
                self.config5_tag_3[index][1] = tag
            elif table_num == 4:
                self.config5_tag_4[index][0] = line_num
                self.config5_tag_4[index][1] = tag
    
    def config5_get_table_num(self, index):
        min_line_num = float('inf')
        table_num = 0
        
        if self.config5_tag_1[index][0] < min_line_num:
            min_line_num = self.config5_tag_1[index][0]
            table_num = 1
        if self.config5_tag_2[index][0] < min_line_num:
            min_line_num = self.config5_tag_2[index][0]
            table_num = 2
        if self.config5_tag_3[index][0] < min_line_num:
            min_line_num = self.config5_tag_3[index][0]
            table_num = 3
        if self.config5_tag_4[index][0] < min_line_num:
            table_num = 4
        
        return table_num
    
    def config6_step(self, address, line_num):
        index = (address // (2 ** (self.config6_block_offset + self.config6_byte_offset))) % (2 ** self.config6_index_offset)
        tag = address >> (self.config6_byte_offset + self.config6_block_offset + self.config6_index_offset)
        
        if self.config6_tag_1[index][1] == tag:
            self.config6_hits += 1
            self.config6_tag_1[index][0] = line_num
        elif self.config6_tag_2[index][1] == tag:
            self.config6_hits += 1
            self.config6_tag_2[index][0] = line_num
        elif self.config6_tag_3[index][1] == tag:
            self.config6_hits += 1
            self.config6_tag_3[index][0] = line_num
        elif self.config6_tag_4[index][1] == tag:
            self.config6_hits += 1
            self.config6_tag_4[index][0] = line_num
        else:
            table_num = self.config6_get_table_num(index)
            if table_num == 1:
                self.config6_tag_1[index][0] = line_num
                self.config6_tag_1[index][1] = tag
            elif table_num == 2:
                self.config6_tag_2[index][0] = line_num
                self.config6_tag_2[index][1] = tag
            elif table_num == 3:
                self.config6_tag_3[index][0] = line_num
                self.config6_tag_3[index][1] = tag
            elif table_num == 4:
                self.config6_tag_4[index][0] = line_num
                self.config6_tag_4[index][1] = tag
    
    def config6_get_table_num(self, index):
        min_line_num = float('inf')
        table_num = 0
        
        if self.config6_tag_1[index][0] < min_line_num:
            min_line_num = self.config6_tag_1[index][0]
            table_num = 1
        if self.config6_tag_2[index][0] < min_line_num:
            min_line_num = self.config6_tag_2[index][0]
            table_num = 2
        if self.config6_tag_3[index][0] < min_line_num:
            min_line_num = self.config6_tag_3[index][0]
            table_num = 3
        if self.config6_tag_4[index][0] < min_line_num:
            table_num = 4
        
        return table_num
    
    def config7_step(self, address):
        index = (address // (2 ** (self.config7_block_offset + self.config7_byte_offset))) % (2 ** self.config7_index_offset)
        tag = address >> (self.config7_byte_offset + self.config7_block_offset + self.config7_index_offset)
        
        if self.config7_tag[index] == tag:
            self.config7_hits += 1
        else:
            self.config7_tag[index] = tag
    
    def initialize(self):
        self.config1_tag = [0] * (2 ** self.config1_index_offset)
        self.config2_tag = [0] * (2 ** self.config2_index_offset)
        self.config3_tag = [0] * (2 ** self.config3_index_offset)
        
        self.config4_tag_1 = [[0, 0] for _ in range(2 ** self.config4_index_offset)]
        self.config4_tag_2 = [[0, 0] for _ in range(2 ** self.config4_index_offset)]
        
        self.config5_tag_1 = [[0, 0] for _ in range(2 ** self.config5_index_offset)]
        self.config5_tag_2 = [[0, 0] for _ in range(2 ** self.config5_index_offset)]
        self.config5_tag_3 = [[0, 0] for _ in range(2 ** self.config5_index_offset)]
        self.config5_tag_4 = [[0, 0] for _ in range(2 ** self.config5_index_offset)]
        
        self.config6_tag_1 = [[0, 0] for _ in range(2 ** self.config6_index_offset)]
        self.config6_tag_2 = [[0, 0] for _ in range(2 ** self.config6_index_offset)]
        self.config6_tag_3 = [[0, 0] for _ in range(2 ** self.config6_index_offset)]
        self.config6_tag_4 = [[0, 0] for _ in range(2 ** self.config6_index_offset)]
        
        self.config7_tag = [0] * (2 ** self.config7_index_offset)
        self.config_total = 0
        
        self.config1_hits = 0
        self.config2_hits = 0
        self.config3_hits = 0
        self.config4_hits = 0
        self.config5_hits = 0
        self.config6_hits = 0
        self.config7_hits = 0
    
    def print_info(self):
        hit_rate = (self.config1_hits / self.config_total) * 100
        formatted_hit_rate = "{:.2f}".format(hit_rate)
        
        print(f"Cache #1\n"
              f"Cache size: {self.config1_data_size}B   Associativity: {self.config1_ass}    Block size: {self.config1_block_size}\n"
              f"Hits: {self.config1_hits}   Hit Rate: {formatted_hit_rate}%")
        print("---------------------------")
        
        hit_rate = (self.config2_hits / self.config_total) * 100
        formatted_hit_rate = "{:.2f}".format(hit_rate)
        
        print(f"Cache #2\n"
              f"Cache size: {self.config2_data_size}B   Associativity: {self.config2_ass}    Block size: {self.config2_block_size}\n"
              f"Hits: {self.config2_hits}   Hit Rate: {formatted_hit_rate}%")
        print("---------------------------")
        
        hit_rate = (self.config3_hits / self.config_total) * 100
        formatted_hit_rate = "{:.2f}".format(hit_rate)
        
        print(f"Cache #3\n"
              f"Cache size: {self.config3_data_size}B   Associativity: {self.config3_ass}    Block size: {self.config3_block_size}\n"
              f"Hits: {self.config3_hits}   Hit Rate: {formatted_hit_rate}%")
        print("---------------------------")
        
        hit_rate = (self.config4_hits / self.config_total) * 100
        formatted_hit_rate = "{:.2f}".format(hit_rate)
        
        print(f"Cache #4\n"
              f"Cache size: {self.config4_data_size}B   Associativity: {self.config4_ass}    Block size: {self.config4_block_size}\n"
              f"Hits: {self.config4_hits}   Hit Rate: {formatted_hit_rate}%")
        print("---------------------------")
        
        hit_rate = (self.config5_hits / self.config_total) * 100
        formatted_hit_rate = "{:.2f}".format(hit_rate)
        
        print(f"Cache #5\n"
              f"Cache size: {self.config5_data_size}B   Associativity: {self.config5_ass}    Block size: {self.config5_block_size}\n"
              f"Hits: {self.config5_hits}   Hit Rate: {formatted_hit_rate}%")
        print("---------------------------")
        
        hit_rate = (self.config6_hits / self.config_total) * 100
        formatted_hit_rate = "{:.2f}".format(hit_rate)
        
        print(f"Cache #6\n"
              f"Cache size: {self.config6_data_size}B   Associativity: {self.config6_ass}    Block size: {self.config6_block_size}\n"
              f"Hits: {self.config6_hits}   Hit Rate: {formatted_hit_rate}%")
        print("---------------------------")
        
        hit_rate = (self.config7_hits / self.config_total) * 100
        formatted_hit_rate = "{:.2f}".format(hit_rate)
        
        print(f"Cache #7\n"
              f"Cache size: {self.config7_data_size}B   Associativity: {self.config7_ass}    Block size: {self.config7_block_size}\n"
              f"Hits: {self.config7_hits}   Hit Rate: {formatted_hit_rate}%")
        print("---------------------------")
