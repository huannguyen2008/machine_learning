#include <stdio.h>
double next_A(int a,int b, double x[],double y[],int size){
        double alpha = 0.01; //learning rate
        double deri_A = 0;
        for (int i = 0; i < size; i++) {
                deri_A += (a*x[i] + b - y[i])*x[i]; //calculate sum of the derivate
        }
        return a - (alpha*deri_A)/size; //new a
}
double next_B(int a,int b, double x[],double y[],int size){
        double alpha = 0.01; //learning rate
        double deri_B = 0;
        for (int i = 0; i < size; i++) {
                deri_B += (a*x[i] + b - y[i]); //calculate sum of the derivate
        }
        return b - (alpha*deri_B)/size; //new b
}
double cal_E(double a,double b, double x[],double y[],int size){
        double alpha = 0.01; //learning rate
        double square_E = 0;
        for (int i = 0; i < size; i++) {
                square_E +=  (a*x[i] + b - y[i])*(a*x[i] + b - y[i]);
        }
        return square_E/(2*size);
}
int main() {
        double size[] = {30,43,25,51,40,20};
        double price[] = {2.5,3.4,1.8,4.5,3.2,1.6};
        int sizearr= sizeof(size)/ sizeof(size[0]); //calculate size of array
        double a1 =next_A(0,0,size,price,sizearr);
        printf("value of a1 : %lf \n",a1);
        double b1 =next_B(0,0,size,price,sizearr);
        printf("value of b1 : %lf \n",b1);
        printf("value of E with a0 and b0 : %lf \n",cal_E(0,0,size,price,sizearr));
        printf("value of E with a1 and b1 : %lf \n",cal_E(a1,b1,size,price,sizearr));
    return 0;
}
