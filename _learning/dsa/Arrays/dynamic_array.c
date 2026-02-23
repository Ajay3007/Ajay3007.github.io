#include <stdio.h>
#include <stdlib.h>
#define INITIAL_SIZE 8

typedef struct {
    int size;
    int capacity;
    int *array;
} dynamic_array;

// function prototypes
void initArray(dynamic_array **container);
void freeArray(dynamic_array *container);
// CRUD
void insertItem(dynamic_array *container, int item);
int getItem(dynamic_array *container, int index);
void updateItem(dynamic_array *container, int index, int item);
void deleteItem(dynamic_array *container, int item);
void printArray(dynamic_array *container);

int main() {
    dynamic_array *container;
    initArray(&container);
    for(int i = 1; i < 6; i++) {
        insertItem(container, 3*i + 10);
    }
    printArray(container);
    int index = 2;
    int item = getItem(container, index);
    if(item >= 0) 
        printf("Item at index %d = %d\n", index, item);
    else
        printf("Enter a valid index\n");
    index = 4;
    item = 100;
    updateItem(container, index, item);
    printArray(container);
    item = 19;
    deleteItem(container, item);
    printArray(container);
    printf("Insert 10 more items in the container.\n");
    for(int i = 1; i <= 10; i++) {
        insertItem(container, 2*i - 1);
    }
    printArray(container);
    freeArray(container);
    // insertItem(container, 10);  // ERROR: AddressSanitizer: heap-use-after-free
    return 0;
}

//------Function Definitions------
void initArray(dynamic_array **container_ptr) {
    dynamic_array *container = (dynamic_array *)malloc(sizeof(dynamic_array));
    if(container == NULL) {
        printf("ERROR: Container memory allocation failed.\n");
        exit(0);
    }
    container->size = 0;
    container->capacity = INITIAL_SIZE;
    int *array = (int *)malloc(INITIAL_SIZE * sizeof(int));
    if(array == NULL) {
        printf("ERROR: Array memory allocation failed.\n");
        free(container);
        container = NULL;
        exit(0);
    }
    container->array = array;
    *container_ptr = container;
}

void insertItem(dynamic_array *container, int item) {
    if(container->size == container->capacity) {
        int *temp = container->array;
        container->capacity <<= 1;
        container->array = (int *)realloc(container->array, container->capacity * sizeof(int));
        if(container->array == NULL) {
            printf("ERROR: Array memory allocation failed.\n");
            container->array = temp;
            return;
        }
    }
    container->array[container->size++] = item;
}

int getItem(dynamic_array *container, int index) {
    if(index >= container->size) {
        printf("ERROR: Index[%d] is out of the container size[%d].\n", index, container->size);
        return -1;
    }
    return container->array[index];
}

void updateItem(dynamic_array *container, int index, int item) {
    if(index >= container->size) {
        printf("ERROR: Index[%d] is out of the container size[%d].\n", index, container->size);
        return;
    }
    printf("Updating item at index[%d] to new value %d\n", index, item);
    container->array[index] = item;
}

void deleteItem(dynamic_array *container, int item) {
    int index = -1;
    for(int i=0; i<container->size; i++) {
        if(container->array[i] == item) {
            index = i;
            break;
        }
    }
    if(index == -1) {
        printf("ERROR: Item %d NOT found in the container. Can't perform deletion.\n", item);
        return;
    }
    printf("Deleting item %d from the container.\n", item);
    for(int i=index+1; i<container->size; i++) {
        container->array[i-1] = container->array[i];
    }
    container->size -= 1;
}

void printArray(dynamic_array *container) {
    printf("Printing current container items:\n");
    for(int i=0; i<container->size; i++) {
        printf("%d ", container->array[i]);
    }
    printf("\n");
}

void freeArray(dynamic_array *container) {
    free(container->array);
    free(container);
    printf("Allocated memory free successfully.\n");
}
 