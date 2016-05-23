/**

 Project Name:  Swift code is so fast!
 Task:          3
 Other files:   3-main.swift

 This file contains a function that returns the longest
 word in a string provided by 3-main.swift.

 Gloria Bwandungi, 2016

 */

func longest_word(text: String) -> (String){
    let words = text.characters.split(" ").map { String($0) }
    let longest = words.maxElement({$1.characters.count > $0.characters.count})
    return longest!
}
