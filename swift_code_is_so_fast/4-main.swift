/**

 Project Name:  Swift code is so fast!
 Task:          2
 Other files:   2-main.swift

 This file contains a function that returns the value of
 a factorial of a number provided in 2-main.swift

 Gloria Bwandungi, 2016

 */

 let numbers = [4, 7, 1, 9, 6, 5, 6, 9]

let max = numbers.reduce(numbers[0]) {
    if $0 > $1 {
        return $0
    } else {
        return $1
    }
}

print(max)
