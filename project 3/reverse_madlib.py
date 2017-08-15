parts_of_speech=("a","b","c","d")
question=[[ '1.Butterfly has _1_ legs','2._2_ is the fastest animal on the land','3._3_is the coldest location in the earth','4._4_ is the animal referred as the ship of the desert'] ,['5._a_is the least populated country in the world','6._b_ is the oldest democracy in the world','7._c_is the longest river on the earth','8._d_ is the hottest place in the world'],[ '9._a_ is the creater of jeeves and wooster', '10._b_ indoor sport is most popular in the U.S','11._c_was the country hosting 2008 olympic games','12._d_ country was golf first played']]
answer=[["six","cheetah","east antartica","camel"],["vartian city","british","nile","ethiopia"],["P.G wodehouse","basketball","china","scotland"]]
level1=1


def level_chosen_user():
    # In this it will chose the level given by the user
    u_input = raw_input("_"*10+"ENTER THE LEVEL"+"\nenter 1>> for level1"+"\nenter 2>> for level2"+"\nenter 3>> for level3\n")
    return (int(u_input)-1)


def quiz_start(level):
    # Than it will print the question one by one following that it will ask the user to enter answer if answer matches it will move to next question otherwise again print that question until the correct answer is entered.
    i=0
    max_ques=4
    
    while(i<max_ques):
        print question[level][i]
        chosen_user=raw_input("your answer  ")
        if chosen_user == answer[level][i]:
            correct_answer()
            replace=[]
            replace=question[level][i].split('_'+str(i+1)+'_')
            question[level][i]=question[level][i].replace('_'+str(i+1)+'_', chosen_user)
            print question[level][i]
                                     
            
            i=i+1
        else:
            wrong_answer()

    print('successfully done')





def wrong_answer():
    # If the answer entered by the user is wrong than it will print the message.
    print("oops!!you have entered wrong answer...try it again")


def test(chosen_user,answer):
    # In this it will ask the answer by the user than it will compare with the actual answer provided by us.If the answer is true it will return true otherwise return false.
    chosen_user=raw_input("your answer")
    if chosen_user == answer:
        return true
    else:
        return false



def correct_answer():
    # If the answer entered by the user is correct than it will print the message for correct answer.
    print("you have answered correct one!!!")



def start():
    # It will start the quiz by calling the function.
    print('welcome to the quiz')
    print('to continue enter continue and to exit enter -1')
    conti = 'c'
    while conti != 'q':
        level=level_chosen_user()
        quiz_start(level)
        conti = raw_input("Do you want to continue\n Press c to continue or q to quit!!")
       

start()
