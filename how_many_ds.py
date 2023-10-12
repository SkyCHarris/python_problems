
#! How Many D's Are There?

# Create a function that counts how many D's are in a sentence

def count_d(sentence):
    return sentence.count('d') + sentence.count('D')

count_d("My friend Dylan got distracted in school.")