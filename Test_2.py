def Tic():
    print("Welcome to the Game2");
    Player = ["Player1", "Player2"]
    for Player_index,each_player in enumerate(Player):
        Player[Player_index] = input("Enter Player's name:");
    print(f"Welcome {Player[0]} and {Player[1]} .\n\t Let's Begin !!!!!");
    l = [chr(32)]*9;
    Board = print(f'|{l[0]}|{l[1]}|{l[2]}|\n|{l[3]}|{l[4]}|{l[5]}|\n|{l[6]}|{l[7]}|{l[8]}|');
    Player1_input = input(f" Hello {Player[0]}, Please Choose 'X' or 'O' : ");
    if Player1_input == 'X':
        Player2_input = 'O';
    else:
        Player2_input = 'X';
    print(f"{Player1_input}, {Player2_input}");
    for index,inputs in enumerate(l):
        Online_Player = int(input(f"Please enter the position you want to put {Player1_input} :"));
        if l[Online_Player]==chr(32):
            l[Online_Player]=Player1_input;
        else:
            while l[Online_Player]== 'X' or l[Online_Player]== 'O':
                Online_Player = int(input(f"Please enter the position aganin you want to put {Player1_input} :"));
            l[Online_Player]=Player1_input;
            
        Board = print(f'|{l[0]}|{l[1]}|{l[2]}|\n|{l[3]}|{l[4]}|{l[5]}|\n|{l[6]}|{l[7]}|{l[8]}|');
        if l[0]==l[1]==l[2]!=chr(32) or l[0]==l[3]==l[6]!=chr(32) or l[0]==l[4]==l[8]!=chr(32):
            if l[0]==Player1_input:
                print(f'{l[0]} : {Player[0]} wins');
            else:
                print(f'{l[0]} : {Player[1]} wins');
            break;
        elif l[1]==l[4]==l[7]!=chr(32) or l[3]==l[4]==l[5]!=chr(32) or l[2]==l[4]==l[6]!=chr(32):
            if l[4]==Player1_input:
                print(f'{l[4]} : {Player[0]} wins');
            else:
                print(f'{l[4]} : {Player[1]} wins');
            break;
        elif l[2]==l[5]==l[8]!=chr(32) or l[6]==l[7]==l[8]!=chr(32):
            if l[8]==Player1_input:
                print(f'{l[8]} : {Player[0]} wins');
            else:
                print(f'{l[8]} : {Player[1]} wins');
            break; 
        Online_Player = int(input(f"Please enter the position you want to put {Player2_input} :"));
        if l[Online_Player]==chr(32):
            l[Online_Player]=Player2_input;
        else:
            while l[Online_Player]== 'X' or l[Online_Player]== 'O':
                Online_Player = int(input(f"Please enter the position aganin you want to put {Player2_input} :"));
            l[Online_Player]=Player2_input;
        Board = print(f'|{l[0]}|{l[1]}|{l[2]}|\n|{l[3]}|{l[4]}|{l[5]}|\n|{l[6]}|{l[7]}|{l[8]}|');
        if l[0]==l[1]==l[2]!=chr(32) or l[0]==l[3]==l[6]!=chr(32) or l[0]==l[4]==l[8]!=chr(32):
            if l[0]==Player1_input:
                print(f'{l[0]} : {Player[0]} wins');
            else:
                print(f'{l[0]} : {Player[1]} wins');
            break;
        elif l[1]==l[4]==l[7]!=chr(32) or l[3]==l[4]==l[5]!=chr(32) or l[2]==l[4]==l[6]!=chr(32):
            if l[4]==Player1_input:
                print(f'{l[4]} : {Player[0]} wins');
            else:
                print(f'{l[4]} : {Player[1]} wins');
            break;
        elif l[2]==l[5]==l[8]!=chr(32) or l[6]==l[7]==l[8]!=chr(32):
            if l[8]==Player1_input:
                print(f'{l[8]} : {Player[0]} wins');
            else:
                print(f'{l[8]} : {Player[1]} wins');
            break;
            
        
        
        
