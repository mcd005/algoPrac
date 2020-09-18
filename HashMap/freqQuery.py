
import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    operation3Results =[]
    freq = Counter()

    for query in queries:
        operation = query[0]
        operand = query[1]

        if (operation == 1):
            freq[operand] +=1
        elif (operation == 2 and operand in freq.keys()):
            freq[operand] -= 1
        elif (operation == 3):
            if (operand in freq.values()):
                operation3Results.append(1)
            else:
                operation3Results.append(0)

    return(operation3Results)

