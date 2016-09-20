#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//ordenamiento por seleccion

void seleccion(int lista[]){
  int i, j, tmp, pos_min;
  int n = 10;
  clock_t begin = clock();
  for (i = 0; i < n-1; i++) {
    pos_min = i;
    for (j = i+1; j < n; j++) {
      if (lista[j] < lista[pos_min]) {
        pos_min = j;
      }
    }
    tmp = lista[i];
    lista[i] =  lista[pos_min];
    lista[pos_min] = tmp;
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
  int i, n = 10;
  for (i = 0; i < n; i++) {
    lista[i] = 1 + rand() % 100;
    printf("%d -- ",lista[i]);
  }
  printf("\n");
  seleccion(lista);
}
