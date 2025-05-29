# Define university data
university = {
    "S101": {
        "student_name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "student_name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "student_name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

# Q1: Print all student names and their majors
for student_id in university:
    student = university[student_id]
    print("Name:", student["student_name"], "| Major:", student["major"])

print()

# Q2: Average score per course per student
for student_id, student_info in university.items():
    print("Student ID:", student_id, "| Name:", student_info["student_name"])
    for course_name, scores in student_info["courses"].items():
        avg_score = sum(scores.values()) / len(scores)
        print("Course:", course_name, "| Average Score:", avg_score)
    print()

# Q3: Find students who scored >90 in final of Python101
high_scorers = []
for student in university.values():
    if "Python101" in student["courses"]:
        if student["courses"]["Python101"]["final"] > 90:
            high_scorers.append(student["student_name"])
print("Students scoring >90 in Python101 final:", high_scorers)

print()

# Q4: Add new course AI101 for student S101
university["S101"]["courses"]["AI101"] = {"midterm": 75, "final": 82, "project": 78}
print("Updated S101 data:", university["S101"])

print()

# Q5: Print average for each course
for student_id, student_info in university.items():
    print("Student ID:", student_id, "| Name:", student_info["student_name"])
    for course_name, score_details in student_info["courses"].items():
        avg = sum(score_details.values()) / len(score_details)
        print("Course:", course_name, "| Average:", avg)
    print()
