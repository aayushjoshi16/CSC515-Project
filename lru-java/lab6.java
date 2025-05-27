import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class lab6 {
    public static void main(String[] args) throws FileNotFoundException {
        read_file(args[0]);
    }

    public static void read_file(String fName) throws FileNotFoundException {
        CacheSimulator cs = new CacheSimulator();
        Scanner s = new Scanner(new File(fName));

        int lineNum = 1;
        while (s.hasNextLine()) {
            String line = s.nextLine();
            line = line.substring(1);
            line = line.trim();
            int address = Integer.parseUnsignedInt(line, 16);

            cs.config_step(address, lineNum);
            lineNum++;
        }

        cs.printInfo();
    }
}
