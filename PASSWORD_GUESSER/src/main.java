import java.util.Random;

/**
 * 
 * @author shanefenton09
 * Caused a stack overflow when adding 3+ characters in program.
 * Need to get it out of main somehow?
 *
 */

public class main {

	static Random random = new Random();
	
	private static  String alphabet[] 	= {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
	private static String characters[] = {"@","£","#","%","&","*","(",")","$"};
	
	private static int numLetters = alphabet.length;
	private static int numCharacters = characters.length;		
	private static int minNumber = 2;
	
	
	
	
	//--------------------------------------------
	//					MAIN	
	//--------------------------------------------
	public static void main(String[] args) {
		
		String pass = createRanPassword();
		System.out.println("Password to be guessed is: " + pass);
		guessingPassword(pass);	
	}
	
	
	//-----------------------------------------------------------
	//				CREATING A RANDOM PASSWORD
	//-----------------------------------------------------------
	public static String createRanPassword() {
		
		String password[]   = new String[minNumber];
		String newPassword = "";
		int index = 0;
		
		do{
			int number = random.nextInt(2);
		
			switch(number) {
				case 0:
					String a = alphabet[random.nextInt(numLetters)];
					password[index] = a;
					index++;
					break;
					
				case 1:
					String b = characters[random.nextInt(numCharacters)];
					password[index] = b;
					index++;
					break;	
			}
		}
		while(index < minNumber);
		
		//Putting all letters from array into a string 
		for(int x = 0; x < password.length; x++) {
			newPassword+=password[x];
		}
		
		//Returning password
		return newPassword;
	}
	
	
	//-----------------------------------------------------------
	//				CREATING A RANDOM PASSWORD
	//-----------------------------------------------------------
	public static void guessingPassword(String password) {
	
		String guess = createRanPassword();
		
		System.out.println("Trying: " + guess);
		
		if(guess.equals(password)) {
			
			System.out.println("I found the password! It is '" + guess + "'");
			System.exit(0);
		}
		
		else if(!guess.equals(password)) {
			guessingPassword(password);
			
		}
		
		
	}
}
