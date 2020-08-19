

# checking for health
def check(health, a,b):
    if health<=0:
        print('You Died')
        exit()
    if health<2:
        health = health + b
        return health
    if health>7:
        health = 7
        return health
    else:
        pass

# Leave
def leave(health,a):
    print('1> Eat: Type-> eat\n 2> Hunting: Type-> hunt\n3> search for work: Type-> work\n4> fishing: Type-> fish')
    i = input('Your choice:')
    if i == 'fish':
        health = health - 1
        check(health,a,b)
        eat(health,a,health_range)
        return health,a,b
    if i == 'fish':
        health = health - 1
        check(health,a,b)
        fishing(health,a,b)
        return health,a,b
    if i == 'hunt':
        health = health - 1
        check(health,a,b)
        hunting(health,a,b)
        return health,a,b
    if i == 'work':
        health = health - 1
        check(health,a,b)
        work(health,a,b)
        return health,a,b

# Eating
def eat(health,a,health_range):
    health = health - 1
    check(health,a,b)
    print('oh i am soo hungry, its my favorite place')
    print('what should I eat \n1> chicken (will increase ur hunger points range to 2 palce and give u 1 health point but cost u 50 coins): Type-> chicken\n2> veg. dish (will fill your health full but cost u 30): Type-> veg\n3> leave: type-> leave')
    i = input('Your choice:')
    if i == 'chicken':
        health_range += 2
        check(health,a,b)
        a = a - 50
        return health,a,health_range
    if i == 'veg':
        health = health - 1
        check(health,a,b)
        a = a - 30
    else:
        leave(health,a)
    
# working
def work(health,a,b):
    health = health - 1
    check(health,a,b)
    print('got work of 3 hrs(wil cost 3 health points) and will get me 50 coins')
    print('1>to work: Type-> work\n2> leave: type->leave')
    i = input('Your choice:')
    if i == 'work':
        health = health - 3
        check(health,a,b)
        print('I have done my work and it got me 50 coins soo good!')
        a = a+50
    else:
        leave(health,a)

# Fishing
def fishing(health,a,b):
    health -= 1
    check(health,a,b)
    print('1> Bait fish: Type-> fish\n 2> leave: Type-> leave\n3> Hear someone talk to your right: Type-> right\n4> Hear someone talk to your left: Type-> left')
    i = input('Your choice:')
    if i == 'fish':
        health = health - 1
        check(health,a,b)
        print('did not get any fish')
        print('1> Bait again: type-> fish\n2> leave: type-> leave')
        i = input('Your choice:')
        if i == 'fish':
            health = health - 1
            check(health,a,b)
            print('did not get any fish')
            print('1> Bait again: type-> fish\n2> leave: type-> leave')
            i = input('Your choice:')
            if i == 'fish':
                health = health - 1
                check(health,a,b)
                print('gained 1 fish (eat it and will get 3 additional health)')
                b = b+3 
            if i == 'leave':
                health = health - 1
                check(health,a,b)
                leave(health,a)
        if i == 'leave':
            health = health - 1
            check(health,a,b)
            leave(health,a)
    if i == 'leave':
        health = health - 1
        check(health,a,b)
        leave(health,a)
    
    if i == 'right':
        health = health - 1
        check(health,a,b)
        print('people talking about treasure in hola island, may be 10 lakh silver coins')
        print('\n1> Bait again: type-> fish\n2> leave: type-> leave\n3> Hear someone talk to your left: Type-> left')
        i = input('Your choice:')
        if i == 'fish':
            health = health - 1
            check(health,a,b)
            print('did not get any fish')
            print('1> Bait again: type-> fish\n2> leave: type-> leave')
            i = input('Your choice:')
            if i == 'fish':
                health = health - 1
                check(health,a,b)
                print('gained 1 fish (eat it and will get 3 additional health)')
                b = b+3 
            if i == 'leave':
                health = health - 1
                check(health,a,b)
                leave(health,a)
        if i == 'leave':
            health = health - 1
            check(health,a,b)
            leave(health,a) 
        if i == 'left':
            health = health - 1
            check(health,a,b)
            print('people talking about a haunted house of rich people abondand long ago still ghost protect that place, may be 5 lakh silver coins')
            print('1> Bait again: type-> fish\n2> leave: type-> leave')
            i = input('Your choice:')
            if i == 'fish':
                health = health - 1
                check(health,a,b)
                print('gained 1 fish (eat it and will get 3 additional health)')
                b = b+3 
            if i == 'leave':
                health = health - 1
                check(health,a,b)
                leave(health,a)
    if i == 'left':
        health = health - 1
        check(health,a,b)
        print('people talking about a haunted house of rich people abondand long ago still ghost protect that place, may be 5 lakh silver coins')
        print('\n1> Bait again: type-> fish\n2> leave: type-> leave\n3> Hear someone talk to your right: Type-> right')
        i = input('Your choice:')
        if i == 'fish':
            health = health - 1
            check(health,a,b)
            print('did not get any fish')
            print('1> Bait again: type-> fish\n2> leave: type-> leave')
            i = input('Your choice:')
            if i == 'fish':
                health = health - 1
                check(health,a,b)
                print('gained 1 fish (eat it and will get 3 additional health)')
                b = b+3 
            if i == 'leave':
                health = health - 1
                check(health,a,b)
                leave(health,a)
        if i == 'leave':
            health = health - 1
            check(health,a,b)
            leave(health,a) 
        if i == 'right':
            health = health - 1
            check(health,a,b)
            print('people talking about treasure in hola island, may be 10 lakh silver coins')
            print('1> Bait again: type-> fish\n2> leave: type-> leave')
            i = input('Your choice:')
            if i == 'fish':
                health = health - 1
                check(health,a,b)
                print('gained 1 fish (eat it and will get 3 additional health)')
                b = b+3 
            if i == 'leave':
                health = health - 1
                check(health,a,b)
                leave(health,a)
# Hunting
def hunting(health,a,b):
    health -= 1
    check(health,a,b)
    print('1> search for animal: Type-> search\n 2> leave: Type-> leave\n3> hear people living inside the house: Type-> house')
    i = input('Your choice:')
    if i == 'search':
        health = health - 1
        check(health,a,b)
        print('did find an animal to hunt')
        print('1> search for animal: Type-> search\n2> leave: type-> leave')
        i = input('Your choice:')
        if i == 'search':
            health = health - 1
            check(health,a,b)
            print('did find an animal to hunt')
            print('1> search for animal: Type-> search\n2> leave: type-> leave')
            i = input('Your choice:')
            if i == 'search':
                health = health - 1
                check(health,a,b)
                print('find an animal (eat it and will get 5 additional health)')
                print('want to continue, 1> kill him and get 5 aditional health but will take ur 2 health points: type-> kill or\n2> leave: leave ')
                i = input('your choice:')
                if i == 'kill':
                    health = health - 2
                    check(health,a,b)
                    b = b+5
                else:
                    health = health - 1
                    check(health,a,b)
                    pass
            if i == 'leave':
                health = health - 1
                check(health,a,b)
                leave(health,a)
        if i == 'leave':
            health = health - 1
            check(health,a,b)
            leave(health,a)
    if i == 'leave':
        health = health - 1
        check(health,a,b)
        leave(health,a)
    
    if i == 'house':
        health = health - 1
        check(health,a,b)
        print('people talking about to kill a mafia and get all his wealth, wealth is unknown')
        print('\n1> search for animal again: type-> search\n2> leave: type-> leave\n')
        i = input('Your choice:')
        if i == 'search':
            health = health - 1
            check(health,a,b)
            print('did find an animal to hunt')
            print('1> search for animal again: type-> search\n2> leave: type-> leave')
            i = input('Your choice:')
            if i == 'search':
                health = health - 1
                check(health,a,b)
                print('find an animal (eat it and will get 5 additional health)')
                print('want to continue, 1> kill him and get 5 aditional health but will tske ur 2 health points: type-> kill or\n2> leave: leave ')
                i = input('your choice:')
                if i == 'kill':
                    health = health - 2
                    check(health,a,b)
                    b = b+5
                else:
                    health = health - 1
                    check(health,a,b)
                    pass
            if i == 'leave':
                health = health - 1
                check(health,a,b)
                leave(health,a)
        if i == 'leave':
            health = health - 1
            check(health,a,b)
            leave(health,a) 

print('Creator-> This is the journey of a poor man came across different struggles, only u the user can help him to get him what u wanted\n')
print('Rules\n1> with every step u take one health point is reduced. you have a total of 7. different situation can change the value of reduction.\n2>u start with only 40 coins.\n3> Your action can lead u to differnt situation. choose carefully.\n4> All the best.')
print('\n Hi, My name is Tiku. I think today is going to be as always, leaving home and coming back with just a little coins for living.\nGod please hear my prayer, at least give me some thing for my good works I have done so far.\n')
print('\n Today I only have 40 coins, how will I be tummy full today. Lets go earn and live my boring life')
a = 40
health_range = 7
health = 7
b = 0

# First Step:
print('(Tiku came out of the house) oh no were to go today, should I take right path or left')
print('1> For Right path: Type-> right\n 2> For Left path: Type-> left')
i = input('Your Choice:')
if i == 'right':
    health = health - 1
    print('(In his path towards he see people doing fishing which he loves and also it fulfill his hunger) I love fishing but I want to go and search for work for living')
    print('1> Go fishing: Type-> fish\n2> Search for work: Type-> work\n3>Eat: Type-> eat')
    i = input('Your choice:')
    if i== 'fish':
        health = health - 1
        check(health,a,b)
        fishing(health,a,b)
    if i == 'work':
        health = health - 1
        check(health,a,b)
        work(health,a,b)
    if i == 'eat':
        health = health - 1
        check(health,a,b)
        eat(health,a,b)

if i == 'left':
    health = health - 1
    print('(In his path towards he sees the jungle he usually come to hunt to fulfill his hunger) I love fishing but I want to go and search for work for living')
    print('1> Go Hunting: Type-> hunt\n 2> Search for work: Type-> work\n3>Eat: Type-> eat')
    i = input('Your choice:')
    if i== 'hunt':
        health = health - 1
        check(health,a,b)
        hunting(health,a,b)
    if i == 'work':
        health = health - 1
        check(health,a,b)
        work(health,a,b)
    if i == 'eat':
        health = health - 1
        check(health,a,b)
        eat(health,a,b)


print('what a stressfull day')
print('1> should I go for hola island: type-> hola\n2> or go for the haunted house: type-> haunted\n3> or kill mafia that can be a good work: type-> mafia\n4> mystery place: type-> mystery\n5> leave: type->leave\n6> Quit game: type-> quit')        
print('(Note:-Before i go for looking for hiest first I should be prepared)')
i = input('Your choice')

# Quit
if i == 'quit':
    print('Thanks for playing game')
    exit()

# leave
if i == 'leave':
    leave(health,a)

# hola island
if i == 'hola':
    health = health - 1
    check(health,a,b)
    print('Man rumers spread very fast. Shit, 10 more people looking for the treasure')
    print('oh no no, i see one guy rowing his boat towards the island. I will have to get there early. According to my estimate it will take him approx 2.5 hrs to gat to the island')
    print('\n1>should I buy boat and row for 2.5 hrs ( cost me 10 coins): type-> boat\n2>should I call my frind and use his motor boat, pay him 30 ( it will take me only 1 hr): motor\n3>or I should borrow jet ski it is much faster the motor boat will ahve to wait for 1 hr(cost me 50 coins): type-> jet')
    i = input('Your choice:')
    if i == 'boat':
        health = health - 2.5
        check(health,a,b)
        a = a - 10
        print('5 more arrived with me 2 are ahead')
        print('\n1> should I team up with these 5 and kill the 2 ahead (will get 1/5 of money): team\n2> or I should be lonewolf hahaha no be serious Tiku(chance of getting 10 lakh silver coins): type-> lone')
        i = input('Your choice:')
        if i == 'team':
            print("health will reduce to 2 because to kill 2 people")
            health = health - 2
            check(health,a,b)
            print('look for treasure everyone')
            print('\n1> search for treasure( cost me 5 health points): type-> search\n2> leave for home: type-> home')
            i = input('Your choice:')
            if i == 'search':
                health = health - 5
                check(health,a,b)
                print('Yes, got a treasure')
                print('I earned',2+' lakh silver coins')
                print('Note-> you earn what u got but losse the good person inside you. You are a killer')
                exit()
        

        if i == 'lone':
            print('Remember Tiku my chance is low and might be killed by others be carefull')
            health = health - 1
            check(health,a,b)
            print('I see bear. My god, he is comming to me')
            print('1>run away back home: type-> run\n2> kill him and will take me my 3 health points: type-> kill')
            if i == 'run':
                health = health - 1
                check(health,a,b)
                print('I ran away I got scared\n will have to live like this forever')
                print('I have only:',a+' coins')
                exit()
            if i == 'kill':
                health = health - 3
                check(health,a,b)
                print('oh man I killed him somehow')
                b = b + 2
                print('got something to eat')
                print('Now what to do\n1> should I kill everyone( cost me 7 health points ): type-> kill\n2> leave for home: type-> home')
                i = input('Your choice')
                if i == 'kill':
                    health = health - 7
                    check(health,a,b)
                    print('Man I killed every one. Shit I am very bad')
                    print('\nlooking for treasure (cost me 2 health points)')
                    health = health - 2
                    check(health,a,b)
                    print('Yes, I got it whow man yes. I am now rich')
                    print('You have won:',10+'lakh silver coins')
                    print('Note-> Not a good way to win you have killed 7 people you are bad')
                    exit()
                if i == 'home':
                    health = health - 1
                    check(health,a,b)
                    print('I did not got treasure but I did not go to kill any person this is a win for me')
                    print('Note-> You are a good guy Tiku')
                    exit()

    if i == 'motor':
        health = health - 2
        check(health,a,b)
        a = a - 30
        print('I am with 2 guys and we are ahead')
        print('\n1> should I team up with these 2 (will get 1/3 of money): team\n2> or I should be lonewolf hahaha no be serious Tiku(chance of getting 10 lakh silver coins): type-> lone')
        i = input('Your choice:')
        if i == 'team':
            print("bear on our way lets kill him (cost me 5 health points")
            health = health - 5
            check(health,a,b)
            print('look for treasure everyone')
            print('\n1> search for treasure( cost me 10 health points): type-> search\n2> leave for home: type-> home')
            i = input('Your choice:')
            if i == 'search':
                health = health - 10
                check(health,a,b)
                print('Yes, got a treasure')
                print('I earned',3.33 +' lakh silver coins')
                print('Note-> Now u can live a good life')
                exit()
        

        if i == 'lone':
            print('Remember Tiku my chance is low and might be killed by others be carefull')
            health = health - 1
            check(health,a,b)
            print('I see bear. My god, he is comming to me')
            print('1>run away back home: type-> run\n2> kill him and will take me my 3 health points: type-> kill')
            if i == 'run':
                health = health - 1
                check(health,a,b)
                print('I ran away I got scared\n will have to live like this forever')
                print('I have only:',a+' coins')
                exit()
            if i == 'kill':
                health = health - 3
                check(health,a,b)
                print('oh man I killed him somehow')
                b = b + 2
                print('got something to eat')
                print('Now what to do\n1> should I kill everyone( cost me 10 health points ): type-> kill\n2> leave for home: type-> home')
                i = input('Your choice')
                if i == 'kill':
                    health = health - 10
                    check(health,a,b)
                    print('Man I killed every one. Shit I am very bad')
                    print('\nlooking for treasure (cost me 2 health points)')
                    health = health - 2
                    check(health,a,b)
                    print('Yes, I got it whow man yes. I am now rich')
                    print('You have won:',10+'lakh silver coins')
                    print('Note-> Not a good way to win you have killed 2 people you are bad')
                    exit()
                    

    if i == 'jet':
        health = health - 1.75
        check(health,a,b)
        a = a - 50
        print('I am ahead of every one')
        print('\n1> should I team up with the 2 comming behind me(will get 1/3 of money): team\n2> or I should be lonewolf hahaha no be serious Tiku(chance of getting 10 lakh silver coins): type-> lone')
        i = input('Your choice:')
        if i == 'team':
            print("bear on our way lets kill him (cost me 6 health points")
            health = health - 6
            check(health,a,b)
            print('look for treasure everyone')
            print('\n1> search for treasure( cost me 12 health points): type-> search\n2> leave for home: type-> home')
            i = input('Your choice:')
            if i == 'search':
                health = health - 12
                check(health,a,b)
                print('Yes, got a treasure')
                print('I earned',3.33 +' lakh silver coins')
                print('Note-> Now u can live a good life')
                exit()
        

        if i == 'lone':
            print('Remember Tiku my chance is low and might be killed by others be carefull')
            health = health - 1
            check(health,a,b)
            print('I see bear. My god, he is comming to me')
            print('1>run away back home: type-> run\n2> kill him and will take me my 8 health points: type-> kill')
            if i == 'run':
                health = health - 1
                check(health,a,b)
                print('I ran away I got scared\n will have to live like this forever')
                print('I have only:',a+' coins')
                exit()
            if i == 'kill':
                health = health - 8
                check(health,a,b)
                print('oh man I killed him somehow')
                b = b + 2
                print('got something to eat')
                
                print('\nlooking for treasure (cost me 5 health points)')
                health = health - 5
                check(health,a,b)
                print('Yes, I got it whow man yes. I am now rich')
                print('You have won:',10+'lakh silver coins')
                print('Note-> congrats Tiku you are rich now')
                exit()

# Haunted 
if i == 'haunted':
    print('Note-> this is a haunted place health will reduce with 2 times per step')
    health = health - 2
    check(health,a,b)
    print('Man I see one more guy behind me looking to get inside the house.\nMan I hate ghosts.')
    print('\n1> should I join him (get 1/2 of the treasure): type-> join\n2> I will go alone, I cant share the treasure: type-> alone')
    i = input('Your choice')
    if i == 'join':
        health = health - 2
        check(health,a,b)
        print('Man it is so scary place, please stay together beacause you have a gun we can get through it.')
        print('1> search (cost me 5 health points): type-> search\n2> leave : type-> leave')
        i = input('Your choice:')
        if i == 'search':
            health = health - 7
            check(health,a,b)
            print('Man there is someone I see green Eyes')
            print('\n1> Man shoot him: type-> shoot\n2> wait : type-> wait')
            i = input('Your choice:')
            if i == 'shoot':
                health = health - 2
                check(health,a,b)
                print('Thank god u saved me if we get the treasure I will give u 1 lakh with my side as a gift. please dont refuse it')
                print('saying to myself in my head-> Man I see something this can be it yes should I leave him or tell him')
                print('1> search and tell(cost me 5 health points): type-> tell\n2> leave : type-> alone')
                i = input('Your choice:')
                if i == 'alone':
                    health = health - 7
                    check(health,a,b)
                    print('yes i see it yes lets hurry and leave')
                    print('Man ghost in house protecting the treasure')
                    print('Another man: You fooled me i will kill u')
                    print('1> give him 50 thousand more and survive: type-> give\n2> I cant give more: type-> no')
                    if i == 'give':
                        health = health - 2
                        check(health,a,b)
                        print('thanks for not killing me and protecting me from everything')
                        print('you take 1.5 lakh silver coins from me thanks')
                        print('I earn 1 lakh coins')
                        exit()
                    if i == 'no':
                        health = health - 2
                        check(health,a,b)
                        print('you died')
                        exit()
                if i == 'tell':
                    health = health - 7
                    check(health,a,b)
                    print('thanks for protecting me from everything')
                    print('you take 1 lakh silver coins from me thanks')
                    print('I earn 1.5 lakh coins')
                    exit()



        if i == 'leave':
            health = health - 2
            check(health,a,b)
            print('I cant be at this place it so scary')
            print('I will love to live as always then searching inside')
            print('Note-> You are scared of thing, yiu cant do anything')
            exit()

# Mafia place 
if i == 'mafia':
    print('Note-> this is a dangerous place health will reduce with 3 times per step')
    health = health - 3
    check(health,a,b)
    print('Man I see 15 people guarding th place with the gun and 2 more guys came here for the treasure')
    print('\n1> Team up (treasure will distributed 1/3): type-> team\n2> alone : type-> alone')
    i = input('Your choice:')
    if i == 'team':
        health = health - 3
        check(health,a,b)
        print('Listen everyone lets assassinate them one bye one (cost me 10 health points): type-> kill\n leave : type-> leave')
        i = input('Your choice:')
        if i == 'leave':
            health = health - 3
            check(health,a,b)
            print('I cant kill soo many people, it is good to be save now ')
            print('NOte-> You Did not earn anything')
            exit()
        
        if i == 'kill':
            health = health - 13
            check(health,a,b)
            print('yes guys we did it now search for the leader (searching will cost 10 health points)')
            health = health - 13
            check(health,a,b)
            print('I found him\n1> kill him (cost me 5): type-> kill\n2> kill one of urs( cost me 15): type-> one')
            i = input('Your choice:')
            if i == 'kill':
                health = health - 7
                check(health,a,b)
                print('Yes we did it we are rich now')
                print('I got 20 lakh silver coins')
                exit()
            if i == 'one':
                health = health - 18
                check(health,a,b)
                print('I did it so that we can get more of our money')
                print('I got 30 lakh silver coins')
                print('Note-> u did get rich but came out as a bad man u are a killer')
                exit()
    
    if i == 'alone':
        health = health - 3
        check(health,a,b)
        print("i will have to kill all 2 people first which are looking for the treasure too")
        print('1> kill 2 (cost me 30): type-> kill\n 2> kill 15 alone (cost me 150): type-> yo')
        i = input('Your choice:')
        if i == 'yo':
            health = health - 153
            check(health,a,b)
            print('Yes I did it')
            print('I earn 60 lakh silver coins. Now I can rule this place')
            print('Note-> U become rich but loose humanity')
            exit()
        
        if i == 'kill':
            health = health - 33
            check(health,a,b)
            print('u dies as some one saw u killing and shot u dead')
            print('Note-> being greeding killed u. You are a looser')
            exit()

# mystery 
if i == 'mystery':
    print('Note-> You cant get to myster place as it is a mystery too')
    print('You lost and will live like always')
    exit()