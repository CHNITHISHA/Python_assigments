class Department:
    total_departments = 0

    def __init__(self, dept_id, name, location, head):
        self.dept_id = dept_id
        self.name = name
        self.location = location
        self.head = head
        Department.total_departments += 1

    def display_info(self):
        print(f"Department ID   : {self.dept_id}")
        print(f"Department Name : {self.name}")
        print(f"Location        : {self.location}")
        print(f"Head of Dept    : {self.head}")
        print("-" * 30)


def search_by_id(departments, dept_id):
    for dept in departments:
        if dept.dept_id == dept_id:
            dept.display_info()
            return
    print("Department ID not found.")


def search_by_name(departments, name):
    for dept in departments:
        if dept.name.lower() == name.lower():
            dept.display_info()
            return
    print("Department name not found.")


def main():
    departments = []
    n = int(input("Enter number of departments: "))

    for i in range(n):
        print(f"\nEnter details for Department {i+1}:")
        dept_id = input("Department ID: ")
        name = input("Department Name: ")
        location = input("Location: ")
        head = input("Head of Department: ")
        departments.append(Department(dept_id, name, location, head))

    print("\nAll Departments:")
    for dept in departments:
        dept.display_info()

    print(f"Total Departments: {Department.total_departments}")

    # Search 
    search_id = input("\nEnter Department ID to search: ")
    search_by_id(departments, search_id)

    search_name = input("\nEnter Department Name to search: ")
    search_by_name(departments, search_name)


if __name__ == "__main__":
    main()
