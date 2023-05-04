#include <stdio.h>

int main(){

    /**
     * Programa de que imprime una tabla de multiplicar del 1 al 10
     * por lo que tiene que imprimir las multiplicaciones, solo cuando el resultado
     * es multiplo de 6, se tiene que rompler el bucle, en caso de que el residuo de mod 
     * de resultado y 4 solo sea 1, tiene que escribir un continue.
    */
    for(int i = 1; i <= 10; i++){
        
        for (int  j = 1; j <= 10; j++)
        {
            int resultad = i * j;
            if(resultad % 4 == 1){
                continue;
            }
            if(resultad % 6 == 0){
                break;
            }
            
            printf("%d x %d = %d\n",i, j, resultad);
        }
        printf("\n");
    }   
    return 0;
}