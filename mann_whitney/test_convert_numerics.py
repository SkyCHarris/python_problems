import pandas as pd

data1 = {'Mathscore': ['strong', 'strong', 'weak', 'weak', 'strong']}
data2 = {'weak', 'strong', 'strong', 'weak'}

df = pd.DataFrame(data1)

#TODO: Convert string literal into numeric value
# Iterate through and assign values
# Assign function on top of it

# Strong = 1 and Weak = 0
# Convert strong into 1 and weak into 0

def trans_mathscore(x):
    if x == 'strong':
        return 1
    elif x == 'weak':
        return 0
    
mathscore_numeric = df['Mathscore'].apply(trans_mathscore)
print(mathscore_numeric)