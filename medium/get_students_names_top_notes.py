
#! Get Students with Names and Top Notes

# Create function that takes dictionary of objects and returns dictionary of objects with name and top notes

def top_note(student):
    new_dict = {}
    values_list = student.values()
    top_note = max(values_list)
    

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# # Attempt 2

def top_note(student):
    new_dict = {}
    sorted_notes = sorted(student.values())
    print(sorted_notes)

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 3

def top_note(student):
        values_list = student.values()
        sorted_values = values_list.sort()
        print(sorted_values)
        best_note = sorted_values.popitem()
        return {"name", best_note}


top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 4

# get best note
def top_note(student):
     for k, v in student:
          print(k,v)
          
top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 5

def top_note(student):
    for key, value in student.items():
          sorted_values = sorted(value)
          popped = sorted_values.pop()
    print({key[1], popped})
        #   print(popped)

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 6

def top_note(student):
     for key, value in student.items():
          values_wanted = student.values()
          max_note = max(value)
          print(values_wanted, max_note)

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 7

def top_note(student):
    new_dict = {}
    best_note = max(student["notes"])
    new_dict = {student["name"], best_note}
    return new_dict
# Getting weird arrangement of name and top note

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 8

def top_note(student):
    for name, notes in student:
        student[notes] = "top-note"
    return student

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# 1. Takes dictionary of objects
# 2. Gets top-note from "notes" value
# 3. Keeps original "name" values
# 4. Updates "notes" to "top_note"
# 5. Changes "top_note" value to best note

# Attempt 9

def top_note(student):
     best_note = max(student["notes"])
     student = student["name"], best_note
     print(student)
     # gives us tuple with student name and best_note

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 10

def top_note(student):
    for name, notes in student.items(): # .items() fixes unpack error
        sorted_notes = sorted(notes)
        best_note = sorted_notes.pop()
        print(best_note)

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 11

def top_note(student):
     for name, notes in student.items():
          sorted_notes = sorted(notes)
          print(sorted_notes)
        #   student.keys() - 
    
top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 12

def top_note(student):
    for key, value in student.items():
        student_values = student.values()
        best_note = max(student_values)
        print(best_note)

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 13

def top_note(student):
    new_guy = {}
    newest_guy = {}
    sorted_guy = sorted(student["notes"])
    popped_guy = sorted_guy.pop()   # sorts and pops correct value #TODO: Need new dictionary now
    for key in student.keys() - {"notes"}:
        new_guy[key] = student[key]
        newest_guy = {new_guy[key], popped_guy}
    print(newest_guy)
         

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Attempt 14

def top_note(student):
    new_dict = {}
    sorted_guy = sorted(student["notes"])
    popped_guy = sorted_guy.pop()
    student["top-note"] = student["notes"]
    del student["notes"]
    for value in student.values():
         print(student)
    #      student[top_note] = popped_guy #TODO THIS ONE ALMSOT THERE AGDKADSJLKFDS
    # print(student)

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Actual 1

def top_note(student):
    return {"name":student["name"], "top_note": max(student["notes"])}

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Actual 2

def top_note(student):
    return {
         'name': student['name'], 'top_note': max(student['notes'])
    }

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })

# Actual 3

def top_note(student):
	notes_list = student["notes"]
	name = student["name"]
	top_note = max(notes_list)
	
	return {"name":name, "top_note":top_note}

top_note({ "name": "John", "notes": [3, 5, 4] })
top_note({ "name": "Max", "notes": [1, 4, 6] })
top_note({ "name": "Zygmund", "notes": [1, 2, 3] })