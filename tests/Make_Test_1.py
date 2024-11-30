# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 1
# Simple Pay Calculator

import os.path
import sys
import Make_Solution
from tud_tests import *

def test_problem_1():

    try:
        exists = os.path.exists("Make_Solution.py")
        assert exists == True
    except:
        sys.exit()

    set_keyboard_input([5])
    main()
    output = get_display_output()
    print(output)
    '''
    assert output == [
            "Simple Pay Program\n",
            "How many hours did you work: ",
            "\nPay Stub",
            "\t\tHours: 5",
            "\t\tRate: $25.00",
            "\t\tPay: $125.00",
            "\t\tTax: $15.62",
            "\t\tNet Pay: $109.38"   
    ]
    '''