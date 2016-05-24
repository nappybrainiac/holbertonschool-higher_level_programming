/**

 Project Name:  Swift code is so fast!
 Task:          7
 Other files:   7-main.swift

 This file contains a function that checks whether a number
 is a prime number or not.

 Gloria Bwandungi, 2016

 */

func prime_number(n: Int, i: Int) -> (Bool) {  /* This is the recursive function */

    if(i == 1){   /* When i reaches 1, then it means n is prime */
        return true
    } else if (n % i == 0){  /* If n is divisible by any value of i */
        return false
    }
    return prime_number(n, i: (i - 1))
}

func is_prime(number: Int) -> (Bool){
    if(number == 1){
        return false
    } else if (number < 0){
        return false
    }
    return prime_number(number, i: (number - 1)) /* This calls the recursive function */
}
