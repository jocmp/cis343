//: Playground - noun: a place where people can play

import Cocoa

class Person {
    var residence: Residence?
}

class Residence {
    var numberOfRooms = 1
}

let john = Person()

print(john.residence?.numberOfRooms)

//print(john.residence!.numberOfRooms)

if let roomCount = john.residence?.numberOfRooms {
    print("John's residence has \(roomCount) room(s).")
} else if john.residence?.numberOfRooms == nil {
    print("Unable to retrieve the number of rooms.")
}
// Prints "Unable to retrieve the number of rooms."

var suzy:String? = nil

print(john)

var anotherYou:String

func anotherOne() {
    self.anotherYou = "no"
    var anotherYou: String = "hey"
    anotherYou += "why"
    print(anotherYou)
}

anotherOne()



for index in 1..<Process.arguments.count {
    print(Process.arguments[index])
}