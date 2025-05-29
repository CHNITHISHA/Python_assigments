def simple_logger(task):
    def execute_task(*input_data, **extra_info):
        return task(*input_data, **extra_info)
    return execute_task

student_list = []

@simple_logger
def register_student(*scores, **details):
    new_entry = {
        "student_name": details.get("student_name", "Not Provided"),
        "student_id": details.get("student_id", "None"),
        "score_list": list(scores)
    }
    student_list.append(new_entry)

@simple_logger
def show_results():
    for entry in student_list:
        score_list = entry["score_list"]
        if not score_list:
            print(f"{entry['student_name']} has no scores.")
            continue
        average_score = sum(score_list) / len(score_list)
        print(f"\nStudent Name : {entry['student_name']}")
        print(f"Student ID   : {entry['student_id']}")
        print(f"Scores       : {score_list}")
        print(f"Average      : {average_score:.2f}")

register_student(85, 90, 78, student_name="NITHISHA", student_id="101")
register_student(45, 40, 50, student_name="AMULYA", student_id="102")
register_student(95, 88, 92, student_name="JAANU", student_id="103")

show_results()
