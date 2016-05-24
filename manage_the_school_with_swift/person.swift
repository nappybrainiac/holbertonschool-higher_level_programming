/**

 Project Name:  Manage the school with Swift
 Task:          0, 1, 2, 3, 4
 Other files:   6-main.swift

 This file contains a function that reverses the array provided
 in 6-main.swift.

 Gloria Bwandungi, 2016

 */

protocol Classify{
    func isStudent() -> Bool
}

class Person {

    var first_name: String
    var last_name: String
    var age: Int

    init(first_name: String, last_name: String, age: Int){
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }

    func fullName() -> String{
        return first_name + " " + last_name
    }
}

class Mentor: Person, Classify {

    func isStudent() -> Bool{
        return false
    }

}

class Student: Person, Classify {

    func isStudent() -> Bool{
        return true
    }

}
