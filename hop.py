import random


player_names=[]
player_scores=[]





while True:

    checker=False#to check if the player played befor
    idIndex=None#to find the score of each id
    score=0
    answer=None
    #get an id
    player_id=input("ID: ")
    #check if it's in the list or not
    for x in player_names:
        if x==player_id:
            checker=True
    #add the new player id
    if checker==False:
        player_names.append(player_id)
    #defin the idIndex
    idIndex=player_names.index(player_id)
    #choose a num to start
    starter=random.randint(1,9)
    print(starter)
    num=starter
    print(player_names)
     
    while True:

        #pc starts
        if num%5==0:
            pc="hop"
        else:
            pc=num
        print("pc: "+str(pc))
        #choose the players turn
        answer=num+1
        if answer%5==0:
            answer="hop"
        print("cheet: "+str(answer))
        #get the players answer
        inpt=input("You: ")
        #check if its right
        if inpt==str(answer):
            score=score+1
            print("score: "+str(score))
        else:
            #if it's wrong....
            print("Wrong X_X")
            #show the highest score
            if checker==False:
                print("highest: "+str(score))
            else:
                if score<player_scores[idIndex]:
                    print("highest: "+str(player_scores[idIndex]))
                else:print("highest: "+str(score))
            #ask if play again
            print("Wanna play again?")
            #get the answer
            loser_answer=input(": ")
            if loser_answer=="yes":
                if checker==False:
                    player_names.pop(len(player_names))

                break#play again
            elif loser_answer=="no":
                #add the score to the list
                if checker==False:
                    player_scores.append(score)
                else:
                    if score>player_scores[idIndex]:
                        player_scores[idIndex]=score
                #make a list of with a tuple of scors and players

                mergedList=[(player_names[i],player_scores[i]) for i in range(0, len(player_names))]
                
                #sort the list based on scores
                mergedList.sort(key=lambda a:a[1])
                #reverse the list
                mergedList.reverse()
                #print the first three
                print("Top three: "),
                count=0#a counter to put exactly the first three indexes
                for x in mergedList:
                    if count<3:
                        print(mergedList[count])
                        count+=1
                    else:
                        break
                #updating the score
                if score>player_scores[player_names.index(player_id)]:
                    player_scores.insert(player_names.index(player_id),score)
                break
            
            

        num=num+2 