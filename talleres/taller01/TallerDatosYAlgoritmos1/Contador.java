
public class Contador
{
    private int cont = 0;
    private String id;

    public Contador(String id){
     this.id = id;
    }

    public int incrementos(){
        cont++;
        return cont;
    }
    
    public void incrementar(){
        cont++;
    }
    
    public String toString() {
        return "El acomulado es " + cont;
    }
}
