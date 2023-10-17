# Would like to calculate how long on average I've lived in the same house

# Given a person's age and the number of times they've moved house as 'moves', return the average number of years that they've spent living in the same house

def years_in_one_house(age, moves):
    average_house_years = age / (moves + 1)
    return round(average_house_years)