cmake_minimum_required(VERSION 3.15)
project(machine_learning C)

set(CMAKE_C_STANDARD 99)

add_executable(machine_learning gradient.c batch_learning.c stochastic.c minibatch.c)