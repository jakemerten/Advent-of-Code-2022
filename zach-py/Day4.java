import java.io.*;

public class Day4 {


    public static void main(String[] args) {

        int ass_pairs = 0;

        try {
            File file = new File("input4.txt");
            BufferedReader br = new BufferedReader(new FileReader(file));
            String line;
            while ((line = br.readLine()) != null) {
               
               String [] numbers = line.split(",");
               String [] firstPair = numbers[0].split("-");
               String [] secondPair = numbers[1].split("-");
               
               int first_floor = Integer.parseInt(firstPair[0]);
               int first_ceiling = Integer.parseInt(firstPair[1]);
               
               int second_floor = Integer.parseInt(secondPair[0]);
               int second_ceiling = Integer.parseInt(secondPair[1]);
                
               if (first_floor <= second_floor && first_ceiling >= second_ceiling) {
                    ass_pairs += 1;
               }
                else if (first_floor >= second_floor && first_ceiling <= second_ceiling) {
                    ass_pairs += 1;
                }
                
                //**** For Part 2 Add this parametr as well */
                else if ( second_floor <= first_ceiling && second_ceiling >= first_floor) {
                    ass_pairs += 1;
                }                    
               //System.out.println(first_floor +" " + first_ceiling + " " + second_floor + " " + second_ceiling);

            }
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println(" ass pairs: " + ass_pairs);


    }
   
}
