def calculate_gpa():
    num_courses = int(input("Enter the number of courses: "))
    
    total_credits = 0
    total_grade_points = 0
    
    for i in range(num_courses):
        credits = int(input("Enter credits for course {}: ".format(i+1)))
        grade = float(input("Enter result (grade) for course {}: ".format(i+1)))
        
        total_credits += credits
        total_grade_points += credits * grade
        
    gpa = total_grade_points / total_credits
    return gpa

def main():
    print("GPA Calculator")
    print("------------------")
    gpa = calculate_gpa()
    print("------------------")
    print("GPA: {:.2f}".format(gpa))


if __name__=='__main__':
    main()