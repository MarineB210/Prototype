public class Move
{
	// 1 => Wall
	// 2 => Box
	// 3 => Place for box
	// 4 => Box in place for box
	// 5 => Player
	
	public static void right(Player player,int[][] matrice)
	{
		int coordonateX = player.getX();
		int coordonateY = player.getY();
		int verification = Verification.verification(coordonateX,coordonateY+1,matrice);
		if(verification == 0)
		{
			matrice[coordonateX][coordonateY] = 0;
			matrice[coordonateX][coordonateY+1] = 5;
			player.setY(coordonateY+1);
		}
		else if(verification == 2)
		{
			int secondVerification = Verification.verification(coordonateX,coordonateY+2,matrice);
			if(secondVerification == 0)
			{
				matrice[coordonateX][coordonateY] = 0;
				matrice[coordonateX][coordonateY+1] = 5;
				matrice[coordonateX][coordonateY+2] = 2;
				player.setY(coordonateY+1);
			}
			else if(secondVerification == 3)
			{
				matrice[coordonateX][coordonateY] = 0;
				matrice[coordonateX][coordonateY+1] = 5;
				matrice[coordonateX][coordonateY+2] = 4;
				player.setY(coordonateY+1);
			}
			else
			{
				System.out.println("Vous ne pouvez pas bouger cette box a droite !");
			}
		}
		else
		{
			System.out.println("Vous ne pouvez pas aller a droite !");
		}
		projectionMatrice(matrice) ; 
	}
	
	public static void left(Player player,int[][] matrice)
	{
		int coordonateX = player.getX();
		int coordonateY = player.getY();
		int verification = Verification.verification(coordonateX,coordonateY-1,matrice);
		if(verification == 0)
		{
			matrice[coordonateX][coordonateY] = 0;
			matrice[coordonateX][coordonateY-1] = 5;
			player.setY(coordonateY-1);
		}
		else if(verification == 2)
		{
			int secondVerification = Verification.verification(coordonateX,coordonateY-2,matrice);
			if(secondVerification == 0)
			{
				matrice[coordonateX][coordonateY] = 0;
				matrice[coordonateX][coordonateY-1] = 5;
				matrice[coordonateX][coordonateY-2] = 2;
				player.setY(coordonateY-1);
			}
			else if(secondVerification == 3)
			{
				matrice[coordonateX][coordonateY] = 0;
				matrice[coordonateX][coordonateY-1] = 5;
				matrice[coordonateX][coordonateY-2] = 4;
				player.setY(coordonateY-1);
			}
			else
			{
				System.out.println("Vous ne pouvez pas bouger cette box a gauche !");
			}
		}
		else
		{
			System.out.println("Vous ne pouvez pas aller a gauche !");
		}
		projectionMatrice(matrice) ;
	}
	
	public static void up(Player player,int[][] matrice)
	{
		int coordonateX = player.getX();
		int coordonateY = player.getY();
		int verification = Verification.verification(coordonateX-1,coordonateY,matrice);
		if(verification == 0)
		{
			matrice[coordonateX][coordonateY] = 0;
			matrice[coordonateX-1][coordonateY] = 5;
			player.setX(coordonateX-1);
		}
		else if(verification == 2)
		{
			int secondVerification = Verification.verification(coordonateX-2,coordonateY,matrice);
			if(secondVerification == 0)
			{
				matrice[coordonateX][coordonateY] = 0;
				matrice[coordonateX-1][coordonateY] = 5;
				matrice[coordonateX-2][coordonateY] = 2;
				player.setX(coordonateX-1);
			}
			else if(secondVerification == 3)
			{
				matrice[coordonateX][coordonateY] = 0;
				matrice[coordonateX-1][coordonateY] = 5;
				matrice[coordonateX-2][coordonateY] = 4;
				player.setX(coordonateX-1);
			}
			else
			{
				System.out.println("Vous ne pouvez pas bouger cette box en haut !");
			}
		}
		else
		{
			System.out.println("Vous ne pouvez pas aller en haut !");
		}
		projectionMatrice(matrice) ;
	}
	
	public static void down(Player player,int[][] matrice)
	{
		int coordonateX = player.getX();
		int coordonateY = player.getY();
		int verification = Verification.verification(coordonateX+1,coordonateY,matrice);
		if(verification == 0)
		{
			matrice[coordonateX][coordonateY] = 0;
			matrice[coordonateX+1][coordonateY] = 5;
			player.setX(coordonateX+1);
		}
		else if(verification == 2)
		{
			int secondVerification = Verification.verification(coordonateX+2,coordonateY,matrice);
			if(secondVerification == 0)
			{
				matrice[coordonateX][coordonateY] = 0;
				matrice[coordonateX+1][coordonateY] = 5;
				matrice[coordonateX+2][coordonateY] = 2;
				player.setX(coordonateX+1);
			}
			else if(secondVerification == 3)
			{
				matrice[coordonateX][coordonateY] = 0;
				matrice[coordonateX+1][coordonateY] = 5;
				matrice[coordonateX+2][coordonateY] = 4;
				player.setX(coordonateX+1);
			}
			else
			{
				System.out.println("Vous ne pouvez pas bouger cette box en bas !");
			}
		}
		else
		{
			System.out.println("Vous ne pouvez pas aller en bas !");
		}
		projectionMatrice(matrice) ;
	}
	
	public static void projectionMatrice(int[][] matrice)
	{
		int longerX = 6;
		int longerY = 7;
		String message = "";
		for(int i = 0 ; i < longerX ; i++)
		{
			System.out.println(message);
			message = "" ;
			for(int j = 0 ; j < longerY ; j++)
			{
				message = message + matrice[i][j] ;
			}
		}
		System.out.println(message);
		System.out.println("");
	}
}
