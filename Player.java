public class Player
{
	private int x ;
	private int y ;
	
	public Player(int x , int y) 
	{
		this.x = x ;
		this.y = y ;
	}
	
	public Player()
	{
		this(1,1) ;
	} 
	
	public int setX(int x)
	{
		return this.x = x ;
	}
	
	public int getX()
	{
		return this.x ;
	}
	
	public int setY(int y)
	{
		return this.y = y ;
	} 
	
	public int getY()
	{
		return this.y ;
	} 
} 
