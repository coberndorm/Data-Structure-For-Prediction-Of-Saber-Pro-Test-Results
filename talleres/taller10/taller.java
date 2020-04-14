public class Nodo
{
    Nodo izquierda;
    Nodo derecha;
    int dato;
    public Nodo(int dato){
        this.dato = dato;
    }
    public boolean buscar(int valor){
        if(dato == valor){
            return true;
        }
        else if(valor < dato){
            if(izquierda == null){
                return false;
            }
            else{
                return izquierda.buscar(valor);
            }
        }
        else{
            if(derecha == null){
                return false;
            }
            else{
                return derecha.buscar(valor);
            }
        }
    }
    public void insertar(int valor){
        if(valor > dato){
            if(derecha == null){
                derecha = new Nodo(valor);
            }
            else{
                derecha.insertar(valor);
            }
        }
        else{
            if(izquierda == null){
                izquierda = new Nodo(valor);
            }
            else{
                izquierda.insertar(valor);
            }
        }
    }
}
