def Tic_Tac_Toe():
     print("Welcome to the Game2");
     Player = ["Player1", "Player2"]
     for Player_index,each_player in enumerate(Player):
        Player[Player_index] = input("Enter Player's name:");
      print(f"Welcome {Player[0]} and {Player[1]} .\n\t Let's Begin !!!!!");
      l = [chr(32)]*9;
      Board = print(f'|{l[0]}|{l[1]}|{l[2]}|\n|{l[3]}|{l[4]}|{l[5]}|\n|{l[6]}|{l[7]}|{l[8]}|');

      inputs = ['X','O']
      Player1_input = input(f" Hello {Player[0], Please Choose 'X' or 'O' : ");
      if Player1_input == 'X':
        Player2_input = 'O';
      else:
        Player2_input = 'X';
      print(f"{Player1_input}, {Player2input}");
    
    

    
