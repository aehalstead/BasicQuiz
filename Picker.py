from QuestionBank import QABank

class QuestionPicker(object):
    
    def my_questionPicker(self,level):
        
        p_dict = QABank()
        
        if level.lower() == "easy":
            return p_dict.my_easybank()
        elif level.lower() == "normal":
            return p_dict.my_normalbank()
        elif level.lower() == "hard":
            return p_dict.my_hardbank()
        else:
            return p_dict.my_easybank()
        
    def my_questionPickerValue(self,level):
        
        p_dict = QABank()
        
        if level.lower() == "easy":
            return 1
        elif level.lower() == "normal":
            return 2
        elif level.lower() == "hard":
            return 3
        else:
            return 1