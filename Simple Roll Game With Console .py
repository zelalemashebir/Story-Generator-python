import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    
    return roll

while True:
  players= input("enter no of player(2-4): ")
  if players.isdigit():
     players=int(players)
     if 2 <= players <= 4:
        break
     else:
         print ("must between 2-4")
  else:
     print ("invalid ")
   
     

max_score= 50
player_scores=[0 for _ in range(players)]     

while max(player_scores) < max_score:
   for player_idx in range(players):
       print("\nplayer",player_idx + 1,"turn has stared\n")
       print("your totalscore is:",player_scores[player_idx],"\n")
       current_score = 0

       
       while True:
         should_roll= input("would u like to roll (y)? ")
         if should_roll.lower() != "y":
            break

         value =roll()
         if value == 1:
             print ("you rolled a 1! turn done")
             current_score=0
             break
              
         else:
             current_score += value
              
             print ("you rolled a:",value)

         print("your score is :",current_score)   
  
   player_scores[player_idx] += current_score
   print("your total score is",player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("player number", winning_idx + 1 , "is the winner score of", max_score )
