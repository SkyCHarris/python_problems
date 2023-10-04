# Create a function that returns the number of frames shown in a given number of minutes for a certain FPS

def frames(minutes, fps):
    return minutes * 60 * fps

frames(1, 1)
frames(10, 1)
frames(10, 25)