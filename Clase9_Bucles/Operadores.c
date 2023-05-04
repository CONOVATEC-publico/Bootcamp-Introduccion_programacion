#include <stdio.h>

int main(){
    // Declarar una variable
    int x = 45;
    int y = 0;
    printf("%d \n",x);

    y = x; // Operador de Asignacion
    printf("%d \n", y);

    x = y + 9;
    printf("El resultado de la suma es: %d \n", x);
    x = y - 15;
    printf("El resultado de la resta es: %d \n", x);

    x = y % 6;
    printf("El resto de %d y %d es: %d \n", y, 6,x);
    
    x++;
    printf("El valor de x es: %d \n", x);
    x--;
    printf("El valor de x es: %d \n", x);

    printf("El valor de x es: %d \n", ++x);
    printf("El valor de x es: %d \n", x++);
    printf("El valor de x es: %d \n", x);

    
    return 0;
}