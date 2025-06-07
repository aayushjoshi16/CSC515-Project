import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class CacheConfig:
    def __init__(
        self,
        size,
        associativity,
        block_size,
        byte_offset,
        block_offset,
        index_offset,
        config_id,
    ):
        self.size = size
        self.associativity = associativity
        self.block_size = block_size
        self.byte_offset = byte_offset
        self.block_offset = block_offset
        self.index_offset = index_offset
        self.config_id = config_id

        self.num_sets = 2**index_offset
        self.tag_store = [
            [[0, 0] for _ in range(associativity)] for _ in range(self.num_sets)
        ]
        self.hits = 0
        self.total_accesses = 0

    def access(self, address, line_num) -> bool:
        index = (
            address // (2 ** (self.block_offset + self.byte_offset))
        ) % self.num_sets
        tag = address >> (self.byte_offset + self.block_offset + self.index_offset)

        hit = False
        for way in self.tag_store[index]:
            if way[1] == tag:
                way[0] = line_num  # Update timestamp
                hit = True
                break

        self.total_accesses += 1
        if hit:
            self.hits += 1
        else:
            # Miss: Replace the least recently used block
            lru_way = min(self.tag_store[index], key=lambda x: x[0])
            lru_way[0] = line_num
            lru_way[1] = tag

        return hit

    def hit_rate(self):
        return (self.hits / self.total_accesses) * 100 if self.total_accesses else 0

    def __str__(self):
        return (
            f"Cache #{self.config_id}\n"
            f"Cache size: {self.size}B   Associativity: {self.associativity}    Block size: {self.block_size}\n"
            f"Accesses {self.total_accesses}   Hits: {self.hits}   Hit Rate: {self.hit_rate():.2f}%"
        )


class CacheSimulator:
    def __init__(self, config_type="all"):
        self.config_type = config_type
        self.configs = [
            CacheConfig(2048, 1, 1, 2, 0, 9, 1),
            CacheConfig(2048, 1, 2, 2, 1, 8, 2),
            CacheConfig(2048, 1, 4, 2, 2, 7, 3),
            CacheConfig(2048, 2, 1, 2, 0, 8, 4),
            CacheConfig(2048, 4, 1, 2, 0, 7, 5),
            CacheConfig(2048, 4, 4, 2, 2, 5, 6),
            CacheConfig(4096, 1, 1, 2, 0, 10, 7),
        ]

    def config_step(self, address, line_num):
        hit = -1

        # Process all configurations independently
        for i, config in enumerate(self.configs):
            # If "all" configurations are requested, simulate large cache with all configs
            if self.config_type == "all":
                hit_result = config.access(address, line_num)
                if hit_result and hit == -1:
                    hit = i

            # If a specific configuration is requested, only process that one
            if self.config_type == str(i + 1):
                hit_result = config.access(address, line_num)
                if hit_result:
                    hit = i
                else:
                    hit = -1

        # Output in the original format for LSTM compatibility
        print(f"{hit + 1} {address:08x}")

    def print_info(self):
        for config in self.configs:
            eprint(config)
            eprint("---------------------------")
