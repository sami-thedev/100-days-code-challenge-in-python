programming_dictionary ={
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",

}
# print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."



# using loop for dictionaries
for key in programming_dictionary:
  print(key)
  # print(programming_dictionary[key])






# project


# Do not modify the student_scores dictionary
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Create an empty dictionary to store student grades
student_grades = {}

# Convert scores to grades based on the given criteria
for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Final version of student_grades
# print(student_grades)



# dictionary inside the dictionary
travel_di={
  "pakistan":{
    "cities_visited":["lahore","karachi","islamabad"],
    "total_visits":12

  },
  "india":{
    "cities_visited":["mumbai","delhi","chennai"],
    "total_visits":10,
  }
}
print(travel_di["india"]["cities_visited"][2])

travel_log ={
  "pakistan": ["islamabad","Karachi","Peshawar"],
  "india":["delhi","mumbai","chennai"]
}
# print(travel_log["pakistan"][1])


nested_list=["a","b","c",["d","e","f"]]

# print(nested_list[3][1])