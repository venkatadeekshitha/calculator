from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def game(request):
    result=None
    player1=''
    player2=''

    if request.method == "POST":
        player1 = request.POST.get('player1','').lower()
        player2 = request.POST.get('player2','').lower()


        valid_choices = ['rpck','paper','scissors']

        if player1 in valid_choices and player2 in valid_choices:
            if player1 == player2:
                result = 'It\'s a tie!'
            elif (player1 == 'rock' and player2 =='scissors') or \
                 (player1 == 'scissors' and player2 =='paper') or \  
                 (player1 == 'paper' and player2 =='rock'):
                result = 'palyer 1 wins!'
            else: 
                result = 'player 2 wins!'
        else:
            result ='Invalid input! please enter rock,paper,scissor.'
    return render(request, 'index.html',{
        'result': result,
        'player1': player1,
        'player2': player2,
    })             
   
