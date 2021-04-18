#define Your rules here
def Rules():
    rules = {"Numbers":{
                        "zero": 0,
                        "one" : 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9,
                        "ten": 10,
                        "eleven":11,
                        "twelve":12,
                        "thirteen":13,
                        "fourteen":14,
                        "fifteen":15,
                        "sixteen":16,
                        "seventeen":17,
                        "eighteen":18,
                        "nineteen":19,
                        "twenty": 20,
                        "thirty": 30,
                        "forty": 40,
                        "fifty": 50,
                        "sixty": 60,
                        "seventy": 70,
                        "eighty": 80,
                        "ninety": 90,
                        "hundred": 100
                        },
            "Tuples": {
                         "single":1,
                         "double":2,
                         "triple":3,
                         "quadruple":4,
                         "quintuple":5,
                         "sextuple":6,
                         "septuple":7,
                         "octuple":8,
                         "nonuple":9,
                         "decuple":10
                      },
            "General": {
                          "A T M":"ATM",
                          "C M": "CM",
                          "P M": "PM",
                          "D M": "DM",
                          "A M": "AM"
                       }
            }
    return rules

#checking if word has comma at front or at last or at both 
def check_for_coma(word):
    front=""
    last=""
    if(len(word)>1):
        if word[-1]==',' or word[-1]=='.':
            last=word[-1]
            word=word[:-1]
        if word[0]==',' or word[0]=='.':
            front=word[0]
            word=word[1:]
    return front,word,last


#class for conversion
class S2W:

    def __init__(self):

        self.rules=Rules()
        self.paragraph=""
        self.output=""

    #getting user input
    def get_input(self):

        self.paragraph=input("\nEnter Your data:\n")

        if not self.paragraph:
            raise ValueError("No data entered")

    #user output
    def show_output(self):
        print("\nConverted Data:\n \"" +self.output+"\"")

    
    #conversion function
    def Convert(self):
        #splitting entered data into words
        words=self.paragraph.split()

        #accessing defines rules
        numbers=self.rules['Numbers']
        tuples=self.rules['Tuples']
        general=self.rules['General']
        i=0
        no_of_words=len(words)
         
        while i<no_of_words: 
            front,word,last=check_for_coma(words[i])
            #for $ 
            if i+1!= no_of_words:
                front_n,next_word,last_n=check_for_coma(words[i+1])
                if word.lower() in numbers.keys() and (next_word.lower()=='dollars' or next_word.lower()=='dollar'):
                    self.output=self.output+" "+front+"$"+str(numbers[word.lower()])+last
                    i=i+2

                elif word.lower() in tuples.keys() and len(next_word)==1:
                    #when word is of form Triple A
                    self.output=self.output+" "+front_n+(next_word*tuples[word.lower()])+last_n
                    i=i+2
                elif (word+" "+next_word) in general.keys():
                    #if word is of form P M or C M
                    self.output=self.output+" "+front+word+next_word+last_n
                    i=i+2
                else:
                    self.output=self.output+" "+words[i]
                    i=i+1
            else:
                self.output=self.output+" "+words[i]
                i=i+1
#main function 
def main():
    obj_spoken=S2W()#class
    obj_spoken.get_input()#getting user data
    obj_spoken.Convert()#conversion

    obj_spoken.show_output()#output

if __name__ == "__main__":
    main()
