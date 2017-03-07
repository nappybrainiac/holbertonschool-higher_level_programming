/**

 Project Name:  Swift code is so fast!
 Task:          2
 Other files:   2-main.swift

 This file contains a function that returns the value of
 a factorial of a number provided in 2-main.swift

 Gloria Bwandungi, 2016

 */

 func factorial(N: Int) -> (Int) {
    if (N <= 1) {
        return 1
    }

    return N * factorial(N - 1)
}
