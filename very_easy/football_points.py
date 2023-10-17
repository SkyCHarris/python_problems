# Create a function that takes the number of wins, draws, and losses and calculates the number of points a football team has obtained so far

def football_points(wins, draws, losses):
    win_points = wins * 3
    draw_points = draws * 1
    loss_points = losses * 0
    total_points = win_points + draw_points + loss_points
    print(total_points)
    return total_points

football_points(3, 4, 2)
football_points(5, 0, 2)
football_points(0, 0, 1)