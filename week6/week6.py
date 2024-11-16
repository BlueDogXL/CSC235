# response1 = "Very good product, highly satisfied"
# response2 = "Not bad but could be better"
# response3 = "Terrible experience, wouldn't recommend"
# response4 = "GOOD product"
  
# positive_words = ["good", "great", "satisfied"]
# negative_words = ["bad", "terrible", "wouldn't recommend"]

# responses = [response1,response2,response3,response4]
# posCount = 0
# negCount = 0
# for response in responses:
#     print(f"Response: {response}")
#     words = response.split()
#     for word in words:
#         for posWord in positive_words:
#             if word.upper() == posWord.upper():
#                 posCount = posCount + 1
#                 print(f"Positive word found: {word}")
#         for negWord in negative_words:
#             if word.upper() == negWord.upper():
#                 negCount = negCount + 1
#                 print(f"Negative word found: {word}")
#             if len(word) != len(negWord):
#                 if negWord.upper().__contains__(word.upper()):
#                     negCount = negCount + 1
#                     print(f"Negative word found: {word}")
#                     break
# print(f"Positive words: {posCount}")
# print(f"Negative words: {negCount}")
loopCondition = True
while loopCondition == True:
    decisionList = []
    print("text adventure 2! it's the same as the first one but less annoying to program!")
    for i in range(3): 
        decision = int(input(f"chosen so far: {decisionList}. press 1 for option 1, 2 for option 2: "))
        decisionList.append(decision)
    answer = input(f"chosen: {decisionList}. want to play again? (Y/N)")
    if answer.upper() == "Y":
        loopCondition = True
    elif answer.upper() == "N":
        loopCondition = False
    else:
        print("Not Y or N so i'm gonna assume you want to go again! have fun!")
        loopCondition = True
print("Thanks for playing!")