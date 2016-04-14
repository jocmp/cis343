//
//  engine.swift
//  csvdump
//
//  Created by Josiah Campbell on 4/12/16.
//

// Use of modules
import Foundation

class CsvEngine {
    
    private let headerFields: [String] = ["First name", "Last name", "Phone", "City"]
    
    // No parameters, but "->" designates return tuple
    func readFile() -> (filename: String, newRecords: [[String]]) {
        var readCsv: String = ""
        var filename: String
        print("Enter filename")
        // Optional unwrapping
        filename = readLine()!
        
        do {
            try readCsv = NSString(contentsOfFile: filename, encoding: NSUTF8StringEncoding) as String
        } catch {
            print("Trouble loading file: \(filename)")
            return ("", [])
        }
        return (filename, stringToRecords(readCsv))
    }
    
    func writeFile(filename: String, _ data: String) -> Bool {
        do {
            try data.writeToFile("\(filename).csv", atomically: true, encoding: NSUTF8StringEncoding)
        } catch {
            // failed to write file – bad permissions, bad filename
            return false
        }
        return true
    }
    
    func stringToRecords(let csvFromFile: String) -> [[String]] {
        // Separate each row
        let separatedRows: [String] = csvFromFile.componentsSeparatedByString("\n")
        var newRecords: [[String]] = []
        for person in separatedRows {
            // Split into individual arrays, and append to newRecords
            newRecords.append(person.componentsSeparatedByString(","))
        }
        return newRecords
    }
    
    func recordsToString(records:[[String]]) -> String {
        // fileData must be assigned before data can be appended to it
        var fileData: String = ""
        // Store people
        for record in records {
            for field in record {
                fileData += field + ","
            }
            fileData += "\n"
        }
        return fileData
    }
    
    func printRecords(records:[[String]]) {
        // Print people
        for record in records {
            for i in 0...3 {
                print("\(headerFields[i]): \(record[i])")
            }
            print("\n")
        }
    }
    
    func addRecord() -> [String] {
        var row: [String] = []
        var currentField = ""
        
        for fieldName in headerFields {
            print("Enter \(fieldName)")
            currentField = readLine()!
            row.append(currentField)
        }
        return row
    }
}