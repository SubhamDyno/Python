from tkinter import *
import tkinter as Tkinter
import random
import tkinter.messagebox as tm

root = Tk()
root.title("Tic Tac Toe")
root.geometry("600x500")

                
class Tic_Tac_Toe():
    
    def Welcome():
        Heading = Label(root, text="Welcome to the Game", fg="Black", bg="#45DD7C")
        Heading.pack()
        
        ''' Creating a separate frame inside root'''
        Player = LabelFrame(root, text="Player details")
        Player.pack(fill="both")

        ''' Assigning the varibale that is going to be entered in Player Entry label'''
        Player1_value = StringVar();
        Player2_value = StringVar();

        ''' Players Label Design'''
        Player1 = Label(Player, text="Enter Player1's Name")
        Player2 = Label(Player, text="Enter Player2's Name")

        ''' Placing the Players inside the Player Frame'''
        Player1.grid(row=0)
        Player2.grid(row=1)

        ''' Designing Entry box for players'''
        Player1_entry = Entry(Player,textvariable=Player1_value,bg="#7795D8")
        Player2_entry = Entry(Player,textvariable=Player2_value, bg="#7795D8")

        ''' Placing  the entry bix inside player label'''
        Player1_entry.grid(row=0,column=1)
        Player2_entry.grid(row=1,column=1)

        ''' Input for dropdown list '''
        Options = [
            "O",
            "X" ];
        marker_var = StringVar()

        ''' Default value for drop down '''
        marker_var.set("X");

        ''' Creating the dropdown list'''
        marker_assign = OptionMenu(Player, marker_var, *Options)
        marker_assign.grid(row=0, column=4)
        
        
        def Submitted():
            # Submitted is the command executed after submitting all below details :
            # Players Name, Players X,O assignment
            
            def rando():
                '''
                This function determines the random player
                who puts his/her mark first on Tic_Tac_Toe Board
                '''
                list_player = ['Player1', 'Player2']
                first = random.choice(list_player);
                return first
            #message box to show who won the rando function
            
            tm.showinfo("First to Go", f"Congratulation!! {rando()}");
            print(f"{marker_var.get()} "+ Player1_value.get()+ Player2_value.get())

            #Forget the packes which do not have to appear any more 
            Player.pack_forget()
            Heading.pack_forget();
            button.pack_forget();
            class B:
                
                print("Class-B", Player1_value.get()+ Player2_value.get());
                
                def Making_grid():
                    
                                
                        
                        
                    '''Box=[['Box1','Box2','Box3'],['Box4', 'Box5', 'Box6'],['Box7', 'Box8', 'Box9']]
                    for i in range(3):
                        for j in range(3):
                            Box[i][j] = StringVar();
                            print(type(Box[i][j]));'''
                    def Loop(create_box):
                        Box=[['Box1','Box2','Box3'],['Box4', 'Box5', 'Box6'],['Box7', 'Box8', 'Box9']]
                        for i in range(3):
                            for j in range(3):
                                Box[i][j] = StringVar();
                        Playing_Ground = LabelFrame(root, text="Playering Ground")
                        Playing_Ground.pack(fill="both");
                        
                        #create_box = {};
                        count=0
                        for i in range(3):
                            for j in range(3):
                                create_box[count] = Entry(Playing_Ground,textvariable=Box[i][j],width=2)
                                create_box[count].grid(row=i, column=j);
                                count+=1
                        print(type(create_box))
                        
                        def Output():
                            print("Hey i am the one" + Box[1][1].get())
                            Box[1][2].set("X");
                            count=0;
                            for i in range(8):
                                if create_box[i].get() != "":
                                        if len(create_box[i].get()) == 1 and (create_box[i].get() == 'O' or create_box[i].get() == 'X'):
                                            print("Valide\n-------------");
                                            print(create_box)
                                            Loop(create_box);
                                            
                                        else:
                                        #print("Invalide\n-----------");
                                            
                                            tm.showinfo("Message", "Invalid Entry ! Enter again");
                                            Loop(create_box);
                        '''valid = 1;
                        invalid=0;
                        
                                
                        def Validate(valid, invalid):
                            count=0;
                            #print(create_box[count].get());
                            if len(create_box[count].get()) == 1 and (create_box[count].get() == 'O' or create_box[count].get() == 'X'):
                                #print("Valide\n-------------")
                                count=count+1
                                return valid;
                        
                                        
                                            
                            else:
                                #print("Invalide\n-----------");
                                count=count+1
                                tm.showinfo("Message", "Invalid Entry ! Enter again");
                                return invalid;
                                
                        #def Empty(count, invalid):
                            #if create_box[count].get() == "":
                               # print("I am empty")
                            #return False;
                        
                        #Validate(count, valid);
                        
                        if Validate(valid, invalid)== valid:
                            print("Pela");
                            Loop(create_box);
                            
                        elif Validate(valid, invalid)== invalid:
                            print("Gula");
                            Loop(create_box);
                        else:
                            print("Somethingfissy");
                        
                        #Loop(create_box);
                        #Empty(count, invalid);
                        '''
                                
                        Next = Button(Playing_Ground,text="Next",command=Output)
                        Next.grid(row = 5, column=5)
                        return create_box;
                    create_box = {};
                    #count=0
                    Loop(create_box);
                   
                    
                
            o = B.Making_grid();
            
        button = Button(root, text="Submit Details", command=Submitted)
        button.pack();



        
    

if __name__ == "__main__":
    obj = Tic_Tac_Toe.Welcome();
    
    
