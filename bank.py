#places={position:'place name'}
places = {1:"Start",2:"Mediterranean avenue",3:"Community chest",4:"Baltic avenue",5:"Income tax",6:"Reading railroad",
    7:"Oriental avenue",8:"Chance",9:"Vermont avenue",10:"Connecticut avenue",11:"Jail",12:"St. Charles place",13:"Electric company",
    14:"States avenue",15:"Virginia avenue",16:"Pennsylvania railroad",17:"St. James place",18:"Community chest",19:"Tennessee avenue",
    20:"New York avenue",21:"Free parking",22:"Kentucky avenue",23:"Chance",24:"Indiana avenue",25:"Illinois avenue",26:"B&O Railroad",
    27:"Atlantic avenue",28:"Ventnor avenue",29:"Water works",30:"Marvin gardens",31:"Go to Jail",32:"Pacific avenue",33:"North carolina",34:"Community chest",
    35:"Pennsylvania avenue",36:"Short line",37:"Chance",38:"Park place",39:"Luxury tax",40:"Broadway"}


#these lists are used for generating the card dictionary
property_buy=[0,60,0,60,0,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,220,0,220,240,200,260,260,150,280,0,300,300,0,320,200,0,350,0,400]

property_rent=[0,2,0,4,0,{'rent':25,'2 RRs are owned':50,'3 RRs are owned':100,'4 RRs are owned':200},6,0,6,8,0,10,
            {'1 utility owned':'d*4','2 utilities owned':'d*10'},10,12,{'rent':25,'2 RRs are owned':50,'3 RRs are owned':100,'4 RRs are owned':200},14,0,
            14,16,0,18,0,18,20,{'rent':25,'2 RRs are owned':50,'3 RRs are owned':100,'4 RRs are owned':200},22,22,
            {'1 utility owned':'d*4','2 utilities owned':'d*10'},24,0,26,26,0,28,
            {'rent':25,'2 RRs are owned':50,'3 RRs are owned':100,'4 RRs are owned':200},0,35,0,50]

color=[None,"Purple",None,"Purple",None,"Railroad","Light Blue",None,"Light Blue","Light Blue",None,"Pink","Utitlity","Pink","Pink","Railroad","Orange",None,"Orange","Orange",
    None,"Red",None,"Red","Red","Railroad","Yellow","Yellow","Utility","Yellow",None,"Green","Green",None,"Green","Railroad",None,"Dark Blue",None,"Dark Blue"]

house_buy=[0,50,0,50,0,0,50,0,50,50,0,100,0,100,100,0,100,0,100,100,0,150,0,150,150,0,150,150,0,150,0,200,200,0,200,0,0,200,0,200]

hotel_buy=[0,50,0,50,0,0,50,0,50,50,0,100,0,100,100,0,100,0,100,100,0,150,0,150,150,0,150,150,0,150,0,200,200,0,200,0,0,200,0,200]

house1_rent=[0,10,0,20,0,0,30,0,30,40,0,50,0,50,60,0,70,0,70,80,0,90,0,90,100,0,110,110,0,120,0,130,130,0,150,0,0,175,0,200]

house2_rent=[0,30,0,60,0,0,90,0,90,100,0,150,0,150,180,0,200,0,200,220,0,250,0,250,300,0,330,330,0,350,0,390,390,0,450,0,0,500,0,600]

house3_rent=[0,90,0,180,0,0,270,0,270,300,0,450,0,450,500,0,550,0,550,600,0,700,0,700,750,0,800,800,0,850,0,900,900,0,1000,0,0,1100,0,1400]

house4_rent=[0,160,0,320,0,0,400,0,400,450,0,625,0,625,700,0,750,0,750,800,0,875,0,875,925,0,975,975,0,1025,0,1100,1100,0,1200,0,0,1300,0,1700]

hotel_rent=[0,250,0,450,0,0,550,0,550,600,0,750,0,750,900,0,950,0,950,1000,0,1050,0,1050,1100,0,1150,1150,0,1200,0,1275,1275,0,1400,0,0,1500,0,2000]

community_chest = {
    1: "advance to start.+200$",
    2: "Bank error in your favor. Collect $200.",
    3: "Doctor's fees. Pay $50.",
    4: "From sale of stock you get $50.",
    5: "get out of jail free",
    6: "go to jail",
    7: "Grand Opera Night.Buy tickets for $50",
    8: "Holiday Fund matures. Receive $100. ",
    9: "Income tax refund. Collect $20.",
    10: "It's your birthday. Collect $10",
    11: "Life insurance matures. Collect $100",
    12: "Hospital Fees. Pay $50.",
    13: "School fees. Pay $50. ",
    14: "Receive $25 consultancy fee.",
    15: "You are assessed for street repairs: Pay $40 per house and $115 per hotel you own.",
    16: "you have won second prize in a beauty contest. Collect $10."
}

chance_c = {
    1: "Advance to Go. Collect $200",
    2: "Advance to Illinois Ave.",
    3: "Advance to St. Charles Place.",
    4: "Advance token to the nearest Utility",
    5: "Advance to the nearest Railroad.",
    6: "Bank pays you dividend of $50. ",
    7: "get out of jail free",
    8: "Go back three spaces",
    9: "go to jail",
    10: "Make general repairs on all your property: For each house pay $25",
    11: "Take a trip to Reading Railroad.",
    12: "Take a walk on the Boardwalk.",
    13: "You have been elected Chairman of the Board. Pay each player $50.",
    14: "Your building loan matures. Receive $150.",
    15: "Pay school tax of $150",
    16: "Parking fine $15"
}


#function to allot money, position, etc to each player at the begining of the game
#the values of this dictionary changes along the way in the game
def allot_values(n): #n=number of players
    d={}
    for i in range(n):
        d['player'+' '+str(i+1)]={}
        d['player'+' '+str(i+1)]['money']=500
        d['player'+' '+str(i+1)]['position']=0
        d['player'+' '+str(i+1)]['property']={} #{'colour':'places owned by the player'}

        d['player'+' '+str(i+1)]['property']['Purple']=[]
        d['player'+' '+str(i+1)]['property']['Light Blue']=[]
        d['player'+' '+str(i+1)]['property']['Pink']=[]
        d['player'+' '+str(i+1)]['property']['Orange']=[]
        d['player'+' '+str(i+1)]['property']['Red']=[]
        d['player'+' '+str(i+1)]['property']['Yellow']=[]
        d['player'+' '+str(i+1)]['property']['Green']=[]
        d['player'+' '+str(i+1)]['property']['Dark Blue']=[]

        d['player'+' '+str(i+1)]['railroads']=[] 
        d['player'+' '+str(i+1)]['utilities']=[]
        d['player'+' '+str(i+1)]['houses']={} #{'place': number of houses}
        d['player'+' '+str(i+1)]['hotel']=[] #list of places that have hotels
        d['player'+' '+str(i+1)]['get out of jail']=0 #no. of get out of jail cards you have from com chest and chance
        d['player'+' '+str(i+1)]['round']=1
    return d



def cards(): #returns a dictionary of title deed cards with property name as key and property details as values
    card={}
    for i in range(40):
        if property_rent[i]!=0:
            if type(property_rent[i])==int:
                d={"Colour":color[i],
                "Property cost":property_buy[i],
                "Rent":property_rent[i],
                "Rent with 1 house":house1_rent[i],
                "Rent with 2 houses":house2_rent[i],
                "Rent with 3 houses":house3_rent[i],
                "Rent with 4 houses":house4_rent[i],
                "Rent with hotel":hotel_rent[i],
                "House cost":house_buy[i],
                "Hotel cost":hotel_buy[i]}
                
            elif type(property_rent[i])==dict: #railroads and utilities 
                d={"Colour":color[i],
                "Property cost":property_buy[i],
                "Rent":property_rent[i]}
                
        else: #start, community chest, chance
            d={"Colour":color[i],
            "You have landed on":places[i+1]}
            
        card[places[i+1]]=d
    return card #card has all the details that should be printed on the screen
