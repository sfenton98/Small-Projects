/*
 *  Shane Fenton
 */

import java.util.Random;

public class main {

	public static void main(String[] args) {
		
		Random random = new Random();
		
		String alphabet[] 	= {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
		String characters[] = {"@","£","#","%","&","*","(",")","$"};
		int    numbers[] 	= {1,2,3,4,5,6,7,8,9,0};
		
		
		int numLetters = alphabet.length;
		int numCharacters = characters.length;
		int numNumbers = numbers.length;
		
		int minNumber = 15;
		int maxNumber = 20;
		int index = 0;
		

			do{
				index++;
			
				int number = random.nextInt(3);
			
				switch(number) {
				case 0:
					System.out.print(alphabet[random.nextInt(numLetters)]);
					break;
					
				case 1:
					System.out.print(characters[random.nextInt(numCharacters)]);
					break;
					
				case 2:
					System.out.print(numbers[random.nextInt(numNumbers)]);
					break;
					
				}
			    
			}
			while(index < minNumber);
				
			
			System.out.print(alphabet[random.nextInt(maxNumber)]);
		
		
 	}

}
