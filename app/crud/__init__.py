from .base import BaseCRUD
from .teacher import TeacherCRUD
from .course import CourseCRUD
from .classes import ClassCRUD
from .yearcourses import YearCoursesCRUD
from .student import StudentCRUD
from .parent import ParentCRUD
from .parenttostudent import ParentToStudentCRUD
from .lesson import LessonCRUD

teacher = TeacherCRUD()
course = CourseCRUD()
classes = ClassCRUD()
yearcourses = YearCoursesCRUD()
student = StudentCRUD()
parent = ParentCRUD()
parenttostudent = ParentToStudentCRUD()
lesson = LessonCRUD()