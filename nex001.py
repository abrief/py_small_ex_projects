def longest_word():
    longest_so_far = ''
    for word in words:
        length = len(word)
        if length > len(longest_so_far):
            longest_so_far = word
    return longest_so_far

sentence = input("Enter a sentence: \n")
words = sentence.split(" ")
output = longest_word()
print(output)