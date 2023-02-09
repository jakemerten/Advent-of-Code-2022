/* 
 * Sort all stacks into lists of Letters  - List one('D', 'Z', 'T')
 * 
 * Find a way to pull numbers from each line of text
 * 
 * Read line by line - pulling numbers -  (numberToMove), (stackToTake), (stackToReceive)
 * 
 * Use function to execute pop or push with above variables
 * 
*/

import java.io.*;
import java.util.ArrayList;
import java.util.List;


public class Day5 {

    // Lists of Crates
    static List<List<String>> listOfLists = new ArrayList<>();

    static List<String> listOne = new ArrayList<>();
    static List<String> listTwo = new ArrayList<>();
    static List<String> listThree = new ArrayList<>();
    static List<String> listFour = new ArrayList<>();
    static List<String> listFive = new ArrayList<>();
    static List<String> listSix = new ArrayList<>();
    static List<String> listSeven = new ArrayList<>();
    static List<String> listEight = new ArrayList<>();
    static List<String> listNine = new ArrayList<>();



    



    public static void main(String[] args) {

        

        listOne.add("H");
        listOne.add("T");
        listOne.add("Z");
        listOne.add("D");

        listTwo.add("Q");
        listTwo.add("R");
        listTwo.add("W");
        listTwo.add("T");
        listTwo.add("G");
        listTwo.add("C");
        listTwo.add("S");

        listThree.add("P");
        listThree.add("B");
        listThree.add("F");
        listThree.add("Q");
        listThree.add("N");
        listThree.add("R");
        listThree.add("C");
        listThree.add("H");

        listFour.add("L");
        listFour.add("C");
        listFour.add("N");
        listFour.add("F");
        listFour.add("H");
        listFour.add("Z");

        listFive.add("G");
        listFive.add("L");
        listFive.add("F");
        listFive.add("Q");
        listFive.add("S");

        listSix.add("V");
        listSix.add("p");
        listSix.add("W");
        listSix.add("Z");
        listSix.add("B");
        listSix.add("R");
        listSix.add("C");
        listSix.add("S");

        listSeven.add("Z");
        listSeven.add("F");
        listSeven.add("J");

        listEight.add("D");
        listEight.add("L");
        listEight.add("V");
        listEight.add("Z");
        listEight.add("R");
        listEight.add("H");
        listEight.add("Q");

        listNine.add("B");
        listNine.add("H");
        listNine.add("G");
        listNine.add("N");
        listNine.add("F");
        listNine.add("Z");
        listNine.add("L");
        listNine.add("D");

        listOfLists.add(listOne);
        listOfLists.add(listTwo);
        listOfLists.add(listThree);
        listOfLists.add(listFour);
        listOfLists.add(listFive);         
        listOfLists.add(listSix);
        listOfLists.add(listSeven);
        listOfLists.add(listEight);
        listOfLists.add(listNine);
    
        int numberToMove = 0;
        int stackToTake = 0;
        int stackToReceive = 0;
    




        try {
            File file = new File("input5.txt");
            BufferedReader br = new BufferedReader(new FileReader(file));
            String line;
            while ((line = br.readLine()) != null) {
               
                String [] numbers = line.split(" ");
                numberToMove = Integer.parseInt(numbers[1]);
                stackToTake = Integer.parseInt(numbers[3]);
                stackToReceive = Integer.parseInt(numbers[5]);
                
                String temp;
                // Part 2 flow- multiple crates moving at same time - do not reverse order
                
                if (numberToMove > 1) {
                    for(int i = numberToMove; i > 0; i--) {
                        temp = listOfLists.get(stackToTake -1).get((listOfLists.get(stackToTake - 1).size()) - i);
                        listOfLists.get(stackToTake -1).remove((listOfLists.get(stackToTake - 1).size()) - i);
                        listOfLists.get(stackToReceive -1).add(temp);
                    }
                }
                
                else {
                // Part 1 flow
                    for (int i = 0; i < numberToMove; i++) {
                                        
                        temp = listOfLists.get(stackToTake -1).get((listOfLists.get(stackToTake - 1).size()) - 1);
                        listOfLists.get(stackToTake -1).remove((listOfLists.get(stackToTake - 1).size()) - 1);
                        listOfLists.get(stackToReceive -1).add(temp);

                    }
                }


            }
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }


        List <String> message = new ArrayList<>();
        for (int i = 0; i < 9; i++) {
            
            message.add((listOfLists.get(i).get((listOfLists.get(i).size()) - 1)));
        
        }
        System.out.println(message);



    }
}
