/**

 Project Name:  Swift code is so fast!
 Task:          8

 This file contains a function that joins strings from
 an array of strings and adds a space between them.

 Gloria Bwandungi, 2016

 */

let strings = ["We", "Heart", "Swift"]

let string = strings.reduce("") {
    if $0 == "" {
        return $1
    } else {
        return $0 + " " + $1
    }
}

print(string)
