# -*- coding:utf-8 -*-


class SimpleGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = SimpleGradeBook()
book.add_student('Linda')
book.report_grade('Linda', 90)
book.report_grade('Linda', 10)
print(book.average_grade('Linda'))


class BySubjectGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total/count


book = BySubjectGradeBook()
book.add_student('Tom')
book.report_grade('Tom', 'Math', 10)
book.report_grade('Tom', 'Chinese', 40)
book.report_grade('Tom', 'Math', 10)
print(book.average_grade('Tom'))


class WeightedGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                pass
        return score_sum / score_count