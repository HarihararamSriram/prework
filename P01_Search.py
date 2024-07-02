import sqlite3
from typing import List, Tuple


class Student:
    name: str
    marks: int

    def __init__(self, name: str, marks: int) -> None:
        self.name = name
        self.marks = marks
        pass


def search(name: str) -> List[Student]:
    with sqlite3.connect("./assignment.db") as conn:
        curr = conn.cursor()
        rows: List[Tuple[str, int]] = curr.execute(
            f"SELECT * FROM students WHERE name LIKE ?", (f'%{name}%',)).fetchall()

        results: List[Student] = [
            Student(name=row[0], marks=row[1]) for row in rows]

        return results


if __name__ == "__main__":
    name = ''
    while True:
        name = str(input('Enter the name of the student: ')).strip()
        if (len(name) > 0):
            break
        print("Please enter a search string\n")

    req_students = search(name)

    if (len(req_students) == 0):
        print("Oops! No students present that match the search text")

    else:
        print("{:20} | {}".format("Name", "Marks"))
        for req_student in req_students:
            print("{:20} | {}".format(
                req_student.name, req_student.marks, sep="\t\t|"))
        print("\n=====\n")

        total_score = sum([student.marks for student in req_students])
        average_score = round(total_score/len(req_students), 2)
        print(f"Total Score: {total_score}", f"Average Score: {average_score}")
