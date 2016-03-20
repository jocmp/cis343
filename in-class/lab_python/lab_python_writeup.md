CIS 343<br>Josiah Campbell<br>Object Oriented Python Lab

1. Code entered in file
2. Program output:<br>`<__main__.Student instance at 0x1015b9cb0>`
3. The printed representation is an address in memory for the student object Joey.
4. `name` and `gpa` are explicitly passed parameters. Python implicitly passes the `self` parameter. Instantiating an object without the correct number of parameters returns a TypeError like so:<br>`TypeError: __init__() takes exactly 3 arguments (2 given)`
5. The output now is `Joey Coder: 4.0`
6. A publicly accessable counter might lead to modification. If someone were to change the value of the counter without creating a student, the counter is no longer meaningful.
7. The output after changing the counter scope:  
```
Traceback (most recent call last):
  File "student.py", line 12, in <module>
    joey = Student('Joey Coder', 4.0)
  File "student.py", line 7, in __init__
    Student.num_students += 1
AttributeError: class Student has no attribute 'num_students'
```
8. Using a main method helps display the actual flow of a program, as opposed to
inlining function calls.
