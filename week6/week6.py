response1 = "Very good product, highly satisfied"
response2 = "Not bad but could be better"
response3 = "Terrible experience, wouldn't recommend"
response4 = "GOOD product"
  
positive_words = ["good", "great", "satisfied"]
negative_words = ["bad", "terrible", "wouldn't recommend"]

responses = [response1,response2,response3,response4]
posCount = 0
negCount = 0
for response in responses:
    print(f"Response: {response}")
    words = response.split()
    for word in words:
        for posWord in positive_words:
            if word.upper() == posWord.upper():
                posCount = posCount + 1
                print(f"Positive word found: {word}")
        for negWord in negative_words:
            if word.upper() == negWord.upper():
                negCount = negCount + 1
                print(f"Negative word found: {word}")
            if len(word) != len(negWord):
                if negWord.upper().__contains__(word.upper()):
                    negCount = negCount + 1
                    print(f"Negative word found: {word}")
                    break
print(f"Positive words: {posCount}")
print(f"Negative words: {negCount}")