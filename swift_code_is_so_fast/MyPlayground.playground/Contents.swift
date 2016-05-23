func longest_word(text: String) -> (String){
    let words = text.characters.split(" ").map { String($0) }
    let longest = words.maxElement({$1.characters.count > $0.characters.count})
    return longest!
}

var my_text = "I don't know which word will be the longest of this sentence, so I will try to find it!"
print("\"\(longest_word(my_text))\" is the longest word in \"\(my_text)\"")


