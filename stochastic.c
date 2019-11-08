//
// Created by huannguyen on 06/11/2019.
//
#include <stdio.h>
#include <stdlib.h>
int main(){
    /*
    double first_x[] = {1,1,1,1,1,1};rename file,just for fun :)
    double size_house[] = {30,43,25,51,40,20};
    double floors[] = {3,4,2,4,3,1};
    double rooms[] = {6,8,3,9,5,2};
    */
    double alpha =0.001; //learning rate
    int iteration = 100000; // number of iteration
    double min_cost = 0; //the minimum of cost function
    double best_thetas[4]; // thetas to make the minimum cost function
    double x_value[4][6] = {{1,1,1,1,1,1},{30,43,25,51,40,20},{3,4,2,4,3,1},{6,8,3,9,5,2}}; // 6 rows and 4 columns
    double price[] = {2.5,3.4,1.8,4.5,3.2,1.6}; //y values
    double theta0[] = {0,0,0,0}; //first thetas
    double theta_temp[4]; //temporate array to save thetas
    for (int m = 0; m < iteration; m++) {

        // random
        int index = rand() % 6;
        double x_input[4][1];
        for (int i = 0; i < 4; i++) {
            x_input[i][0] = x_value[i][index];
        }
        double y_input[1]={price[index]};
        // calculate next thetas
        for (int n = 0; n < 4; n++) {
            theta_temp[n]= theta0[n];
        }
        for (int i = 0; i < 4; i++) {
            double temp = 0;
            for (int j = 0; j < 1; j++) {
                double hx = 0;
                for (int k = 0; k < 4; k++) {
                    hx += theta0[k] * x_input[k][j];
                }
                hx -= y_input[j];
                temp += hx * x_input[i][j];
            }
            theta0[i] = theta0[i] - (alpha * temp/6);
        }

        // calculate cost function
        double cost_function = 0;
        for (int l = 0; l < 6; l++) {
            double hx = 0;
            for (int k = 0; k < 4; k++) {
                hx += theta_temp[k] * x_value[k][l];
            }
            hx -= price[l];
            cost_function += hx * hx;
        }
        cost_function = cost_function/12;

        // find minimum cost function
        if(m == 0) {min_cost = cost_function;}
        if(cost_function<min_cost){
            min_cost = cost_function;
            for (int i = 0; i < 4 ; i++) {
                best_thetas[i] = theta_temp[i];
            }
        }
    }
    for (int n = 0; n <4 ; n++) {
        printf("best thetas is:%lf\n",best_thetas[n]);
    }
    printf("minimum cost function is: %lf",min_cost);
    return 0;
}
