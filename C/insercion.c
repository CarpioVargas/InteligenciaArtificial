#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//ordenamiento por seleccion

void insercion(int lista[]){
  int tmp, i , j;
  int n = 10;
  clock_t begin = clock();
  for (i = 0; i < n; i++) {
    tmp = lista[i];
    for (j = i; (j>0) && (tmp<lista[j-1]); j--) {
      lista[j] = lista[j-1];
    }
    lista[j] = tmp;
  }

  clock_t end = clock();
  float time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  for (i = 0; i < n; i++) {
    printf("%d -- ",lista[i]);
  }
  printf("\n");
  printf("tiempo consumido en ejecucion: %f",time_spent );
  printf("\n");
}

void main() {
  int lista[10];
  int i;
  int n = 10;
  for (i = 0; i < n; i++) {
    lista[i] = 1 + rand() % 100;
    printf("%d -- ",lista[i]);
  }
  printf("\n");
  insercion(lista);
}
