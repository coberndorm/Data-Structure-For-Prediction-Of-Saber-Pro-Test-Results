
import java.io.;
import java.util.;
public class MatrizAdyacencia
{
    int[][] grafo;
    public MatrizAdyacencia(int a){
        this.grafo = new int[a][a];
    }
    public static void nuevaArista(int[][] grafo, int a, int b, int peso) {
        grafo[a][b] = peso;
    }
    public static ArrayList buscarRelaciones(int[][] grafo, int vertice){
        ArrayList<Integer> relaciones = new ArrayList<Integer>();
        for(int i=0; i<grafo.length; i++){
            if(grafo[vertice][i] != 0){
                relaciones.add(i);
            }
        }
        return relaciones;
    }
    public static int buscarPeso(int[][] grafo, int inicio, int llegada){
        return grafo[inicio][llegada];
    }
}
