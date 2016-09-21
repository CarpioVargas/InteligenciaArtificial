#include<stdio.h>
#include <time.h>

void quicksort(int list[], int min, int max)
{
  int pivot, i, j, tmp;
  if(min < max) {
    pivot = min;
    i = min;
    j = max;
    while(i < j) {
      while(list[i] <= list[pivot] && i <= max)
        i++;
      while(list[j] > list[pivot] && j >= min)
        j--;
      if(i < j) {
        tmp = list[i];
        list[i] = list[j];
        list[j] = tmp;
      }
    }

    tmp = list[j];
    list[j] = list[pivot];
    list[pivot] = tmp;
    quicksort(list, min, j-1);
    quicksort(list, j+1, max);
  }
}

void printArray(int list[], int list_size)
{
    int i;
    for (i=0; i < list_size; i++)
        printf("%d ", list[i]);
    printf("\n");
}

void main()
{
    int list[10];
    int list_size = sizeof(list)/sizeof(list[0]);
    int i, n = 10;
    float time_spent;

    for (i = 0; i < n; i++) {
      list[i] = 1 + rand() % 100;
    }
    printf("\nLista original \n");
    printArray(list, list_size);
    clock_t begin = clock();
    quicksort(list, 0, list_size-1);
    clock_t end = clock();
    time_spent = (float)(end - begin) / CLOCKS_PER_SEC;
    printf("\nLista ordenada \n");
    printArray(list, list_size);
    printf("%.10f\n",time_spent );
}
