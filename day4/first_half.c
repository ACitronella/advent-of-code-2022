#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(){
    int a, b, c, d, s, overlap = 0;
    FILE *fp = fopen("input.txt", "r");

    while(true){
        s = fscanf(fp, "%d-%d,%d-%d", &a, &b, &c, &d); // im no expert in C. Literally have no idea how bad this is.
        if(s == -1) break; // when next line don't match with format anymore
        overlap += (a <= c && d <= b) || (c <= a && b <= d); // (a...c...d...b) || (c...a...b...d)
    }
    printf("%d\n", overlap);

    fclose(fp);
    return 0;
}