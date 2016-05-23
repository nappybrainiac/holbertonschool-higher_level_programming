/**

 Project Name:  Swift code is so fast!
 Task:          1
 Other files:   1-main.swift

 This file takes a string from 1-main.swift and tests if it is a
 palindrome.

 Gloria Bwandungi, 2016

 */

func is_palindrome(s: String) -> Bool {

    var revstring = ""

    for character in s.characters {
        revstring = String(character) + revstring
    }

    return (revstring.lowercaseString == s.lowercaseString)
}
