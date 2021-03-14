public class Verification
{
	// 1 => Wall
	// 2 => Box
	// 3 => Place for box
	// 4 => Box in place for box
	// 5 => Player
	
	public static int verification(int x,int y,int[][] matrice)
	{
		if(matrice[x][y] == 0)
		{
			return 0 ;
		}
		else if(matrice[x][y] == 1)
		{
			return 1 ;
		}
		else if(matrice[x][y] == 2)
		{
			return 2 ;
		}
		else if(matrice[x][y] == 3)
		{
			return 3 ;
		}
		else if(matrice[x][y] == 4)
		{
			return 4 ;
		}
		else
		{
			return 6 ;
		}
	}
}
