#include <stdio.h>
#include <stdbool.h>

int main(){
    // Declarar una variable
    int i = 1;
    do{
        if(i % 2 == 0){
            printf("%d \n", i);
        }
        i++;
    }while (i <= 20);
    
    
    return 0;
}