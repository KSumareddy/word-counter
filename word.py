import string

def word_counter(text):
    text = text.translate(str.maketrans('', '', string.punctuation.replace("'", "")))
    words = text.lower().split()
    
    return len(words)

input_text = input("Enter some text: ")
word_count = word_counter(input_text)
print(word_count)  
