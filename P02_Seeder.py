import sqlite3
from faker import Faker

faker = Faker("en_IN")
Faker.seed(43)


def insert_students(count: int):
    with sqlite3.connect("./assignment.db") as conn:
        curr = conn.cursor()

        values = []
        for i in range(count):
            name = faker.name()
            marks = faker.random_int(50, 100)
            values.append(str((name, marks)))

        query = f"INSERT INTO students VALUES {format(', '.join(values))};"

        curr.execute(query)


if __name__ == "__main__":
    insert_students(50)
