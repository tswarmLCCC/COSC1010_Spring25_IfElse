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

    set_keyboard_input([5])
    main()
    output = get_display_output()
   #print(output)

    assert output == ["Enter a number between 0 and 23: ", "Too early to get up"]

    assert output[0].lower() == "enter a number between 0 and 23: "

    assert Make_Homework.number == 5

