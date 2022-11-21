Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sentence = input("Enter a sentence: ")
Enter a sentence: This sentence has no long words.
>>> listofWords = sentence.split()
>>> print("There are", len(listofWords), "words.")
There are 6 words.
>>> sum = 0
>>> for word in listofWords:
...     sum+= len(word)
...     print("The average word length is", sum / len(listofWords))
... 
...     
The average word length is 0.6666666666666666
The average word length is 2.0
The average word length is 2.5
The average word length is 2.8333333333333335
The average word length is 3.5
The average word length is 4.5
