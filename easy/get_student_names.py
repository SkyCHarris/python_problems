
#! Get Student Names

# Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order

def get_student_names(students):
    value_set = students.values()
    return sorted(value_set)

get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
})