#include <stdio.h>

int main(){
    // Declarar una variable
    int x = 45;
    int y = 63;
    int a = x >= y; // falso
    int b = x == 45; // verdadero

    // Operadores logicos en C, and, or y not

    int and = a && b;
    int or = a || b;
    int not = !a;
    
    printf("Es Verdadero? AND : %d\n", and);
    printf("Es Verdadero? OR : %d\n", or);
    printf("Es Verdadero? NOT : %d\n", not);
    
    return 0;
}