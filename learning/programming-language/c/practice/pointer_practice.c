/*
 * practice.c
 * Pointer practice pack for interview refresh:
 * - pointers
 * - arrays + pointers
 * - char arrays + pointers
 * - 2D/3D arrays + pointer arithmetic
 * - const pointers
 * - malloc/free
 * - structs + struct pointers
 * - raw buffer parsing (telecom-relevant)
 *
 * Compile:
 *   gcc -O0 -g pointer_practice.c -o pointer_practice
 * Run:
 *   ./pointer_practice
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

/* ============================================================
 * TASK 1: Pointer basics
 * ============================================================ */
void update(int *p) {
    // 1) print address of pointer variable p (i.e., &p)
    // 2) print address stored in p (i.e., p)
    // 3) print value pointed by p
    // 4) increment *p by 10
    printf("Address of local p : %p\n", &p);
    printf("Address stored in p : %p\n", p);
    printf("Value pointed by p : %d\n", *p);
    *p += 10;
}

/* ============================================================
 * TASK 2: Swap using pointers
 * ============================================================ */
void swap_int(int *a, int *b) {
    // swap values
    int temp = *a;
    *a = *b;
    *b = temp;
}

/* ============================================================
 * TASK 3: Sum array using pointer arithmetic only
 * ============================================================ */
int sum_array(int *arr, int n) {
    // Use pointer arithmetic, not arr[i]
    int sum = 0;
    for(int i=0; i<n; i++) {
        sum += *(arr+i);
    }
    return sum;
}

/* ============================================================
 * TASK 4: Return pointer to max element
 * ============================================================ */

int* max_ptr(int *arr, int n) {
    // Return pointer to FIRST max element
    if (n <= 0) return NULL;

    int *max = arr;

    for(int i=1;i<n;i++) {
        if(arr[i] > *max)
            max = &arr[i];
    }
    return max;
}


/* ============================================================
 * TASK 5: Reverse int array in-place using pointers
 * ============================================================ */
void reverse_int_array(int *arr, int n) {
    // Use two pointers: left and right
    int *left = arr, *right = arr + n - 1;
    while(left < right) {
        swap_int(left, right);
        left++;
        right--;
    }
}

/* ============================================================
 * TASK 6: Custom strlen using char* only
 * ============================================================ */
size_t my_strlen(const char *s) {
    // implement using pointer increment
    size_t len = 0;
    while(*s != '\0') {
        s++;
        len++;
    }
    return len;
}

/* ============================================================
 * TASK 7: Custom strcpy (assume dst has enough space)
 * ============================================================ */
void my_strcpy(char *dst, const char *src) {
    // copy including '\0'
    while (*src) {
        *dst++ = *src++;
    }
    *dst = '\0';
}

/* ============================================================
 * TASK 8: Reverse string in-place using pointers
 * ============================================================ */
void reverse_str(char *s) {
    // TODO:
    // Reverse characters of string in-place
    char *left = s, *right = s + my_strlen(s) - 1;
    while(left < right) {
        char temp = *left;
        *left = *right;
        *right = temp;
        left++;
        right--;
    }
}

/* ============================================================
 * TASK 9: Char array vs char pointer demo
 * ============================================================ */
void demo_char_array_vs_pointer() {
    char arr[] = "hello";
    const char *ptr = "hello";

    printf("\n[TASK 9] Char array vs pointer\n");
    printf("arr=\"%s\", sizeof(arr)=%zu\n", arr, sizeof(arr));
    printf("ptr=\"%s\", sizeof(ptr)=%zu\n", ptr, sizeof(ptr));

    // Modify arr[0] = 'H';
    // Print arr again.
    arr[0] = 'H';
    printf("arr[modified]=\"%s\"\n", arr);
    // DO NOT modify ptr[0] (string literal) - UB.
    // Instead just add a comment explaining why.
    // ptr[0] = 'C';   // error: read-only variable is not assignable
}

/* ============================================================
 * TASK 10: Print 2D matrix using pointer arithmetic
 * ============================================================ */
void fill2D(int a[3][4]) {
    int val = 1;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            a[i][j] = val++;
        }
    }
}

void print2D(int (*p)[4], int rows) {
    // Print matrix without using p[i][j]
    // p is a pointer to an array of 4 integer, instead of the first element of the array
    printf("sizeof(p)=%zu, sizeof(*p)=%zu\n", sizeof(p), sizeof(*p));
    // p+1 will point to the next address after 4 integer
    // Use *(*(p+i) + j)
    for(int i=0; i<rows; i++) {
        for(int j=0; j<4; j++) {
            printf("%d\t", *(*(p+i)+j));
        }
        printf("\n");
    }
}

/* ============================================================
 * TASK 11: Row sum for 2D matrix
 * ============================================================ */
void row_sum(int (*p)[4], int rows, int *out) {
    // out[i] = sum of row i
    for(int i=0; i<rows; i++) {
        for(int j=0; j<4; j++) {
            out[i] += *(*(p+i) + j);
        }
    }
}

/* ============================================================
 * TASK 12: 3D get element using pointer
 * ============================================================ */
int get3D(int (*p)[3][4], int i, int j, int k) {
    // Access using pointer arithmetic and return
    // *(p+i) -> i-th 2-D matrix
    // *(*(p+i) + j) -> j-th row of i-th 2-D matrix
    // *((*(*(p+i) + j)) + k) -> p[i][j][k]
    return *(*(*(p+i) + j) + k);
}

/* ============================================================
 * TASK 13: const pointer variations demo
 * ============================================================ */
void demo_const_pointers() {
    printf("\n[TASK 13] const pointer variations\n");

    int x = 10;
    int y = 20;

    const int *p1 = &x;      // pointer to const int
    int *const p2 = &x;      // const pointer to int
    const int *const p3 = &x; // const pointer to const int

    // Uncomment and mark valid/invalid lines:
    p1 = &y;         // valid
    // *p1 = 99;        // invalid

    // p2 = &y;         // invalid
    *p2 = 99;        // valid

    // p3 = &y;         // invalid
    // *p3 = 99;        // invalid

    printf("x=%d y=%d\n", x, y);
}

/* ============================================================
 * TASK 14: const correctness function signatures
 * ============================================================ */
int sum_const(const int *arr, int n) {
    int sum = 0;
    for(int i=0; i<n; i++) {
        sum += *(arr+i);
    }
    return sum;
}

void fill(int *const arr, int n) {
    // fill arr[i] = i
    for(int i=0; i<n; i++) {
        *(arr+i) = i;
    }
}

void print_const(const int *const arr, int n) {
    // print array values
    for(int i=0; i<n; i++) {
        printf("%d ", *(arr+i));
    }
    printf("\n");
}

/* ============================================================
 * TASK 15: malloc/free array creation
 * ============================================================ */
int* create_array(int n) {
    // allocate n ints (malloc)
    int *arr = (int*) malloc(n * sizeof(int));
    if (!arr) return NULL;
    // fill i*i
    for(int i=0; i<n; i++) {
        *(arr+i) = i*i;
    }
    // return pointer
    return arr;
}

/* ============================================================
 * TASK 16: Dynamic 2D allocation with contiguous memory
 * ============================================================ */
int** alloc2D(int rows, int cols) {
    // Allocate:
    // 1) int* block = malloc(rows*cols*sizeof(int))
    // 2) int** m = malloc(rows*sizeof(int*))
    // 3) m[i] = block + i*cols
    int **m = (int**) malloc(rows * sizeof(int*));
    if (!m) return NULL;
    
    int *data = (int*) malloc(rows * cols * sizeof(int));
    if (!data) {
        free(m);
        return NULL;
    }
    
    for (int i = 0; i < rows; i++) {
        m[i] = data + i * cols;
    }
    return m;
}

void free2D(int **m) {
    // free block first then free pointer array
    if (!m) return;

    free(m[0]); // data block
    free(m);    // pointer array
}

/* ============================================================
 * TASK 18-20: struct + pointer
 * ============================================================ */
struct User {
    int id;
    char name[32];
    int groupId;
};

struct User* create_user(int id, const char *name, int groupId) {
    // malloc struct User
    // assign fields safely (strncpy)
    // return pointer
    struct User* user = (struct User*) malloc(sizeof(struct User));
    user->id = id;
    strncpy(user->name, name, sizeof(user->name) - 1);
    user->name[sizeof(user->name) - 1] = '\0';
    user->groupId = groupId;
    // snprintf(user->name, sizeof(user->name), "%s", name);
    return user;
}

void destroy_user(struct User *u) {
    free(u);
}

void print_users(struct User *u, int n) {
    // traverse using pointer arithmetic (u++)
    for(int i=0; i<n; i++) {
        printf("User{%d} : id=%d, name=%s, groupId=%d\n", i+1, u->id, u->name, u->groupId);
        u++;
    }
}

/* ============================================================
 * TASK 21: Packet-like header parsing
 * ============================================================ */
struct Header {
    uint16_t type;
    uint16_t len;
    uint32_t seq;
};

static uint16_t read_u16_be(const uint8_t *p) {
    // big-endian to host
    return (uint16_t)((p[0] << 8) | (p[1]));
}

static uint32_t read_u32_be(const uint8_t *p) {
    return ((uint32_t)p[0] << 24) |
           ((uint32_t)p[1] << 16) |
           ((uint32_t)p[2] << 8)  |
           ((uint32_t)p[3]);
}

int parse_header(const uint8_t *buf, int size, struct Header *out) {
    // Header format:
    // [type:2 bytes][len:2 bytes][seq:4 bytes] => total 8 bytes

    // Validate size >= 8
    // Fill out->type, out->len, out->seq (use read_u16_be/read_u32_be)
    // return 0 on success else -1
    if(size < 8) return -1;
    out->type = read_u16_be(buf);
    out->len = read_u16_be(buf + 2);
    out->seq = read_u32_be(buf + 4);
    return 0;
}

/* ============================================================
 * MAIN: Runs tasks
 * ============================================================ */
int main() {
    printf("=== POINTER PRACTICE PACK ===\n");

    /* Task 1 */
    printf("\n[TASK 1] update()\n");
    int x = 5;
    printf("Before: x=%d, &x=%p\n", x, (void*)&x);
    update(&x);
    printf("After : x=%d\n", x); // expected 15

    /* Task 2 */
    printf("\n[TASK 2] swap_int()\n");
    int a = 10, b = 20;
    printf("Before: a=%d b=%d\n", a, b);
    swap_int(&a, &b);
    printf("After : a=%d b=%d (expected a=20 b=10)\n", a, b);

    /* Task 3 */
    printf("\n[TASK 3] sum_array()\n");
    int arr[] = {1,2,3,4,5};
    printf("sum=%d (expected 15)\n", sum_array(arr, 5));

    /* Task 4 */
    printf("\n[TASK 4] max_ptr()\n");
    int arr2[] = {4,9,2,9,1};
    int *mx = max_ptr(arr2, 5);
    if (mx) {
        printf("max=%d, index=%ld (expected max=9 index=1)\n",
               *mx, (long)(mx - arr2));
    }

    /* Task 5 */
    printf("\n[TASK 5] reverse_int_array()\n");
    int arr3[] = {1,2,3,4,5};
    reverse_int_array(arr3, 5);
    printf("reversed: ");
    for(int i=0;i<5;i++) printf("%d ", arr3[i]);
    printf("(expected 5 4 3 2 1)\n");

    /* Task 6 */
    printf("\n[TASK 6] my_strlen()\n");
    printf("len(\"hello\")=%zu (expected 5)\n", my_strlen("hello"));

    /* Task 7 */
    printf("\n[TASK 7] my_strcpy()\n");
    char dst[32];
    my_strcpy(dst, "ajay");
    printf("dst=%s (expected ajay)\n", dst);

    /* Task 8 */
    printf("\n[TASK 8] reverse_str()\n");
    char s[] = "abcde";
    reverse_str(s);
    printf("reverse=%s (expected edcba)\n", s);

    /* Task 9 */
    demo_char_array_vs_pointer();

    /* Task 10 */
    printf("\n[TASK 10] print2D()\n");
    int mat[3][4];
    fill2D(mat);
    print2D(mat, 3);

    /* Task 11 */
    printf("\n[TASK 11] row_sum()\n");
    int out[3] = {0};
    row_sum(mat, 3, out);
    printf("Row sums: %d %d %d (expected 10 26 42)\n", out[0], out[1], out[2]);

    /* Task 12 */
    printf("\n[TASK 12] get3D()\n");
    int cube[2][3][4];
    int v = 1;
    for(int i=0;i<2;i++)
        for(int j=0;j<3;j++)
            for(int k=0;k<4;k++)
                cube[i][j][k] = v++;
    printf("cube[1][2][3]=%d (expected 24)\n", get3D(cube, 1, 2, 3));

    /* Task 13 */
    demo_const_pointers();

    /* Task 14 */
    printf("\n[TASK 14] const correctness\n");
    int tmp[5];
    fill(tmp, 5);
    printf("sum_const=%d (expected 10)\n", sum_const(tmp, 5));
    print_const(tmp, 5);

    /* Task 15 */
    printf("\n[TASK 15] create_array()\n");
    int *dyn = create_array(6);
    if (dyn) {
        printf("dyn squares: ");
        for(int i=0;i<6;i++) printf("%d ", dyn[i]);
        printf("(expected 0 1 4 9 16 25)\n");
        free(dyn);
    }

    /* Task 16 */
    printf("\n[TASK 16] alloc2D()/free2D()\n");
    int **m = alloc2D(3, 4);
    if (m) {
        int val2 = 1;
        for(int i=0;i<3;i++)
            for(int j=0;j<4;j++)
                m[i][j] = val2++;

        printf("Dynamic 2D:\n");
        for(int i=0;i<3;i++){
            for(int j=0;j<4;j++)
                printf("%d ", m[i][j]);
            printf("\n");
        }
        free2D(m);
    }

    /* Task 18-20 */
    printf("\n[TASK 18-20] struct User\n");
    struct User *u1 = create_user(1, "Ajay", 101);
    struct User *u2 = create_user(2, "Vivek", 102);
    struct User *u3 = create_user(3, "Rahul", 101);

    if (u1 && u2 && u3) {
        struct User users[3];
        users[0] = *u1;
        users[1] = *u2;
        users[2] = *u3;

        print_users(users, 3);
    }
    destroy_user(u1);
    destroy_user(u2);
    destroy_user(u3);

    /* Task 21 */
    printf("\n[TASK 21] parse_header()\n");
    uint8_t buf[] = {0x00,0x02, 0x00,0x10, 0x00,0x00,0x00,0x05}; // type=2, len=16, seq=5
    struct Header h;
    if (parse_header(buf, sizeof(buf), &h) == 0) {
        printf("type=%u len=%u seq=%u (expected 2 16 5)\n",
               h.type, h.len, h.seq);
    } else {
        printf("parse_header failed\n");
    }

    printf("\n=== DONE ===\n");
    return 0;
}
