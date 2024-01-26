import random
def get_choices():
    player_choice = input("Enter you choice: (rock,paper,scissors): ")
    all_choices = ["rock","paper","scissors"]
    computer_choice = random.choice(all_choices)
    dict = {"player":player_choice,"computer":computer_choice}
    result = check_result_nested_if(player_choice,computer_choice)
    return result

def check_result(player,computer):
    print(f"player played: {player} || computer played: {computer}")
    print("player played: "+ player + " || computer played: "+ computer)
    if(player == computer):
        return "Draw"
    elif (player == 'rock' and computer == 'scissors'):
        return "player win"
    elif (player == 'rock' and computer == 'paper'):
        return "player lose"
    elif(player == 'scissors' and computer == 'rock'):
        return "computer win"
    elif(player == 'scissors' and computer == 'paper'):
        return "player win"
    elif(player == 'paper' and computer == 'rock'):
        return "player win"
    elif(player == 'paper' and computer == 'scissors'):
        return "player lose"
    else:
        return "something went wrong"
    
def check_result_nested_if(player:str,computer:str):
    print(f"player played: {player} || computer played: {computer}")
    print("player played: "+ player + " || computer played: "+ computer)
    if(player == computer):
        return "Draw"
    if(player == 'rock'):
        if(computer == 'scissors'):
            return 'player win'
        else:
            return 'computer win'
    elif(player == 'scissors'):
        if(computer == 'rock'):
            return 'player win'
        else:
            return 'computer win'
    elif(player == 'paper'):
        if(computer == 'rock'):
            return 'player win'
        else:
            return 'computer win'
    else:
        return 'Something went wrong'
    
#Accesing value in Dict 
def access_dict():
    dict = {
        "player":"rock",
        "computer":"paper"
    }
    p_choice = dict['player']
    c_choice = dict['computer']
    return (f"player chooses {p_choice} and computer {c_choice}")
        

result = access_dict()
print(result)
