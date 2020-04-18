#include <stdio.h>
#define PI 3.14159265359

int main(){
    int T,t;
    scanf("%d",&T);

    for(t=0;t<T;t++){
        float radius;
        scanf("%f",&radius);
        float area=PI*radius*radius;
        printf("Case %d: %0.3f\n",t,area);
    }
    return 0;
}
