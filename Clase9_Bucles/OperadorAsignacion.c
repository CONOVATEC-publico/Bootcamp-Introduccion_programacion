#include <stdio.h>

int main(){
    int valor1 = 0;

    valor1 = valor1 + 2;
    printf("Valor: %d \n", valor1);
    valor1 += 2;
    printf("Valor: %d \n", valor1);

    valor1 -= 3;
    printf("Valor: %d \n", valor1);

    valor1 *= 32;
    printf("Valor: %d \n", valor1);
    valor1 /= 2;
    printf("Valor: %d \n", valor1);
    valor1 %= 3;
    printf("Valor: %d \n", valor1);
    return 0;
    
}