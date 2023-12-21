def find_total(d):
    total = sum(d.values())
    print("The total marks are:", total)

def find_avg(d):
    total = sum(d.values())
    avg = total / len(d)
    print("The average is:", avg)

def find_max(d):
    print("The Highest mark is : " + str(max(d.values())))

def find_min(d):
    print("The Lowest marks is : "+str(min(d.values())))


def show_modules_marks(d):
    print(d)

def input_semester_data(semester_name):
    semester_data = dict()
    i = 0
    while i < 4: 
        module_name = input(f"Enter the module name for {semester_name} Semester {i + 1}: ")
        if module_name.lower == "x":
            break
        marks = int(input(f"Enter the marks for the module {module_name}: "))
        semester_data[module_name] = marks
        i += 1
    return semester_data

def main():
    years = 4
    semesters_per_year = 4

    for year in range(1, years + 1):
        for semester in range(1, semesters_per_year + 1):
            print(f"Enter data for Year {year} Semester {semester}:")
            data = input_data()
            find_total(data)
            find_avg(data)
            find_max(data)
            find_min(data)
            show_modules_marks(data)

def input_data():
    data = []
    while True:
        module = input("Enter module name (or 'X' to finish): ")
        if module.lower() == 'x':
            break
        marks = int(input("Enter module marks: "))
        data.append((module, marks))
    return data

def find_total(data):
    total = sum(marks for module, marks in data)
    print(f"Total marks: {total}")

def find_avg(data):
    total, count = sum(marks for module, marks in data), len(data)
    avg = total / count if count != 0 else 0
    print(f"Average marks: {avg}")

def find_max(data):
    if data:
        max_module, max_marks = max(data, key=lambda x: x[1])
        print(f"Maximum marks: {max_marks} in {max_module}")
    else:
        print("No data available")

def find_min(data):
    if data:
        min_module, min_marks = min(data, key=lambda x: x[1])
        print(f"Minimum marks: {min_marks} in {min_module}")
    else:
        print("No data available")

def show_modules_marks(data):
    for module, marks in data:
        print(f"{module}: {marks}")

main()