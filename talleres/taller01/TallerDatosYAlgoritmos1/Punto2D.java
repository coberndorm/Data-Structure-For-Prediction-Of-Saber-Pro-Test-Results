
import java.util.*;
public class Punto2D{
    double x;
    double y;
    public Punto2D(int x,int y, int z){
        this.x = x;
        this.y = y;
    }

    public int getX(){
        return (int)x;
    }
    
    public int getY(){
        return (int)y;
    }
    
    public double radioPolar(){
        return Math.sqrt(x*x + y*y);
    }

    public double anguloPolar(){
        return Math.atan(y/x);
    }
    
    public double distEuclidiana(Punto2D otro){
        return Math.sqrt((otro.x - x)*(otro.x - x) + (otro.y - y)*(otro.y - y));
    }
}