
#! Scrabble Hand

# Given a list of scrabble tiles (as dict.), create af unction that outputs the maximum possible score a player can achieve by summing up the total number of points for all the tiles in their hands
# Each hand contains 7 scrabble tiles

def maximum_score(tile_hand):
    sum = 0
    for value in tile_hand:
        sum += sum(tile_hand.get("score"))
    return sum
[
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]

# Attempt 2

def maximum_score(tile_hand):
    sum = 0
    for i in tile_hand:
        for value in i:
            score = tile_hand.get("score")
            print(score)
            sum += score
    return sum

[
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]

# Attempt 3

def maximum_score(tile_hand):
    sum = 0
    for i in tile_hand:
        score = tile_hand.get("score")
    print(score)

[
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]

# Attempt 4

def maximum_score(tile_hand):
    for key, value in tile_hand.items():
        return sum(value)
    
[
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]

# Attempt 5

def maximum_score(tile_hand):
    for key, value in tile_hand:
        print(key,value)

[
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]

# Attempt 6

def maximum_score(tile_hand):
    sum = 0
    for i in tile_hand:
        sum += i.get("score")
    return sum
        

maximum_score([
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
])