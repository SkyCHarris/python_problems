
#! RegEx XV: Alternation

# The vertical bar | is equivalent to 'or' in RegEx.
# The regular expression x|y matches either "x" or "y"
# Write the regular expression that will match all red flag and blue flag in a string
# Must use | in expression
# Flags can come in any order

import re

pattern = re.search("red flag" | "blue flag")