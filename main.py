class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, exam_scores: list[int] = []):
        # Instance variable
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.exam_scores = exam_scores

    def add_score(self, score):
        self.exam_scores.append(score)

    def show_scores(self):
        print(f"Marks of student {self.first_name} is:", self.exam_scores)

    def score_average(self):
        average_score = 0
        sum_average_score =0
        if len(self.exam_scores) >0:
            for i in self.exam_scores:
                sum_average_score += i
            average_score = sum_average_score/len(self.exam_scores)
            print(f"Average score of the student {self.first_name} is:", average_score)
        else:
            print(f"The student {self.first_name} didn't pass any exam yet")
        pass

    def Course_passed(self):
        count = 0
        for i in self.exam_scores:
            if i > 60:
                count += 1
        if count >= 3:
            print("True")
        else:
            print("False")

if __name__ == '__main__':
    s1 = Student(1, "John", "Doe", [100, 95])
    s2 = Student(2, "Linda", "Jones", [25, 65, 80, 75])
    s3 = Student(3, "Jason", "Kirk", [50, 60, 55])
    s4= Student(4, "Jane", "Doe", [95, 80, 100])
    s5 = Student(5, "Vanessa", "D")
    print(s1.student_id, " ", s1.first_name, " ", s1.last_name, " ", s1.exam_scores)
    print(s2.student_id, " ", s2.first_name, " ", s2.last_name, " ", s2.exam_scores)
    print(s3.student_id, " ", s3.first_name, " ", s3.last_name, " ", s3.exam_scores)
    print(s4.student_id, " ", s4.first_name, " ", s4.last_name, " ", s4.exam_scores)
    print(s5.student_id, " ", s5.first_name, " ", s5.last_name, " ", s5.exam_scores)
    s1.add_score(70)
    s2.add_score(50)
    s3.add_score(80)
    s4.add_score(75)
    s1.show_scores()
    s1.Course_passed()
    s2.show_scores()
    s2.Course_passed()
    s3.show_scores()
    s3.Course_passed()
    s4.show_scores()
    s4.Course_passed()
    s5.show_scores()
    s5.Course_passed()
    s1.score_average()
    s2.score_average()
    s3.score_average()
    s4.score_average()
    s5.score_average()



