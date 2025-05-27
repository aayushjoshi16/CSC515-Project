import java.util.Arrays;

public class CacheSimulator {

    public CacheSimulator() {
        this.initialize();
    }

    private int config_total;

    public void config_step(int address, int lineNum) {
        this.config1_step(address);
        this.config2_step(address);
        this.config3_step(address);
        this.config4_step(address, lineNum);
        this.config5_step(address, lineNum);
        this.config6_step(address, lineNum);
        this.config7_step(address);
        config_total++;
    }


    //  Tag Index Block Byte
    //  21    9     0    2
    private final int config1_data_size = 2048;             // 2 KB
    private final int config1_ass = 1;
    private final int config1_block_size = 1;               // 1 Word

    private final int config1_byte_offset = 2;
    private final int config1_block_offset = 0;
    private final int config1_index_offset = 9;

    private final int[] config1_tag = new int[(int) Math.pow(2, config1_index_offset)];
    private int config1_hits;

    public void config1_step(int address) {
        int index = (address / ((int) Math.pow(2, config1_block_offset + config1_byte_offset))) % ((int) Math.pow(2, config1_index_offset));
        int tag = address >>> (config1_byte_offset + config1_block_offset + config1_index_offset);

        if (config1_tag[index] == tag) {
            config1_hits++;
        } else {
            config1_tag[index] = tag;
        }
    }

    //  Tag Index Block Byte
    //  21    8     1    2
    private final int config2_data_size = 2048;             // 2 KB
    private final int config2_ass = 1;
    private final int config2_block_size = 2;               // 2 Word

    private final int config2_byte_offset = 2;
    private final int config2_block_offset = 1;
    private final int config2_index_offset = 8;

    private final int[] config2_tag = new int[(int) Math.pow(2, config2_index_offset)];
    private int config2_hits;

    public void config2_step(int address) {
        int index = (address / ((int) Math.pow(2, config2_block_offset + config2_byte_offset))) % ((int) Math.pow(2, config2_index_offset));
        int tag = address >>> (config2_byte_offset + config2_block_offset + config2_index_offset);

        if (config2_tag[index] == tag) {
            config2_hits++;
        } else {
            config2_tag[index] = tag;
        }
    }


    //  Tag Index Block Byte
    //  21    7     2    2
    private final int config3_data_size = 2048;             // 2 KB
    private final int config3_ass = 1;
    private final int config3_block_size = 4;               // 4 Word

    private final int config3_byte_offset = 2;
    private final int config3_block_offset = 2;
    private final int config3_index_offset = 7;

    private final int[] config3_tag = new int[(int) Math.pow(2, config3_index_offset)];
    private int config3_hits;

    public void config3_step(int address) {
        int index = (address / ((int) Math.pow(2, config3_block_offset + config3_byte_offset))) % ((int) Math.pow(2, config3_index_offset));
        int tag = address >>> (config3_byte_offset + config3_block_offset + config3_index_offset);

        if (config3_tag[index] == tag) {
            config3_hits++;
        } else {
            config3_tag[index] = tag;
        }
    }

    //  Tag Index Block Byte
    //  22    8     0    2
    private final int config4_data_size = 2048;             // 2 KB
    private final int config4_ass = 2;
    private final int config4_block_size = 1;               // 1 Word

    private final int config4_byte_offset = 2;
    private final int config4_block_offset = 0;
    private final int config4_index_offset = 8;

    private final int[][] config4_tag_1 = new int[(int) Math.pow(2, config4_index_offset)][2];
    private final int[][] config4_tag_2 = new int[(int) Math.pow(2, config4_index_offset)][2];
    private int config4_hits;

    public void config4_step(int address, int lineNum) {
        int index = (address / ((int) Math.pow(2, config4_block_offset + config4_byte_offset))) % ((int) Math.pow(2, config4_index_offset));
        int tag = address >>> (config4_byte_offset + config4_block_offset + config4_index_offset);

        if (config4_tag_1[index][1] == tag) {
            config4_hits++;
            config4_tag_1[index][0] = lineNum;
        } else if (config4_tag_2[index][1] == tag) {
            config4_hits++;
            config4_tag_2[index][0] = lineNum;
        } else {
            if (config4_tag_1[index][0] < config4_tag_2[index][0]) {
                config4_tag_1[index][0] = lineNum;
                config4_tag_1[index][1] = tag;
            } else {
                config4_tag_2[index][0] = lineNum;
                config4_tag_2[index][1] = tag;
            }
        }
    }

    //  Tag Index Block Byte
    //  23    7     0    2
    private final int config5_data_size = 2048;             // 2 KB
    private final int config5_ass = 4;
    private final int config5_block_size = 1;               // 1 Word

    private final int config5_byte_offset = 2;
    private final int config5_block_offset = 0;
    private final int config5_index_offset = 7;

    private final int[][] config5_tag_1 = new int[(int) Math.pow(2, config5_index_offset)][2];
    private final int[][] config5_tag_2 = new int[(int) Math.pow(2, config5_index_offset)][2];
    private final int[][] config5_tag_3 = new int[(int) Math.pow(2, config5_index_offset)][2];
    private final int[][] config5_tag_4 = new int[(int) Math.pow(2, config5_index_offset)][2];
    private int config5_hits;

    public void config5_step(int address, int lineNum) {
        int index = (address / ((int) Math.pow(2, config5_block_offset + config5_byte_offset))) % ((int) Math.pow(2, config5_index_offset));
        int tag = address >>> (config5_byte_offset + config5_block_offset + config5_index_offset);

        if (config5_tag_1[index][1] == tag) {
            config5_hits++;
            config5_tag_1[index][0] = lineNum;
        } else if (config5_tag_2[index][1] == tag) {
            config5_hits++;
            config5_tag_2[index][0] = lineNum;
        } else if (config5_tag_3[index][1] == tag) {
            config5_hits++;
            config5_tag_3[index][0] = lineNum;
        } else if (config5_tag_4[index][1] == tag) {
            config5_hits++;
            config5_tag_4[index][0] = lineNum;
        } else {
            int tableNum = config5_getTableNum(index);
            if (tableNum == 1) {
                config5_tag_1[index][0] = lineNum;
                config5_tag_1[index][1] = tag;
            } else if (tableNum == 2) {
                config5_tag_2[index][0] = lineNum;
                config5_tag_2[index][1] = tag;
            } else if (tableNum == 3) {
                config5_tag_3[index][0] = lineNum;
                config5_tag_3[index][1] = tag;
            } else if (tableNum == 4) {
                config5_tag_4[index][0] = lineNum;
                config5_tag_4[index][1] = tag;
            }
        }
    }

    private int config5_getTableNum(int index) {
        int minLineNum = Integer.MAX_VALUE;
        int tableNum = 0;

        if (config5_tag_1[index][0] < minLineNum) {
            minLineNum = config5_tag_1[index][0];
            tableNum = 1;
        }
        if (config5_tag_2[index][0] < minLineNum) {
            minLineNum = config5_tag_2[index][0];
            tableNum = 2;
        }
        if (config5_tag_3[index][0] < minLineNum) {
            minLineNum = config5_tag_3[index][0];
            tableNum = 3;
        }
        if (config5_tag_4[index][0] < minLineNum) {
            tableNum = 4;
        }
        return tableNum;
    }

    //  Tag Index Block Byte
    //  23    5     2    2
    private final int config6_data_size = 2048;             // 2 KB
    private final int config6_ass = 4;
    private final int config6_block_size = 4;               // 4 Word

    private final int config6_byte_offset = 2;
    private final int config6_block_offset = 2;
    private final int config6_index_offset = 5;

    private final int[][] config6_tag_1 = new int[(int) Math.pow(2, config6_index_offset)][2];
    private final int[][] config6_tag_2 = new int[(int) Math.pow(2, config6_index_offset)][2];
    private final int[][] config6_tag_3 = new int[(int) Math.pow(2, config6_index_offset)][2];
    private final int[][] config6_tag_4 = new int[(int) Math.pow(2, config6_index_offset)][2];
    private int config6_hits;

    public void config6_step(int address, int lineNum) {
        int index = (address / ((int) Math.pow(2, config6_block_offset + config6_byte_offset))) % ((int) Math.pow(2, config6_index_offset));
        int tag = address >>> (config6_byte_offset + config6_block_offset + config6_index_offset);

        if (config6_tag_1[index][1] == tag) {
            config6_hits++;
            config6_tag_1[index][0] = lineNum;
        } else if (config6_tag_2[index][1] == tag) {
            config6_hits++;
            config6_tag_2[index][0] = lineNum;
        } else if (config6_tag_3[index][1] == tag) {
            config6_hits++;
            config6_tag_3[index][0] = lineNum;
        } else if (config6_tag_4[index][1] == tag) {
            config6_hits++;
            config6_tag_4[index][0] = lineNum;
        } else {
            int tableNum = config6_getTableNum(index);
            if (tableNum == 1) {
                config6_tag_1[index][0] = lineNum;
                config6_tag_1[index][1] = tag;
            } else if (tableNum == 2) {
                config6_tag_2[index][0] = lineNum;
                config6_tag_2[index][1] = tag;
            } else if (tableNum == 3) {
                config6_tag_3[index][0] = lineNum;
                config6_tag_3[index][1] = tag;
            } else if (tableNum == 4) {
                config6_tag_4[index][0] = lineNum;
                config6_tag_4[index][1] = tag;
            }
        }
    }

    private int config6_getTableNum(int index) {
        int minLineNum = Integer.MAX_VALUE;
        int tableNum = 0;

        if (config6_tag_1[index][0] < minLineNum) {
            minLineNum = config6_tag_1[index][0];
            tableNum = 1;
        }
        if (config6_tag_2[index][0] < minLineNum) {
            minLineNum = config6_tag_2[index][0];
            tableNum = 2;
        }
        if (config6_tag_3[index][0] < minLineNum) {
            minLineNum = config6_tag_3[index][0];
            tableNum = 3;
        }
        if (config6_tag_4[index][0] < minLineNum) {
            tableNum = 4;
        }
        return tableNum;
    }

    //  Tag Index Block Byte
    //  20    10     0    2
    private final int config7_data_size = 4096;             // 4 KB
    private final int config7_ass = 1;
    private final int config7_block_size = 1;               // 1 Word

    private final int config7_byte_offset = 2;
    private final int config7_block_offset = 0;
    private final int config7_index_offset = 10;

    private final int[] config7_tag = new int[(int) Math.pow(2, config7_index_offset)];
    private int config7_hits;

    public void config7_step(int address) {
        int index = (address / ((int) Math.pow(2, config7_block_offset + config7_byte_offset))) % ((int) Math.pow(2, config7_index_offset));
        int tag = address >>> (config7_byte_offset + config7_block_offset + config7_index_offset);

        if (config7_tag[index] == tag) {
            config7_hits++;
        } else {
            config7_tag[index] = tag;
        }
    }

    public void initialize() {
        Arrays.fill(config1_tag, 0);
        Arrays.fill(config2_tag, 0);
        Arrays.fill(config3_tag, 0);
        for (int i = 0; i < config4_tag_1.length; i++) {
            config4_tag_1[i][0] = 0;
            config4_tag_1[i][1] = 0;
            config4_tag_2[i][0] = 0;
            config4_tag_2[i][1] = 0;
        }
        for (int i = 0; i < config5_tag_1.length; i++) {
            config5_tag_1[i][0] = 0;
            config5_tag_1[i][1] = 0;
            config5_tag_2[i][0] = 0;
            config5_tag_2[i][1] = 0;
            config5_tag_3[i][0] = 0;
            config5_tag_3[i][1] = 0;
            config5_tag_4[i][0] = 0;
            config5_tag_4[i][1] = 0;
        }
        for (int i = 0; i < config6_tag_1.length; i++) {
            config6_tag_1[i][0] = 0;
            config6_tag_1[i][1] = 0;
            config6_tag_2[i][0] = 0;
            config6_tag_2[i][1] = 0;
            config6_tag_3[i][0] = 0;
            config6_tag_3[i][1] = 0;
            config6_tag_4[i][0] = 0;
            config6_tag_4[i][1] = 0;
        }
        Arrays.fill(config7_tag, 0);
        config_total = 0;

        config1_hits = 0;
        config2_hits = 0;
        config3_hits = 0;
        config4_hits = 0;
        config5_hits = 0;
        config6_hits = 0;
        config7_hits = 0;
    }

    public void printInfo() {
        double hitRate = ((double) config1_hits / config_total) * 100;
        String formattedHitRate = String.format("%.2f", hitRate);

        System.out.println("Cache #1\n" +
                "Cache size: " + config1_data_size + "B   Associativity: " + config1_ass + "    Block size: " + config1_block_size + "\n" +
                "Hits: " + config1_hits + "   Hit Rate: " + formattedHitRate + "%");
        System.out.println("---------------------------");

        hitRate = ((double) config2_hits / config_total) * 100;
        formattedHitRate = String.format("%.2f", hitRate);

        System.out.println("Cache #2\n" +
                "Cache size: " + config2_data_size + "B   Associativity: " + config2_ass + "    Block size: " + config2_block_size + "\n" +
                "Hits: " + config2_hits + "   Hit Rate: " + formattedHitRate + "%");
        System.out.println("---------------------------");

        hitRate = ((double) config3_hits / config_total) * 100;
        formattedHitRate = String.format("%.2f", hitRate);

        System.out.println("Cache #3\n" +
                "Cache size: " + config3_data_size + "B   Associativity: " + config3_ass + "    Block size: " + config3_block_size + "\n" +
                "Hits: " + config3_hits + "   Hit Rate: " + formattedHitRate + "%");
        System.out.println("---------------------------");

        hitRate = ((double) config4_hits / config_total) * 100;
        formattedHitRate = String.format("%.2f", hitRate);

        System.out.println("Cache #4\n" +
                "Cache size: " + config4_data_size + "B   Associativity: " + config4_ass + "    Block size: " + config4_block_size + "\n" +
                "Hits: " + config4_hits + "   Hit Rate: " + formattedHitRate + "%");
        System.out.println("---------------------------");

        hitRate = ((double) config5_hits / config_total) * 100;
        formattedHitRate = String.format("%.2f", hitRate);

        System.out.println("Cache #5\n" +
                "Cache size: " + config5_data_size + "B   Associativity: " + config5_ass + "    Block size: " + config5_block_size + "\n" +
                "Hits: " + config5_hits + "   Hit Rate: " + formattedHitRate + "%");
        System.out.println("---------------------------");

        hitRate = ((double) config6_hits / config_total) * 100;
        formattedHitRate = String.format("%.2f", hitRate);

        System.out.println("Cache #6\n" +
                "Cache size: " + config6_data_size + "B   Associativity: " + config6_ass + "    Block size: " + config6_block_size + "\n" +
                "Hits: " + config6_hits + "   Hit Rate: " + formattedHitRate + "%");
        System.out.println("---------------------------");

        hitRate = ((double) config7_hits / config_total) * 100;
        formattedHitRate = String.format("%.2f", hitRate);

        System.out.println("Cache #7\n" +
                "Cache size: " + config7_data_size + "B   Associativity: " + config7_ass + "    Block size: " + config7_block_size + "\n" +
                "Hits: " + config7_hits + "   Hit Rate: " + formattedHitRate + "%");
        System.out.println("---------------------------");
    }
}
