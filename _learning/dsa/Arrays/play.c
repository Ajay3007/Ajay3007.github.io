#include<stdio.h>

int x = 0;

int f1() {
    x = 5;
    return x;
}

int f2() {
    x = 10;
    return x;
}

int main() {
    int a = f1()+f2();
    printf("%d\n", x);
    return 0;
}

/**
 * 
 * Output Explanation:
 * The output of the program is 10. This is because the order of function calls in the expression f1() + f2() is not guaranteed.
 * The compiler may choose to evaluate f2() before f1(), resulting in x being set to 10 last.
 * Therefore, the final value of x printed is 10.
 * 
 * Note: The behavior of this code is undefined according to the C standard, as it modifies and accesses the variable 'x' without a sequence point in between.
 * Different compilers or optimization settings may yield different results.
 * 
 */