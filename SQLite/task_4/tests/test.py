from pathlib import Path
import sys
import unittest

module_path = Path(__file__).parents[1]
sys.path.append(str(module_path))
from main import sqlite_pythonDB, Student, Course, StudentCourse