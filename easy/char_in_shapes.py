
#! Characters in Shapes

# Create function to calc. how many char. in total needed to make up the shape
# Given a list of strings, makes up a shape in the compiler

def count_characters(lst):
    return sum(len(i) for i in lst)

count_characters([
  "###",
  "###",
  "###"
])