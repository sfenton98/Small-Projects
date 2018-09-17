import java.util.Random;
import java.util.Scanner;

public class main {

	private static Random random = new Random();
	private static int range = 100;
	private static Scanner kb =new Scanner(System.in); 
	
	//------------------------------------
	//		CREATE RANDOM NUMBER
	//------------------------------------
	public static void main(String[] args) {
		
		Boolean bool = false;
		
		System.out.println("-- GUESS A NUMBER BETWEEN 1-99");
	
		int numberToBeGuessed = createRandomNumber();
		
		do {
			int numberGuessed = readInt("Enter a number:");
			bool = checkNumber(numberToBeGuessed,numberGuessed);
			
		} while(bool == false);
	}
	
	//------------------------------------
	//	CREATE RANDOM NUMBER
	//------------------------------------
	public static int createRandomNumber() {
		
		int numberToBeGuessed = random.nextInt(range);
		
		return numberToBeGuessed;
	}
	
	public static boolean checkNumber(int numberToBeGuessed,int numberGuessed) {
		
		boolean bool = false;
		
		if(numberToBeGuessed == numberGuessed) {
			bool = true;
			System.out.println("You guessed correct! It was " + numberToBeGuessed);
		}
		else {
			if(numberGuessed<numberToBeGuessed) {
				System.out.println("Too low");
			}
			else if(numberGuessed>numberToBeGuessed) {
				System.out.println("Too high");
			}
		}
	
		
		return bool;
	}
	
	public static int readInt(String question) {
		int choice;
		System.out.print(question);
		while (!kb.hasNextInt()) {
			kb.nextLine();
			System.out.println("ERROR - must be integer");
			System.out.println(question);
		}
		choice = kb.nextInt();
		kb.nextLine();
		return choice;
	}
	

	
	
}
