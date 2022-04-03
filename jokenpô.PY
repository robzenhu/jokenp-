import random

def play():
    user = input("Escolha: 'r' para Rock, 'p' paper, 's' para scissors? ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "Empate!"
    
    if is_win(user, computer):
        return "Você venceu!"
    
    return "Você perdeu!"
    
def is_win(player, computer):
    if(player == 'r' and computer =='s') or (player == 's' and computer =='p')  or (player == 'Papel' and computer =='Pedra'):
        return True


print(play())
