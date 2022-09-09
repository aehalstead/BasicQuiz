# BasicQuiz Python Basic Quiz
# Making a QuizGame with simple questions
# Goal 1: Must take in muiltiple questions and randomly rotate through them without repeating
# Goal 2: Keep score base off Question Difficulty
# Goal 3: Add a second player and winner
# Goal 4: Add a mix level of difficulty

from Picker import QuestionPicker

print("Game will begin!")
doesUserWantsToPlay=input("Do you want to play? ")
#Confirming Player wants to play
if (doesUserWantsToPlay.lower() != "yes" ):
    quit()

#set score to zero
score = 0 

levelPlayerWants = input("Easy, Normal, Hard? ")

#Question Picker pickes the right level from the dictionary
ap_dict = QuestionPicker()

for key, value in dict(ap_dict.my_questionPicker(levelPlayerWants)).items():
    
    #Asking Questions
    answer = input(key)

    if str(answer.lower()) == value.lower():
        print("Correct")
        score += ap_dict.my_questionPickerValue(levelPlayerWants,)
        
    else:
        print("Wrong")
        

print("Game Ends! Score: " + str(score))
