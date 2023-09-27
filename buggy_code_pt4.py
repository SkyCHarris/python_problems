# Emmy has written a function that returns a greeting to users. However, she's in love with Mubashir, and wants to greet him slightly differently. She added a special case in her function, but made a mistake. Help!

def greeting(name):
    if name == "mubashir":
        return "Hello, my Love!"
    else:
        return "Hello, " + name + "!"