#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    capitalized_words = [w.capitalize() for w in words]
    print(" ".join(capitalized_words)) 

    # return " ".join(capitalized_words) -------------> this would work for standard stdout
   


s = input()
result = solve(s)

 