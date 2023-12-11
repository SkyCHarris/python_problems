
#! Mann-Whitney U Test

#TODO: scipy.stats.mannwhitneyu(x, y, use_continuity=True, alternative='two-sided', axis=0, method='auto', *, nan-policy='propagate', keepdims=False)

# Checks if there is a difference between 2 independent groups

# T-Test for ind. samples does the same thing
    # Mann-Whit is non-parametric counterpart

#? Diff w. t-test

# t-Test: Checks if there's a mean difference
# Mann-Whitney: Is there a difference in the rank sum?
    # How to calculate?
        # Assign rank to each participant in group
        # Disperesed across two groups, sum ranks for each group, compare
    # Data doesn't have to be normally distributed


#? Details

# Normal/ordinal variable with 2 expressions:

# Gender
# 1 = male
# 2 = female

# Medication
# 1 = Drug
# 2 = Placebo

# Production Facilities
# 1 = A
# 2 = B

# _________
# Independent Variable

# +
# A metric or ordinal variable
# This forms a rank order

# Salary
# Wellbeing
# Weight

# __________
# Dependent variabe


#? Requirements

# Two independent random samples with at least ordinally scaled characteristics
# Variables do NOT have to fulfill distribution curve


#? Null Hypothesis

# In the population, the sum of ranks in the two groups does not differ
# Sum of rank is the same


#? Alternative Hypothesis

# In the population, the sum of rankings differs in the groups


#? Calculate P-Value

# Number of cases (n1)
# n1 = 6

# Rank sum (t1)
# t1 = 37
