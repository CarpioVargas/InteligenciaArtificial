#include<stdlib.h>
#include<stdio.h>
#include <time.h>

void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2){
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1){
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void sort(int arr[], int l, int r)
{
    if (l < r)
    {

        int m = l+(r-l)/2;
        sort(arr, l, m);
        sort(arr, m+1, r);

        merge(arr, l, m, r);
    }
}

void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

/* Driver program to test above functions */
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
    sort(list, 0, list_size - 1);
    clock_t end = clock();
    time_spent = (float)(end - begin) / CLOCKS_PER_SEC;
    printf("\nLista ordenada \n");
    printArray(list, list_size);
    printf("%.10f\n",time_spent );
}
