/**

 Project Name:  Swift code is so fast!
 Task:          5
 Other files:   5-main.swift

 This file contains a function that returns the fibonacci number
 provided in 5-main.swift.

 Gloria Bwandungi, 2016

 */

func fibonacci(number: Int) -> (Int){
    if number == 0{                                       //special case for 0
        return 0
    }else if number == 1{                                     //special case for 1
        return 1
    }else if number > 1{
        return (fibonacci(number - 2) + fibonacci(number - 1)) //for +ve values of n
    }else if number == -1{                                    //special case for -1
        return 1
    }
    return (fibonacci(number + 2) - fibonacci(number + 1)) //for -ve values of n
}
