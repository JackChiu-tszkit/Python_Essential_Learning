# !/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    count=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.count=Employee.count+1
    def displayCount(self):
        print("Total Employee %d" % Employee.count)
    def displayEmployee(self):
        print("Name:%s" %self.name, "\nSalary:%d" %self.salary)

em1=Employee("Zara", 20000)
em1.displayEmployee()
em1.displayCount()
print("Total employee %d" % Employee.count)
