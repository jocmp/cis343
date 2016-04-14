//
//  main.swift
//  csvdump
//
//  Created by Josiah Campbell on 4/10/16.
//

import Foundation

let engine = CsvEngine()

let result = engine.readFile()
var records: [[String]] = []

engine.printRecords(records)

if (result.filename.isEmpty) {
    print("Filename was empty. Enter new record:\n")
    var addMore = true
    var response = ""
    repeat {
        records.append(engine.addRecord())
        print("Record added. Add another? (N)")
        response = readLine()!
        if response.lowercaseString == "n" {
            addMore = false
            break
        }
    } while (addMore)
    
    engine.printRecords(records)
    engine.writeFile("output", engine.recordsToString(records))
} else {
    engine.printRecords(result.newRecords)
}