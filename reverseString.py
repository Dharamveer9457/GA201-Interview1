# Function to return reversed string
def reverseString(str):
    reverse = ""
    for el in str:
        reverse = el + reverse
    return reverse
    
res = reverseString('Python is fun')
print(res)

# Function to find the max salary in the list of employees.
def max_salary_employee(employees):
    max_salary_employee = employees[0]
    max_salary = max_salary_employee.get("salary",0)

    for el in employees:
        salary = el.get("salary",0)
        if salary>max_salary:
            max_salary = salary
            max_salary_employee = el
        
    return max_salary_employ
