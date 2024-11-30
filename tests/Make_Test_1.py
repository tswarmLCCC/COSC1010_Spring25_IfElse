# DO NOT MODIFY THE CODE IN THIS FILE
# This file is used to test the implementation of Problem 1
# Tests for Problem 1

import sys
sys.path.append("..")
sys.path.append(".")
import os.path
import sys
from  Make_Homework import main
import Make_Homework
from tud_tests import *

def test_problem_1():

    try:
        exists = os.path.exists("./Make_Homework.py")
        assert exists == True
    except:
        sys.exit()

