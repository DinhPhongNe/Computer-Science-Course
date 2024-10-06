import time

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def total_score(self):
        return sum(self.grades)

class GradeManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, name):
        student = Student(name)
        self.students.append(student)
    
    def record_grade(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)
                print(f"Đã thêm điểm {grade} cho học sinh {name}.")
                return
        print(f"Học sinh {name} không tìm thấy.")
    
    def calculate_average_all(self):
        if not self.students:
            print("Không có học sinh nào.")
            return
        
        total_sum = 0
        total_grades = 0
        for student in self.students:
            total_sum += sum(student.grades)
            total_grades += len(student.grades)
        
        if total_grades == 0:
            print("Không có điểm nào được ghi lại.")
        else:
            average_all = total_sum / total_grades
            print(f"Điểm trung bình của toàn bộ học sinh: {average_all:.2f}")
        return average_all if total_grades != 0 else 0
    
    def save_data(self, filename):
        if not filename.endswith(".txt"):
            filename += ".txt"
        
        with open(filename, 'w', encoding='utf-8') as file:
            total_sum_all = 0
            for student in self.students:
                total_score = student.total_score()
                file.write(f"{student.name}: {total_score:.2f}\n")
                total_sum_all += total_score

            average_all = self.calculate_average_all()
            file.write(f"Tổng điểm trung bình là: {average_all:.2f}")
        
        print(f"Dữ liệu đã được ghi vào {filename}.")

def main_menu():
    manager = GradeManager()
    
    while True:
        print("\n---== Menu ==---")
        print("1. Add a new student")
        print("2. Record a grade for a student")
        print("3. Calculate the average grade of all students")
        print("4. Save the data to a file")
        print("5. Exit")
        
        choice = input("Nhập lựa chọn của bạn (1-5): ")
        
        if choice == '1':
            name = input("Nhập tên học sinh: ")
            manager.add_student(name)
            print(f"Đã thêm học sinh {name}.")
        
        elif choice == '2':
            name = input("Nhập tên học sinh: ")
            try:
                grade = float(input("Nhập điểm: "))
                manager.record_grade(name, grade)
            except ValueError:
                print("Điểm không hợp lệ, vui lòng nhập lại.")
        
        elif choice == '3':
            manager.calculate_average_all()
        
        elif choice == '4':
            filename = input("Nhập tên file để lưu (mặc định là .txt): ")
            manager.save_data(filename)
        
        elif choice == '5':
            print("Thoát khỏi chương trình...")
            time.sleep(2)
            print("Tạm biệt và hẹn gặp lại!")
            break
        
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main_menu()