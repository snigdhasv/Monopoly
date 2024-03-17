import tkinter
import random
from tkinter import *
from PIL import Image, ImageTk

#import Player
from Bank import *

def check_cond(player_data,card,i,dice_num,no_players):
    #lands/passes GO
    if player_data['player'+' '+i]['position']-dice_num<=0 and player_data['player'+' '+i]['round']>1:
        player_data['player'+' '+i]['round']+=1
        player_data['player'+' '+i]['money']+=200
    

    #player lands on property 
    if player_data['player'+' '+i]['position'] in (2,4,7,9,10,12,14,15,17,19,20,22,24,25,27,28,30,32,33,35,38,40):
        property(player_data,card,no_players,i)

    #player lands on railroads
    elif player_data['player'+' '+i]['position'] in (6,16,26,36):
        rails(player_data,card,no_players,i)

    #income tax
    elif player_data['player'+' '+i]['position']==5:
        player_data['player'+' '+i]['money']-=200

    #landing on jail for just visiting
    elif player_data['player'+' '+i]['position']==11:
        if (player_data['player'+' '+i]['position']-dice_num)<=11 or (player_data['player'+' '+i]['position']-dice_num) in (40,39):
            pass
    
    #landing on go to jail
    elif player_data['player'+' '+i]['position']==31:
        player_data['player'+' '+i]['position']=11
        jail(player_data,card,i,dice_num,no_players)

    #landing on utilities
    elif player_data['player'+' '+i]['position'] in (13,29):
        utility(player_data,no_players,i,dice_num,card)

    #landing on free parking
    elif player_data['player'+' '+i]['position']==21:
        pass

    #luxury tax
    elif player_data['player'+' '+i]['position']==39:
        if len(player_data['player'+' '+i]['railroads'])>=1:
            player_data['player'+' '+i]['money']-=75
        else:
            pass

    #community chest
    elif player_data['player'+' '+i]['position'] in (3,18,34):
        com_chest(player_data,card,i,dice_num,no_players)

    #chance
    elif player_data['player'+' '+i]['position'] in (8,23,37):
        chance(player_data,i,card,no_players,dice_num)


def property(player_data,card,no_players,i):
    #check who owns prop
    place=places[player_data['player'+' '+i]['position']]
    color=card[place]["Colour"]

    for b in range(no_players):
        j=str(b+1)
        #if some other player owns prop
        if place in player_data['player'+' '+j]['property'][color] and place not in player_data['player'+' '+j]['houses'].keys() and place not in player_data['player'+' '+j]['hotel']:
            if j!=i:
                player_data['player'+' '+i]['money']-=card[place]['Rent']
                player_data['player'+' '+j]['money']+=card[place]['Rent']

                rframe=Frame(screen2)
                rframe.grid(row=3,column=0)
                def clear_frame():
                    for w in rframe.winfo_children():
                        w.destroy()
                Button(rframe,text=("Pay rent:",card[place]['Rent'],"to Player",j),command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid()
                break
            
        elif place in player_data['player'+' '+j]['houses'].keys():
            if j!=i:
                if place in player_data['player'+' '+j]['property'][color] and player_data['player'+' '+j]['houses'][place]==1:
                    player_data['player'+' '+i]['money']-=card[place]['Rent with 1 house']
                    player_data['player'+' '+j]['money']+=card[place]['Rent with 1 house']

                    rframe=Frame(screen2)
                    rframe.grid(row=3,column=0)
                    def clear_frame():
                        for w in rframe.winfo_children():
                            w.destroy()        
                    Button(rframe,text=("Pay rent with 1 house:",card[place]['Rent with 1 house'],"to Player",j),command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid()
                    break

                elif place in player_data['player'+' '+j]['property'][color] and player_data['player'+' '+j]['houses'][place]==2:
                    player_data['player'+' '+i]['money']-=card[place]['Rent with 2 houses']
                    player_data['player'+' '+j]['money']+=card[place]['Rent with 2 house']

                    rframe=Frame(screen2)
                    rframe.grid(row=3,column=0)
                    def clear_frame():
                        for w in rframe.winfo_children():
                            w.destroy()
                    Button(rframe,text=("Pay rent with 2 house:",card[place]['Rent with 2 house'],"to Player",j),command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid()
                    break
                    
                elif place in player_data['player'+' '+j]['property'][color] and player_data['player'+' '+j]['houses'][place]==3:
                    player_data['player'+' '+i]['money']-=card[place]['Rent with 3 houses']
                    player_data['player'+' '+j]['money']+=card[place]['Rent with 3 house']

                    rframe=Frame(screen2)
                    rframe.grid(row=3,column=0)
                    def clear_frame():
                        for w in rframe.winfo_children():
                            w.destroy()
                    Button(rframe,text=("Pay rent with 3 house:",card[place]['Rent with 3 house'],"to Player",j),command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid()
                    break

                elif place in player_data['player'+' '+j]['property'][color] and player_data['player'+' '+j]['houses'][place]==4:
                    player_data['player'+' '+i]['money']-=card[place]['Rent with 4 houses']
                    player_data['player'+' '+j]['money']+=card[place]['Rent with 4 house']

                    rframe=Frame(screen2)
                    rframe.grid(row=3,column=0)
                    def clear_frame():
                        for w in rframe.winfo_children():
                            w.destroy()
                    Button(rframe,text=("Pay rent with 4 house:",card[place]['Rent with 4 house'],"to Player",j),command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid()
                    break
                
        elif place in player_data['player'+' '+j]['hotel']:
            if j!=i:
                player_data['player'+' '+i]['money']-=card[place]['Rent with hotel']
                player_data['player'+' '+j]['money']+=card[place]['Rent with hotel']

                rframe=Frame(screen2)
                rframe.grid(row=3,column=0)
                def clear_frame():
                    for w in rframe.winfo_children():
                        w.destroy()
                Button(rframe,text=("Pay rent with hotel:",card[place]['Rent with hotel'],"to Player",j),command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid()
                break
                
        


        #if player himself owns the prop
        elif place in player_data['player'+' '+i]['property'][color]:
            #check if he owns all props of this colour and has 4 houses on this prop
            if j==i:
                if place in player_data['player'+' '+i]['houses'].keys():
                    if player_data['player'+' '+i]['houses'][place]==4:
                        if (color!='Purple' and len(player_data['player'+' '+i]['property'][color])==3) or (color=='Purple' and len(player_data['player'+' '+i]['property'][color])==2):
                            #OPTIONS DISPLAY
                            oframe=Frame(screen2)
                            oframe.grid(row=3,column=0)
                            olabel=Label(oframe,text="DO YOU WANT TO BUY A HOTEL?",font=('Lucida Console',12))
                            olabel.grid(row=0,column=1)
                            def yes():
                                player_data['player'+' '+i]['hotel'].append(place)
                                player_data['player'+' '+i]['money']-=card[place]['Hotel cost']
                                for w in oframe.winfo_children():
                                    w.destroy()
                            def clear_frame():
                                for w in oframe.winfo_children():
                                    w.destroy()
                            Button(oframe,text='YES',command=yes,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=1,column=0)
                            Button(oframe,text='NO',command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=1,column=2)

                        break

                    #build more houses if 4 houses not there
                    elif player_data['player'+' '+i]['houses'][place]<4:
                        #OPTIONS DISPLAY
                        oframe=Frame(screen2)
                        oframe.grid(row=3,column=0)
                        olabel=Label(oframe,text="DO YOU WANT TO BUY A HOUSE?",font=('Lucida Console',12))
                        olabel.grid(row=0,column=1)
                        def yes():
                            player_data['player'+' '+i]['houses'][place]+=1
                            player_data['player'+' '+i]['money']-=card[place]['House cost']
                            for w in oframe.winfo_children():
                                w.destroy()
                        def clear_frame():
                            for w in oframe.winfo_children():
                                w.destroy()   
                        
                        Button(oframe,text='YES',command=yes,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=1,column=0)
                        Button(oframe,text='NO',command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=1,column=2)
                        break
                        
                            
            
    #if nobody owns the prop
    else:
        #OPTIONS DISPLAY
        oframe=Frame(screen2)
        oframe.grid(row=3,column=0)
        olabel=Label(oframe,text="DO YOU WANT TO BUY THE PROPERTY?",font=('Lucida Console',12))
        olabel.grid(row=0,column=1)
        def yes():
            player_data['player'+' '+i]['property'][color].append(place) #add the prop in player_data
            player_data['player'+' '+i]['money']-=card[place]["Property cost"]
            for w in oframe.winfo_children():
                w.destroy()
        def clear_frame():
            for w in oframe.winfo_children():
                w.destroy()
        Button(oframe,text='YES',command=yes,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=1,column=0)
        Button(oframe,text='NO',command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=1,column=2)



def rails(player_data,card,no_players,i):
    place=places[player_data['player'+' '+i]['position']]
    prop_cost=card[place]["Property cost"]

    if place not in player_data['player'+' '+i]['railroads']: #player himself doesn't own it

        for b in range(no_players):
            j=str(b+1)
            #to check if some other player owns the railroad
            if place in player_data['player'+' '+j]['railroads'] and j!=i:
                if len(player_data['player'+' '+j]['railroads'])==1:
                    player_data['player'+' '+i]['money']-=25
                    player_data['player'+' '+j]['money']+=25
                    break
                
                elif len(player_data['player'+' '+j]['railroads'])==2:
                    player_data['player'+' '+i]['money']-=50
                    player_data['player'+' '+j]['money']+=50
                    break
                
                elif len(player_data['player'+' '+j]['railroads'])==3:
                    player_data['player'+' '+i]['money']-=100
                    player_data['player'+' '+j]['money']+=100
                    break

                elif len(player_data['player'+' '+j]['railroads'])==4:
                    player_data['player'+' '+i]['money']-=200
                    player_data['player'+' '+j]['money']+=200
                    break
            
        #to give option to buy if nobody already owns the railroad
        else:
            #OPTIONS DISPLAY
            oframe=Frame(screen2)
            oframe.grid(row=3,column=0)
            olabel=Label(oframe,text="DO YOU WANT TO BUY THIS RAILROAD?",font=('Lucida Console',12))
            olabel.grid(row=0,column=1)
            def yes():
                player_data['player'+' '+i]['railroads'].append(place)
                player_data['player'+' '+i]['money']-=prop_cost
                for w in oframe.winfo_children():
                    w.destroy()
            def clear_frame():
                for w in oframe.winfo_children():
                    w.destroy()
            Button(oframe,text='YES',command=yes,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=1,column=0)
            Button(oframe,text='NO',command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=1,column=2)
            
    else:
        pass   
                

def jail(player_data,card,i,dice_num,no_players):
    #OPTIONS DISPLAY
    oframe=Frame(screen2)
    oframe.grid(row=3,column=0)
    olabel=Label(oframe,text="SELECT WAY TO GET OUT",font=('Lucida Console',12))
    olabel.grid(row=0,column=0)
    def ONE():
        pass
    def TWO():
        if player_data['player'+' '+i]['get out of jail']>=1:       
            player_data['player'+' '+i]['get out of jail']-=1
            with open('dice.txt','r') as f:
                d=f.read()
                d1,d2=d.split()
            dice_num=int(d1)+int(d2)
            player_data['player'+' '+i]['position']+=dice_num
            check_cond(player_data,card,i,dice_num,no_players)
            
        else:
            pass
   
    def THREE():
        player_data['player'+' '+i]['money']-=50
        with open('dice.txt','r') as f:
            d=f.read()
            d1,d2=d.split()
        dice_num=int(d1)+int(d2)
        player_data['player'+' '+i]['position']+=dice_num
        check_cond(player_data,card,i,dice_num,no_players)
    def clear_frame():
        for w in oframe.winfo_children():
            w.destroy()
    

    Button(oframe,text='WAIT ONE ROUND',command=ONE,font=('Copperplate Gothic',12),background='#656565',foreground='#FAF3EF').grid(row=1,column=0)
    Button(oframe,text='GET OUT OF JAIL FREE CARD',command=TWO,font=('Copperplate Gothic',12),background='#656565',foreground='#FAF3EF').grid(row=2,column=0)
    Button(oframe,text='PAY $50 AND GET OUT',command=THREE,font=('Copperplate Gothic',12),background='#656565',foreground='#FAF3EF').grid(row=3,column=0)

    Button(oframe,text='confirm',command=clear_frame,font=('Copperplate Gothic',12),background='#656565',foreground='#FAF3EF').grid(row=5,column=0)



def winner(player_data,no_players):
    mon=[]
    for b in range(no_players):
        j=str(b+1)
        mon.append(player_data['player'+' '+j]['money'])
    
    win=mon.index(max(mon))
    return (win+1)
        


def utility(player_data,no_players,i,dice_num,card):
    place=places[player_data['player'+' '+i]['position']]
    prop_cost=card[place]["Property cost"]
    if place not in player_data['player'+' '+i]['utilities']: #player himself doesn't own it
        for b in range(no_players):
            j=str(b+1)
            #to check if some other player owns the utility
            if place in player_data['player'+' '+j]['utilities'] and j!=i:
                if len(player_data['player'+' '+j]['utilities'])==1:
                    player_data['player'+' '+i]['money']-=dice_num*4
                    player_data['player'+' '+j]['money']+=dice_num*4
                    break
                
                elif len(player_data['player'+' '+j]['utilities'])==2:
                    player_data['player'+' '+i]['money']-=dice_num*10
                    player_data['player'+' '+j]['money']+=dice_num*10
                    break
            
            
        #to give option to buy if nobody already owns the utility
        else:
            #OPTIONS DISPLAY
            oframe=Frame(screen2)
            oframe.grid(row=3,column=0)
            olabel=Label(oframe,text="DO YOU WANT TO BUY THIS UTILITY?",font=('Lucida Console',12))
            olabel.grid(row=0,column=1)
            def yes():
                player_data['player'+' '+i]['utilities'].append(place)
                player_data['player'+' '+i]['money']-=prop_cost
                for w in oframe.winfo_children():
                    w.destroy()
            def clear_frame():
                for w in oframe.winfo_children():
                    w.destroy()
            Button(oframe,text='YES',command=yes,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=1,column=0)
            Button(oframe,text='NO',command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=1,column=2)
            
    else:
        pass   



def com_chest(player_data,card,i,dice_num,no_players):
    c=random.randint(1,16) #c=card number (card is randomly picked)

    com_chest_frame=Frame(screen2)
    com_chest_frame.grid(row=3,column=0)
    def clear_frame():
        for w in com_chest_frame.winfo_children():
            w.destroy()
    Button(com_chest_frame,text=community_chest[c],command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=2,column=0)


    if c==1:
        player_data['player'+' '+i]['position']=1
        player_data['player'+' '+i]['money']+=200
    
    elif c==2:
        player_data['player'+' '+i]['money']+=200
    
    elif c==3:
        player_data['player'+' '+i]['money']-=50
    
    elif c==4:
        player_data['player'+' '+i]['money']+=50
    
    elif c==5:
        player_data['player'+' '+i]['get out of jail']+=1

    elif c==6:
        player_data['player'+' '+i]['position']=11
        jail(player_data,card,i,dice_num,no_players)

    elif c==7:
        player_data['player'+' '+i]['money']-=50
    
    elif c==8:
        player_data['player'+' '+i]['money']+=100
    
    elif c==9:
        player_data['player'+' '+i]['money']+=20
    
    elif c==10:
        player_data['player'+' '+i]['money']+=10
    
    elif c==11:
        player_data['player'+' '+i]['money']+=100
    
    elif c==12:
        player_data['player'+' '+i]['money']-=50
    
    elif c==13:
        player_data['player'+' '+i]['money']-=50
    
    elif c==14:
        player_data['player'+' '+i]['money']+=25

    elif c==15:
        no_house=0 #no. of houses
        for i in player_data['player'+' '+i]['houses'].values():
            no_house+=i
        player_data['player'+' '+i]['money']-=40*no_house

        no_hotel=len(player_data['player'+' '+i]['hotel'])
        player_data['player'+' '+i]['money']-=115*no_hotel
    
    elif c==16:
        player_data['player'+' '+i]['money']+=10


def chance(player_data,i,card,no_players,dice_num):
    c=random.randint(1,16)
    chance_frame=Frame(screen2)
    chance_frame.grid(row=3,column=0)
    def clear_frame():
        for w in chance_frame.winfo_children():
            w.destroy()
    Button(chance_frame,text=chance_c[c],command=clear_frame,font=('Copperplate Gothic',12,'bold'),background='#656565',foreground='#FAF3EF').grid(row=2,column=0)

    if c==1 :
        player_data['player'+' '+i]['position']=1
        player_data['player'+' '+i]['money']+=200
    elif c==2:
        player_data['player'+' '+i]['position']=25
        property(player_data,card,no_players,i)
    elif c==3:
        player_data['player'+' '+i]['position']=12
        property(player_data,card,no_players,i)
    elif c==4:
        if player_data['player'+' '+i]['position']==8:
            player_data['player'+' '+i]['position']=13
        elif player_data['player'+' '+i]['position'] in (23,37):
            player_data['player'+' '+i]['position']=29
        utility(player_data,no_players,i,dice_num,card)
    elif c==5:
        if player_data['player'+' '+i]['position']==37:
            player_data['player'+' '+i]['position']=36
        elif player_data['player'+' '+i]['position'] == 23 :
            player_data['player'+' '+i]['position']=26
        elif player_data['player'+' '+i]['position'] == 8:
            player_data['player'+' '+i]['position']=6
    elif c==6:
        player_data['player'+' '+i]['money']+=50
    elif c==7:
        player_data['player'+' '+i]['get out of jail']+=1
    elif c==8:
        player_data['player'+' '+i]['position']-=3
    elif c==9:
        player_data['player'+' '+i]['position']=11
        jail(player_data,card,i,dice_num,no_players)
    elif c==10:
        no_house=0 #no. of houses
        for i in player_data['player'+' '+i]['houses'].values():
            no_house+=i
        player_data['player'+' '+i]['money']-=15*no_house
    elif c==11:
        player_data['player'+' '+i]['position']=6
    elif c==12:
        player_data['player'+' '+i]['position']=40
    elif c==13:
        player_data['player'+' '+i]['money']-=50*(no_players-1)
        for j in range(no_players):
            j=str(j+1)
            if(j!=i) :
                player_data['player'+' '+j]['money']+=50
    elif c==14:
        player_data['player'+' '+i]['money']+=150
    elif c==15:
        player_data['player'+' '+i]['money']-=150
    elif c==16:
        player_data['player'+' '+i]['money']-=15





if __name__=='__main__':
        
    screen=Tk()
    screen.title("Monopoly")
    screen.geometry('600x500')
    #Putting monopoly logo
    image=Image.open(r"logo.png")
    logo=image.resize((550,230))
    img=ImageTk.PhotoImage(logo)
    label=Label(image=img)
    label.image=img
    label.pack()
    number=IntVar()
    Label(screen,text="").pack()
    Label(screen,text="ENTER NUMBER OF PLAYERS",width="600",height='2',font=('Lucida Console',15,'bold'),background='#9EA4B3').pack()
    Label(screen,text="").pack()

    np=Entry(screen,textvariable=number,font=('Lucida Console',15))
    np.pack()
    Label(screen,text="").pack()

    def start():
        
        no_of_players=np.get()
        file=open("log.txt",'w')
        file.write(no_of_players)
        file.close()
        np.delete(0,END)
        global screen2
        screen2=Toplevel(screen)
        screen2.title("Monopoly game")
        screen2.geometry('1500x1000')

        image1=Image.open(r"logo.png")
        logo1=image1.resize((385,161))
        img=ImageTk.PhotoImage(logo1)
        pic=Label(screen2,image=img)
        pic.image=img
        pic.grid(row=0,column=1)
    

        with open('log.txt','r') as f:
            no_players=int(f.read())#extract the number of players from the text file created in the gui code(input_screen.py)


        player_data=allot_values(no_players)#alloting start values (refer Bank.py) 
        card=cards()#refer Bank.py
        
        
        a=0
        def nextplayer():

                #for a in range(no_players):
                nonlocal a
                if a<=no_players:
                
                
                    i=str(a+1)
                    dice_frame=Frame(screen2)
                    dice_frame.grid(row=2,column=1)

                    dice_list=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

                    d1_label=Label(dice_frame,text='',font=('Helvetica',100))
                    d1_label.grid(row=0,column=0)
                    d2_label=Label(dice_frame,text='',font=('Helvetica',100))
                    d2_label.grid(row=0,column=1)


                    
                    di1=random.randint(1,6)
                    di2=random.randint(1,6)
                    d1=dice_list[di1-1]
                    d2=dice_list[di2-1]
                    d1_label.config(text=d1)
                    d2_label.config(text=d2)

                    d=str(di1)+' '+str(di2)
                    with open ('dice.txt','w') as f:
                        f.write(d)


                    #DICE
                    with open('dice.txt','r') as f:
                        d=f.read()
                        d1,d2=d.split()
                    dice_num=int(d1)+int(d2)


                    #UPDATING PLAYER POSITION
                    player_data['player'+' '+i]['position']+=dice_num #increasing position after dice is rolled
                    if player_data['player'+' '+i]['position']>40:
                        player_data['player'+' '+i]['position']=player_data['player'+' '+i]['position']-40 #if position > 40 you gotta restart positions

                    

                    #PLAYER NUMBER
                    pframe=Frame(screen2,width=50,height=2)
                    pframe.grid(row=1,column=1)
                    plabel=Label(pframe,text=f"PLAYER NUMBER {i}",font=('Copperplate Gothic',14,'bold'))
                    plabel.grid(row=0,column=0)
                       

                    #PLAYER PROPERTIES
                    propframe=Frame(screen2)
                    propframe.grid(row=2,column=2)

                    purp=player_data['player'+' '+i]['property']['Purple']
                    lightblue=player_data['player'+' '+i]['property']['Light Blue']
                    pink=player_data['player'+' '+i]['property']['Pink']
                    orange=player_data['player'+' '+i]['property']['Orange']
                    red=player_data['player'+' '+i]['property']['Red']
                    yellow=player_data['player'+' '+i]['property']['Yellow']
                    green=player_data['player'+' '+i]['property']['Green']
                    darkblue=player_data['player'+' '+i]['property']['Dark Blue']

                    rails=player_data['player'+' '+i]['railroads']
                    utilities=player_data['player'+' '+i]['utilities']
                    house=player_data['player'+' '+i]['houses']
                    hotel=player_data['player'+' '+i]['hotel']
                    gooj=player_data['player'+' '+i]['get out of jail']

                    Label(propframe,text=f"PURPLE PROPERTIES OWNED: {purp}",font=('Futura',12)).grid(row=1,column=1)
                    Label(propframe,text=f"LIGHT BLUE PROPERTIES OWNED: {lightblue}",font=('Futura',12)).grid(row=2,column=1)
                    Label(propframe,text=f"PINK PROPERTIES OWNED: {pink}",font=('Futura',12)).grid(row=3,column=1)
                    Label(propframe,text=f"ORANGE PROPERTIES OWNED: {orange}",font=('Futura',12)).grid(row=4,column=1)
                    Label(propframe,text=f"RED PROPERTIES OWNED: {red}",font=('Futura',12)).grid(row=5,column=1)
                    Label(propframe,text=f"YELLOW PROPERTIES OWNED: {yellow}",font=('Futura',12)).grid(row=6,column=1)
                    Label(propframe,text=f"GREEN PROPERTIES OWNED: {green}",font=('Futura',12)).grid(row=7,column=1)
                    Label(propframe,text=f"DARK BLUE PROPERTIES OWNED: {darkblue}",font=('Futura',12)).grid(row=8,column=1)

                    Label(propframe,text=f"RAILROADS: {rails}",font=('Futura',12)).grid(row=9,column=1)
                    Label(propframe,text=f"UTILITIES: {utilities}",font=('Futura',12)).grid(row=10,column=1)
                    Label(propframe,text=f"HOUSES: {house}",font=('Futura',12)).grid(row=11,column=1)
                    Label(propframe,text=f"HOTELS: {hotel}",font=('Futura',12)).grid(row=12,column=1)
                    Label(propframe,text=f"GET OUT OF JAILS: {gooj}",font=('Futura',12)).grid(row=13,column=1)


                    #MONEY DISPLAY
                    mframe=Frame(screen2,width=50,height=2)
                    mframe.grid(row=1,column=2)
                    money=player_data['player'+' '+i]['money']
                    mlabel=Label(mframe,text=f"MONEY: {money}",font=('Futura',12,'bold'))
                    mlabel.grid(row=0,column=1)

                    #PLACE DISPLAY
                    cframe1=Frame(screen2)
                    cframe1.grid(row=1,column=0)
                    place1=places[player_data['player'+' '+i]['position']]
                    place=place1.upper()
                    cardd=card[places[player_data['player'+' '+i]['position']]]
                    
                    
                    #colour display
                    color_disp=cardd['Colour']
                    if color_disp=='Purple':
                        cd=Label(cframe1,text=place,bg='purple',width=65,height=2,font=('Copperplate Gothic',12,'bold'),foreground='white')
                    elif color_disp=='Light Blue':
                        cd=Label(cframe1,text=place,bg='light blue',width=65,height=2,font=('Copperplate Gothic',12,'bold'))
                    elif color_disp=='Pink':
                        cd=Label(cframe1,text=place,bg='pink',width=65,height=2,font=('Copperplate Gothic',12,'bold'))
                    elif color_disp=='Orange':
                        cd=Label(cframe1,text=place,bg='orange',width=65,height=2,font=('Copperplate Gothic',12,'bold'))
                    elif color_disp=='Red':
                       cd=Label(cframe1,text=place,bg='red',width=65,height=2,font=('Copperplate Gothic',12,'bold'))
                    elif color_disp=='Yellow':
                        cd=Label(cframe1,text=place,bg='yellow',width=65,height=2,font=('Copperplate Gothic',12,'bold'))
                    elif color_disp=='Green':
                        cd=Label(cframe1,text=place,bg='green',width=65,height=2,font=('Copperplate Gothic',12,'bold'))
                    elif color_disp=='Dark Blue':
                        cd=Label(cframe1,text=place,bg='dark blue',width=65,height=2,font=('Copperplate Gothic',12,'bold'))
                    else:
                        cd=Label(cframe1,text=place,bg='gray',width=65,height=2,font=('Copperplate Gothic',12,'bold'))
                    cd.grid(row=0,column=0)


                    cframe=Frame(screen2)
                    cframe.grid(row=2,column=0)
                    C=Listbox(cframe,height=20,width=95,activestyle='dotbox',font=('Futura',10))
                    n=1
                    for c in cardd:
                        C.insert(n,(c,cardd[c]))
                        n+=1
                    n=0
                    
                    C.grid(row=1,column=0)


                    check_cond(player_data,card,i,dice_num,no_players)


                    #Bankrupcy and winning
                    if player_data['player'+' '+i]['money']<=0:
                        end=Toplevel(screen2)

                        image2=Image.open(r"logo.png")
                        logo2=image2.resize((275,115))
                        img=ImageTk.PhotoImage(logo2)
                        pic=Label(end,image=img)
                        pic.image=img
                        pic.grid(row=0,column=1)



                        Label(end,text=f"Player {i} Is Bankrupt",font=('Futura',14,'bold')).grid(row=1,column=0)

                        purp1=player_data['player'+' '+i]['property']['Purple']
                        lightblue1=player_data['player'+' '+i]['property']['Light Blue']
                        pink1=player_data['player'+' '+i]['property']['Pink']
                        orange1=player_data['player'+' '+i]['property']['Orange']
                        red1=player_data['player'+' '+i]['property']['Red']
                        yellow1=player_data['player'+' '+i]['property']['Yellow']
                        green1=player_data['player'+' '+i]['property']['Green']
                        darkblue1=player_data['player'+' '+i]['property']['Dark Blue']

                        rails1=player_data['player'+' '+i]['railroads']
                        utilities1=player_data['player'+' '+i]['utilities']
                        house1=player_data['player'+' '+i]['houses']
                        hotel1=player_data['player'+' '+i]['hotel']
                        gooj1=player_data['player'+' '+i]['get out of jail']
                        mon1=player_data['player'+' '+i]['money']

                        Label(end,text=("MONEY",mon1),font=('Futura',12)).grid(row=2,column=0)

                        Label(end,text=("PURPLE PROPERTIES OWNED:",purp1),font=('Futura',12)).grid(row=3,column=0)
                        Label(end,text=("LIGHT BLUE PROPERTIES OWNED:",lightblue1),font=('Futura',12)).grid(row=4,column=0)
                        Label(end,text=("PINK PROPERTIES OWNED:",pink1),font=('Futura',12)).grid(row=5,column=0)
                        Label(end,text=("ORANGE PROPERTIES OWNED:",orange1),font=('Futura',12)).grid(row=6,column=0)
                        Label(end,text=("RED PROPERTIES OWNED:",red1),font=('Futura',12)).grid(row=7,column=0)
                        Label(end,text=("YELLOW PROPERTIES OWNED:",yellow1),font=('Futura',12)).grid(row=8,column=0)
                        Label(end,text=("GREEN PROPERTIES OWNED:",green1),font=('Futura',12)).grid(row=9,column=0)
                        Label(end,text=("DARK BLUE PROPERTIES OWNED:",darkblue1),font=('Futura',12)).grid(row=10,column=0)

                        Label(end,text=("RAILROADS:",rails1),font=('Futura',12)).grid(row=11,column=0)
                        Label(end,text=("UTILITIES:",utilities1),font=('Futura',12)).grid(row=12,column=0)
                        Label(end,text=("HOUSES:",house1),font=('Futura',12)).grid(row=13,column=0)
                        Label(end,text=("HOTELS:",hotel1),font=('Futura',12)).grid(row=14,column=0)
                        Label(end,text=("GET OUT OF JAILS:",gooj1),font=('Futura',12)).grid(row=15,column=0)
                        


                       #winner display
                        win=str(winner(player_data,no_players))
                        #while_flag=False
                        Label(end,text=f"Player {win} Is The Winner",font=('Futura',14,'bold')).grid(row=1,column=2)

                        purp2=player_data['player'+' '+win]['property']['Purple']
                        lightblue2=player_data['player'+' '+win]['property']['Light Blue']
                        pink2=player_data['player'+' '+win]['property']['Pink']
                        orange2=player_data['player'+' '+win]['property']['Orange']
                        red2=player_data['player'+' '+win]['property']['Red']
                        yellow2=player_data['player'+' '+win]['property']['Yellow']
                        green2=player_data['player'+' '+win]['property']['Green']
                        darkblue2=player_data['player'+' '+win]['property']['Dark Blue']

                        rails2=player_data['player'+' '+win]['railroads']
                        utilities2=player_data['player'+' '+win]['utilities']
                        house2=player_data['player'+' '+win]['houses']
                        hotel2=player_data['player'+' '+win]['hotel']
                        gooj2=player_data['player'+' '+win]['get out of jail']
                        mon2=player_data['player'+' '+win]['money']

                        Label(end,text=("MONEY",mon2),font=('Futura',12)).grid(row=2,column=2)

                        Label(end,text=("PURPLE PROPERTIES OWNED:",purp2),font=('Futura',12)).grid(row=3,column=2)
                        Label(end,text=("LIGHT BLUE PROPERTIES OWNED:",lightblue2),font=('Futura',12)).grid(row=4,column=2)
                        Label(end,text=("PINK PROPERTIES OWNED:",pink2),font=('Futura',12)).grid(row=5,column=2)
                        Label(end,text=("ORANGE PROPERTIES OWNED:",orange2),font=('Futura',12)).grid(row=6,column=2)
                        Label(end,text=("RED PROPERTIES OWNED:",red2),font=('Futura',12)).grid(row=7,column=2)
                        Label(end,text=("YELLOW PROPERTIES OWNED:",yellow2),font=('Futura',12)).grid(row=8,column=2)
                        Label(end,text=("GREEN PROPERTIES OWNED:",green2),font=('Futura',12)).grid(row=9,column=2)
                        Label(end,text=("DARK BLUE PROPERTIES OWNED:",darkblue2),font=('Futura',12)).grid(row=10,column=2)

                        Label(end,text=("RAILROADS:",rails2),font=('Futura',12)).grid(row=11,column=2)
                        Label(end,text=("UTILITIES:",utilities2),font=('Futura',12)).grid(row=12,column=2)
                        Label(end,text=("HOUSES:",house2),font=('Futura',12)).grid(row=13,column=2)
                        Label(end,text=("HOTELS:",hotel2),font=('Futura',12)).grid(row=14,column=2)
                        Label(end,text=("GET OUT OF JAILS:",gooj2),font=('Futura',12)).grid(row=15,column=2)
                        
                    a+=1
                    if a==no_players:
                        a=0
                    
                        
            
        Button(screen2,text="ROLL DICE",command=nextplayer,font=('Futura',14,'bold'),background='#B71815',foreground='#FAF3EF').grid(row=3,column=1)


    Button(screen,text="START",width='30',height="2",command=start,font=('Copperplate Gothic',14,'bold'),background='#B71815',foreground='#FAF3EF').pack()
    screen.mainloop()
