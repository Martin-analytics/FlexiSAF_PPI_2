

class StudentGradeCalculator:
    
    # Constructor
    def __init__(self):
        self.test_score = 0
        self.assignment_score = 0
        self.exam_score = 0
        
    # Encapsulator
    def collect_score(self):
        self.test_score = self.get_test_score()
        self.assignment_score = self.get_assignment_score()
        self.exam_score = self.get_exam_score()
        
    # Getters
    def get_test_score(self):
        while True:
            test_score = input("1. Enter Test Score: \n")
            test_score = self.valid_test_score(test_score)
            if test_score:
                return float(test_score)
    
    def get_assignment_score(self):
        while True:
            assignment_score = input("2. Enter Assignment Score: \n")
            assignment_score = self.valid_assignment_score(assignment_score)
            if assignment_score: 
                return float(assignment_score)
    
    def get_exam_score(self):
        while True:
            exam_score = input("3. Enter Exam Score: \n")
            exam_score = self.valid_exam_score(exam_score)
            if exam_score:
                return float(exam_score)
    
    # Validators
    def general_validator(self, data):
        data = data.strip()

        if data == "":
            print("Input cannot be empty!\n")
            return None
        try:
            num_data = float(data)
            return num_data
        except ValueError:
            print("Input must be numeric!\n")
            return None
    
    def valid_test_score(self, data):
        num_data = self.general_validator(data)
        if num_data is not None and 0 <= num_data <= 20:
            return num_data
        else:
            print("Invalid Test Score! Try again...\n")
            return None
    
    def valid_assignment_score(self, data):
        num_data = self.general_validator(data)
        if num_data is not None and 0 <= num_data <= 10:
            return num_data
        else:
            print("Invalid Assignment Score! Try again...\n")
            return None
    
    def valid_exam_score(self, data):
        num_data = self.general_validator(data)
        if num_data is not None and 0 <= num_data <= 70:
            return num_data
        else:
            print("Invalid Exam Score! Try again...\n")
            return None
    
    # Arithmetic Operations
    def total_score(self, data_1, data_2, data_3):
        total_score = data_1 + data_2 + data_3
        return total_score
    
    def average_score(self, data):
        average_score = data / 100
        return average_score
    
    # Comparison Operation
    def result_evaluation(self, data):
        if data >= 50:
            return "Passed"
        else: 
            return "Failed"
    
    def remark(self, data_1, data_2):
        if data_1 == "Passed" and data_2 >= 90:
            return "Excellent Performance!"
        elif data_1 == "Passed" and 70 <= data_2 < 90:
            return "Good Performance! Keep it up"
        elif data_1 == "Passed" and 50 <= data_2 < 70:
            return "Keep Improving!"
        else:
            return "Improve!"
    
    # Logical Conditions
    def award_qualify(self, data):
        if data == "Excellent Performance!":
            return "Yes"
        else:
            return "No"
    
    # Display Result
    def display_result(self):
        total = self.total_score(
            self.test_score,
            self.assignment_score,
            self.exam_score
            )

        average = self.average_score(total)
        status = self.result_evaluation(total)
        remark = self.remark(status, total)
        award = self.award_qualify(remark)
        
        print("\n===== Result =====")
        print(f"- Total Score: {total}")
        print(f"- Average Score: {average:.2f}")
        print(f"- Status: {status}")
        print(f"- Qualified for Award: {award}")
        print(f"- Remark: {remark}")

# Run file
def main():
    student = StudentGradeCalculator()
    student.collect_score()
    student.display_result()
    
if __name__ == "__main__":
    main()