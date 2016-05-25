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

enum Subject {
    case Math
    case English
    case French
    case History
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

    func className() -> String {
        return "Person"
    }
}

class Mentor: Person, Classify {

    override func className () -> String {
		return "Mentor"
    }

    let subject: Subject


    init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
        self.subject = subject
        super.init(first_name: first_name, last_name: last_name, age: age)
    }

    func stringSubject() -> String {
        if self.subject == Subject.Math{
            return "Math"
        }
        if self.subject == Subject.English{
            return "English"
        }
        if self.subject == Subject.French{
            return "French"
        }
        if self.subject == Subject.History{
            return "History"
        }
    return "String"
    }

    func isStudent() -> Bool{
        return false
    }

}

class Student: Person, Classify {

    override func className () -> String {
		return "Student"
    }

    func isStudent() -> Bool{
        return true
    }

}


class School {

	var name: String
	var list_persons: [Person]


	init(name: String) {
		self.name = name
		self.list_persons = []
	}


	func addStudent(p: Person) -> Bool {
		if p.className() == "Student" {
			self.list_persons.append(p)
			return true
		}
		return false
	}

	func addMentor(p: Person) -> Bool {
		if p.className() == "Mentor" {
			self.list_persons.append(p)
			return true
		}
		return false
	}

    func listStudents() -> [Person] {
        var students = self.list_persons.filter {($0 is Student)}
        students.sortInPlace {($0.age > $1.age)}
        return students
    }

    func listMentors() -> [Person] {
        var mentors = self.list_persons.filter {($0 is Mentor)}
        mentors.sortInPlace {($0.age > $1.age)}
        return mentors
    }

    func listMentorsBySubject(subject: Subject) -> [Person] {
        let mentors = self.listMentors() as! [Mentor]
        let mentorsBySubject: [Mentor] = mentors.filter { (mentor: Mentor) -> Bool in
            mentor.subject == subject
        }
        return mentorsBySubject
    }
}
