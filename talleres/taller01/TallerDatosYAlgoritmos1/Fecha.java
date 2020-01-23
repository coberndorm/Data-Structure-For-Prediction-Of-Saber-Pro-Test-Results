
public class Fecha
{
    int dia;
    int mes;
    int año;
    public Fecha(int dia, int mes, int año){
        this.dia = dia;
        this.mes = mes;
        this.año = año;
    }
    
    public Fecha(String date){
        this.dia = Integer.parseInt(date.substring (0,date.indexOf("/")));
        this.mes = Integer.parseInt(date.substring (date.indexOf("/"),date.lastIndexOf("/")));
        this.año = Integer.parseInt(date.substring (date.lastIndexOf("/")));
    }
    
    public int getDia(){
        return dia;
    }
    
    public int getMes(){
        return mes;
    }
    
    public int getAño(){
        return año;
    }
    
    public String getFecha(){
        return dia+"/"+mes+"/"+año;
    }
    
    public boolean igual(Fecha date){
        if ((date.año == año && date.dia == dia) && date.mes == mes){
            return true;
        }
        return false;
    }
    
    public int compare(Fecha date){
        if(date.año > año) 
            return -1;
        else if(date.año < año)
            return 1;
        if(date.mes > mes) 
            return -1;
        else if(date.mes < mes)
            return 1;
        if(date.dia > dia) 
            return -1;
        else if(date.dia < dia)
            return 1;
        return 0;
    }
}
