import java.util.Scanner ;

public class Testeur
{
	public static void main(String[] args)
	{
		int[][] matrice ={{1,1,1,1,1,1,1},
					{1,0,0,0,0,0,1},
					{1,0,0,2,0,0,1},
					{1,0,0,0,0,0,1},
					{1,0,0,0,0,3,1},
					{1,1,1,1,1,1,1}};
		Player test = new Player(4,4);
		System.out.println("Choisis une direction !");
		System.out.println("1 => haut");
		System.out.println("2 => droite");
		System.out.println("3 => bas");
		System.out.println("4 => gauche");
		System.out.println("5 => quitter");
		Scanner scan = new Scanner(System.in) ;
		int number = scan.nextInt();
		while(number != 5)
		{
			if(number > 5)
			{
				System.out.println("Choisis un chiffre entre 1 et 5 !");
				scan.nextInt();
			}
			else if(number == 1)
			{
				Move.up(test,matrice);
				number = scan.nextInt();
			}
			else if(number == 2)
			{
				Move.right(test,matrice);
				number = scan.nextInt();
			}
			else if(number == 3)
			{
				Move.down(test,matrice);
				number = scan.nextInt();
			}
			else if(number == 4)
			{
				Move.left(test,matrice);
				number = scan.nextInt();
			}
			else
			{
				scan.close();
			}
		}
	}
}
