//: Playground - noun: a place where people can play

import Cocoa

print("hello, world")

// constant
let myConstant = 42

// variable
var myVariable = 50

let implicitInteger = 70
let implicitDouble = 79.0
let explicitDouble: Double = 70
let explicitFloat: Float = 79

let label = "The width is "
let width = 94
let widthLabel = label + String(width)

let vegetable = "red pepper"

switch vegetable {
    case "celery":
        print("Add some raisins and make ants on a log.")
    case "cucumber", "watercress":
        print("That would make a good tea sandwich.")
    case let x where x.hasSuffix("pepper"):
        print("Is it a spicy \(x)?")
    default:
        print("Everything tastes good in soup.")
}

let veggies = ["carrot" : 1, "tomato" : 1, "celery" : 0, "pepper" : 1]

let asparaus = "asparagus"

for (veggie, quality) in veggies {
    if quality == 0 {
        print (veggie + " is bad")
    } else {
        print (veggie + " is good")
    }
}

class Vegetable {
    
    private static var count: Int = 0
    private var notClassCount: Int = 0
    
    init() {
        Vegetable.count += 1
        notClassCount += 1
    }
    
    func getCount() -> Int {
        return Vegetable.count
    }
    
    func getNotClassCount() -> Int {
        return notClassCount
    }
    
    deinit {
        Vegetable.count -= 1
    }
}

var banana = Vegetable()
var pineapple = Vegetable()
var eggplant = Vegetable()

pineapple.getCount()
banana.getNotClassCount()


func getDocumentsDirectory() -> NSString {
    let paths = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)
    let documentsDirectory = paths[0]
    return documentsDirectory
}

var people = "First Name, Last Name, City, Phone\nLizzie,Benson,6165008000,Mount Pleasant\nBarack,Obama,9994001000,Washington DC\nJosiah,Campbell,1008009000,Allendale"
//
let filename = getDocumentsDirectory().stringByAppendingPathComponent("output.csv")

do {
    try people.writeToFile(filename, atomically: true, encoding: NSUTF8StringEncoding)
} catch {
    // failed to write file – bad permissions, bad filename, missing permissions, or more likely it can't be converted to the encoding
}

var readCsv = try NSString(contentsOfFile: filename, encoding: NSUTF8StringEncoding) as String

var recordSeparatedPeople = readCsv.componentsSeparatedByString("\n")

var commaSeparatedPeople: [[String]] = []

for person in recordSeparatedPeople {
    commaSeparatedPeople.append(person.componentsSeparatedByString(","))
}

// Print people
for record in commaSeparatedPeople {
    for field in record {
        print(field, terminator: "\t")
    }
    print("", terminator: "\n")
}

// Store people
for person in commaSeparatedPeople {
    
}

func getUserInput(message: String) -> String {
    print("Please enter \(message.uppercaseString)")
    let input: String? = readLine()
    return input ?? ""
}

var yoyoyo: String

yoyoyo = getUserInput("First name")

print(yoyoyo.isEmpty ? "nothing to see here" : yoyoyo)

let strTuple: (firstName: String, lastName: String) = ("Josiah", "Campbell")

print("Hello, my name is \(strTuple.lastName), \(strTuple.firstName)")

7 == "7"
7 === "7"
7 == 7.0
7 === 7.0

