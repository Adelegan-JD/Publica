# This file handles storing and retrieving student data

students = []

def add_student(name, track):
    students.append({"Name": name, "Track": track})

def get_students():
    return students