# DO NOT MODIFY THE CODE IN THIS FILE
# This file is used to test the implementation of Problem 1
# Tests for Problem 1

import sys
sys.path.append("..")

import os.path
import sys
from  Make_Solution_root import main
import Make_Solution_root
from tud_tests import *

def test_problem_1():

    try:
        exists = os.path.exists("../Make_Solution_root.py")
        assert exists == True
    except:
        sys.exit()

