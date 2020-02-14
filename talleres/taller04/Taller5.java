import java.lang.*;
import java.util.*;

public class Taller5
{   
    //arrayMax complejidad esperada es n
    public int arrayMax (int i, int[] array, int max){
        if (i >= array.length)
            return max;
        if (array[i] > max)
            max = array [i];
        return arrayMax (i+1, array, max);    
    }

    // groupSum complejidad esperada es 2 a la n
    public boolean groupSum (int i, int[] array, int max){
        if (i >= array.length)
            return max == 0;
        return groupSum (i+1, array, max - array [i]) || groupSum (i+1, array, max);
    }

    //fibonacci complejidad esperada es 2 a la n
    public int fibonacci (int num){
        if (num <= 1) 
            return num;
        return fibonacci (num-1) + fibonacci(num-2);
    }

    public int[] llenarArrayAleatorio(int tam) {
        Random random = new Random();
        int[] numeros = new int[tam];
        int n;
        for (int i = 0; i < numeros.length; i++) {
                n = random.nextInt();
                if(n<0)
                    numeros[i] = -n;
                else 
                    numeros[i] = n;
        }
        return numeros;
    }

    public void tiempoArrayMax () {
        for (int i = 10000; i <= 200000; i += 10000){
            int [] array = llenarArrayAleatorio(i);
            long startTime = System.currentTimeMillis();
            arrayMax(0, array, 0);
            long endTime = System.currentTimeMillis();
            System.out.println (i + ": " + (endTime - startTime));
        }
    }

    public void tiempoGroupSum () {
        for (int i = 10; i <=32; i += 1){
            int [] array = llenarArrayAleatorio(i);
            long startTime = System.currentTimeMillis();
            groupSum(0, array, 1067789);
            long endTime = System.currentTimeMillis();
            System.out.println (i + ": " + (endTime - startTime));
        }
    }
    public void tiempoFibonacci () {
        for (int i = 10; i <= 40; i += 1){
            long startTime = System.currentTimeMillis();
            fibonacci(i);
            long endTime = System.currentTimeMillis();
            System.out.println (i + ": " + (endTime - startTime));
        }
    }
}