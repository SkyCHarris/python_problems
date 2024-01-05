
#! RegEx XV: Alternation

import re

txt1 = "red flag blue flag"
txt2 = "yellow flag red flag blue flag green flag"



x = re.findall(('red flag' | 'blue flag'), txt2)
print(x)

# Attempt 2

import re

pattern = re.compile(r'\b(?:red|blue) flag\b')

# Attempt 3

re.findall('red flag | blue flag')

# Actual

pattern = 'red flag | blue flag'
