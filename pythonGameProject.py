from pygame import mixer
mixer.init()
mixer.music.load("lost-soul_30sec-177569.mp3")
mixer.music.play(-1)

import sys
global clue, key
clue=0
global susList
susList={"Maid", "Butler"}
key=0

def result():
    print("Take the final guess...")
    print("Who did the murder?")
    culprit = input("a for Wife |b for Son- Lewis | c for Butler Sebastian | d for Secretary David | e for Business Partner")
    if (culprit == "e"):
        print("DNA Test are here...")
        print("The DNA found on was of...")
        print("Ex Business partner - Mr. baker!")
        print("You have successfully solved the case! You have acquired a promotion and a trip to Spain!")
        sys.exit()
    elif (culprit == "a" or culprit == "b" or culprit == "c" or culprit == "d"):
        print("DNA tests were tampred with...")
        print("Higher power and people with influence interferred with your investiigation and you failed to solve the case!")
        print("Mr. Baker had plooted the murser of his rival!")
        print("You have failed!")
        print("You were demoted and sent to a small village!")
    else:
        print("The game is over!")

def hints():
    hint = input("1 - for first hint | 2 - for second hint")
    if (hint == "1"):
            text = """
Numbers in play, what do they say? Sequence align, letters in line. Crack the code, and follow the road!
            
Match up the numbers to their respective alphabets to get the answer!
            
1.A     2.B     3.C     4.D     5.E     6.F     7.G     8.H     9.I     10.J    11.K   12.L     13.M
14.	N   15.O    16.P    17.Q    18.R    19.S    20.T    21.U    22.V    23.W    24.X    25.Y    26.Z
            """
            print(text)
            clue_guess()
    elif(hint == "2"):
            text = """
            There are only 5 words in this code!
            Only the 1st letter of the first word is in capital letter!"""
            print(text)
            clue_guess()

def check_user_input(user_input):
    expected_sentence = "My partner wants my business"
    if user_input == expected_sentence:
        print("You are Correct!")
        #goodf()
        sus2=input("How do want to proceed: a) Add suspect b) come back later?")
        if (sus2 == "a"):
            susList.add("Business partner")
            susList.add("Wife")
            decipher_clues()
        else:
            print("come back later")
            decipher_clues()
    else:
        print("Wrong guess...")
        clue_guess()
        
def clue_guess():
     message=input("Do you want to solve the clue (a)or do you want a hint(b)?")
     if (message == "a"): 
         user_sentence = input("Enter the sentence: ")
         check_user_input(user_sentence)
     elif (message == "b"):
         hints()
     else:
         print("Try again")
         clue_guess()
         

def decipher_clues():
    print("(a) Hidden Document in Mr Streling's Study Room | (b) Hidden cryptic code on Mr Streling's computer | (c) a Diary entry in Mr. Streling's daily diary")
    entry2 = input("How do you want to proceed (a, b, or c)?")
    global count
    count =0
    if entry2 == "a":
        count = count +1
        print("You have found a Hidden Document!The contents of the document are as follows: \n")
        text="""
Confidential Correspondence
Subject: Urgent Request

Mr. Victor Sterling,

Since my mother's passing, I face daunting financial challenges. Your bond with her holds immense value, and I find myself in a vulnerable position. Your name was synonymous with trust in her eyes.
I appeal to that trust, hoping you'll consider including me in your will. Your acknowledgment would not only alleviate my financial strain but honor the enduring legacy of your connection with my late mother.

I approach this request with humility, understanding its sensitivity, and sincerely hope you'll grant me the solace and security I seek in this uncertain time.

Respectfully,

David Lewis
Secretary, Sterling Enterprises"""
        print(text)
        sus1=input("Do you want to Add Mr. Sectrary as a suspect?(y/n)")
        if(sus1=='y'):
            global susList
            susList.add("Secretary")
            
            decipher_clues()
        else:
            print("Let's move forward...")
            decipher_clues()
    elif entry2 == "b":
        count = count +1
        #goodf()
        text="""
            You explore the computer with the help of your IT specialist.
            Your team has found a hidden file...
            File contains a encrypted message...
            13 25	16 1 18 20 14 5 18	23 1 14 20 19	13 25	2 21 19 9 14 5 19 19"""
        print(text)
        clue_guess()
        
    elif (entry2 == "c"):
        count = count +1
        #badf()
        print("You have found Mr. Sterling's dialy diary!The contents of the diary entry is as follows: \n")
        text="""
I am teired today - [26-11-23]
Today's clash with David, my son, was intense. 
He's eager for control, but I believe he needs time to mature in the business. 
Our argument grew heated; he feels I don't trust his capabilities, underestimating his potential. 
This tension weighs heavily on me – torn between paternal concern and the need for a gradual handover. 
I hope time and understanding will mend this fractured relationship."""
        print(text)
        sus1=input("Do you want to Add Sterling's Son - Lewis as a suspect?(y/n)")
        if(sus1=='y'):
            susList.add("Son")
            
            #badf()
            #decipher_clues()
            initial_decision()
    else:
        decipher_clues()
        
def witness():
    print("who do you want to interrogate?")
    suspect = input("a for Wife |b for Son- Lewis | c for Butler Sebastian | d for Secretary David | e for Business Partner")
    def switch_case(argument):
        if argument == 'a':
            text="""
Interrogation with the Wife - Mrs. Sterling...
You: Good afternoon, Mrs. Sterling. I offer my condolences for your loss.

Mrs. Sterling: Thank you, detective. Although, I would appritiate if we could get this over with, as soon as possible..

You: How would you describe your relationship with Mr. Sterling, Mrs. Sterling?

Mrs. Sterling: Victor and I... well, our marriage was more a facade than a bond, detective. We drifted apart.

You: Were there any individuals your husband might have had conflicts with?

Mrs. Sterling: Victor was a businessman; disagreements were part of it. But he didn't hold grudges personally. Although, same cannot be said about his business partner...

You: What about your son, David? I heard they had their share of disagreements.

Mrs. Sterling: Yes, they clashed, but David loved his father. He wouldn't do this! They argued about the business, but David is innocent. He couldn't have harmed his father.

You: I understand, Mrs. Sterling. Your defense of David is noted. We'll explore every angle to find the truth.

Mrs. Sterling: No! No... You don't understand. He would never do this!
You: I understand, Mrs. Sterling..."""
            print (text)
            witness()
        elif argument == 'b':
            #goodf()
            text = """
Interrogation with the Son- David ...
You: Good afternoon, David. I appreciate you taking the time to speak with me.

David: Of course, detective. Anything to find out the truth...

You: You and your father had disagreements. Could you elaborate?

David: Yeah, we did. It was always about the business. He never trusted my judgment. I am young, but ambitious, he won't let me take over...'

You: But would you say your disagreements ever turned hostile or violent?

David: No. We argued, sure, but I'd never hurt my dad. We just saw things differently.

You: Now that he is dead, wouldn't it be easier for you to take over?

David: What are you impyling, detective! he was my father!

You: Mrs. Sterling insists you wouldn't harm your father. She defends you fiercely.

David: My mom's right. I wouldn't hurt him. We had our issues, but I'd never go that far.

You: Understood, David. Can you tell me if there were any business enemies of your father.

David : Not that I know of - No wait! Recently, my father's business partner broke off from the company...i don't know the full details, but their relation seemed sour.

You: Thank you for your cooperation. We'll do our best to find the truth.

David: I just want to know what happened, detective. He didn't deserve this."""
            print (text)
            witness()
        elif argument == 'c':
            text = """
Interrogation with Mr Butler - Sebastian.
You: Good afternoon, Mr. Butler. Your cooperation in this matter is crucial. Can you tell me about your relationship with Mr. Sterling?

Butler: Of course, detective. I've served the Sterling family for years, but my relationship with Mr. Sterling was professional.

You: You had access to the study where the incident occurred. Could you explain your movements that day?

Butler: Indeed, detective. I was tidying up the study earlier that day. Mr. Sterling asked me to rearrange some documents. At night, I was in the servant's block. the next morning when i came to clean the study room, I discovered Mr. Sterling body...And I informed Everyone immediately.

You: You were the only one with the key to that room. Is there a reason I should not suspect you?

Butler: I assure you, detective, my loyalty lies with the family. I'd never harm Mr. Sterling.

You: Mrs. Sterling mentioned tensions between Mr. Sterling and his son. Any insights on that?

Butler: Yes, they had disagreements, but nothing beyond that. I'd never allow harm to come to Mr. Sterling, and I certainly wouldn't cause it.

You: Thank you, Lewis. Your cooperation is appreciated. We'll keep investigating to find the truth.

Butler: Thank you, detective. I want to see justice served for Mr. Sterling."""
            print (text)
            witness()
        elif argument == 'd':
            #goodf()
            text= """
Interrogation with Mr. Secretary - David...
You: Good day, Mr. Secretary. Your correspondence with Mr. Sterling, particularly the inclusion in his will, has caught my attention. What was your relationship with Mr. Sterling?

Secretary: Ah, Detective, it's about the long-standing relationship with Mr. Sterling. He considered me part of his family.

You: Were there any business rivals Mr. Sterling faced, or any tensions he confided in you?

Secretary: The business world was never short of competitors, Detective. Although, he was meticulous about his public image and refrained from taking part in rivalries, his ex- business partner had hit a nerve, recently...

You: Your inclusion in his will raises eyebrows. Any personal motives or disputes that might connect to this?

Secretary: No, Detective. Mr. Sterling often spoke highly of me and it was only fair after all, that my family has served him with dedication, for years.

You: The timing of your request to be included in his will and his death, is rather suspicios.

secretary: I assure you, detective. I had no ill intent. I am simply struggling financially and needed some help.

You: I see. Your insights are valuable. Anything else you believe might aid the investigation?

Secretary: Nothing more, Detective. I just hope the truth is revealed soon...

You: Thank you, Mr. Secretary. We'll continue to delve into this matter further."""
            print (text)
            witness()
        elif argument == 'e':
            #goodf()
            text = """
Interrogation with Mr Sterling's ex- Business partner - Mr. Baker...
You: Good day, Mr. Partn. Your history with Mr. Sterling is of interest. Any lingering tensions between you two?

Baker: Ah, Detective. We had our share of disagreements, but it was nothing more than a... healthy competition in business.

You: Starting your own business, did it stem from any unresolved matters with Mr. Sterling?

Baker: No bad blood, between us, no. Detective, you know how it is in this 'Dog eat Dog' world. Starting my own business was already in my carrer plans...The timing is merely a coincidence!

You: Any motive for harm, personal or professional, regarding Mr. Sterling?

Baker: No. I won't say we were friends in his last moments...but I will not harm him.'

You: Understood. Your insights are valuable. Anything else you believe might aid the investigation?

Baker: Just hoping to be free from all this summons from court, to be honest. Just get your job done quickly...

You: Thank you for your insights. We will definietly find the truth."""
            result()
        else:
            print("Enter again...")
            witness()
    result1 = switch_case(suspect)
    print(result1)
def maid():
    global susList
    text = """ As Maid is already a suspect, you start your investigation from her...
Interrogation with the maid...
You: Good evening, Ms. Maid. I'm certain of your innocence in this matter. But, i cannot clear you of charges till I find the real culprit...

Ms. Maid: Thank you, sir. I appreciate your belief in me.

You: Can you tell me about Mr. Sterling's relations with his family and friends? Any tensions or conflicts you noticed?

Ms. Maid: Mr. Sterling adored his family, sir. He and his son, David, had their differences, but it was more about the business. As for friends, he didn't have many close ones. He was a private man.

You: Any enemies he might have made? Someone with a grudge?

Ms. Maid: I can't think of anyone, sir. Mr. Sterling was kind and fair. He had disagreements in business, but nothing extreme that I know of.

You: Thank you, Ms. Maid. Your insights are valuable. We'll find the truth soon. You have my assurance.

Ms. Maid: Thank you, Detective. I hope you find the real culprit soon.""" 
    print(text)
    print("Your current suspects are:")
    for e in susList:
        print(e)
    witness()
        
def entry_decision(location):
    print("...")
   
    if location == "a":
        print("The Butler of the house - Sebastian, greets you at the door!")
        print("Mr. Sterling's son Lewis is on the couch, going through some documents...")
        print("Upon investigation, you find a crack in the window!")
        print("The bbutler has given you the key to the Study Room")
        global key
        key=1
        #goodf()
    elif location == "b":
        print("Mrs. Sterling greets you warily in the bedroom. ")
        print("Upon Investigation, You find a hidden diary of Mr. Sterling's")
    elif location == "c":
        print("Maid Mary is the prime suspect")
        print("There are no signs of poison in the Kitchen...")
    elif location == "d":
        if(key==1):
            print("The victim was found dead in this room...")
            print("There is no sign of struggle")
            print("You now have access to Mr. Sterling's Computer!")
            print("You must decipher the hidden code in the computer.")
            #goodf()
            global clue
            clue=2
        else:
            print("You don't have the key to enter the study room...")
            #badf()


def initial_decision():
    print("Do you want to (a) Investigate the crime scene | (b) Decipher Clue | (c)Get DNA samples  | (d)Interview suspects and witnesses: ")
    choice1 = input("How do you want to proceed (a, b, c or d)? ")
#    print("You have chosen", choice1)
    n=1
    if choice1 == "a":
        #goodf()
        print("You have reached The Sterling's Mansion! Where do you want to start?")
        while n<=4:
            entry = input("a for Living Room | b for Mr. Sterling's Bedroom | c for Kitchen | d for Mr. Sterling's Study: ")
            entry_decision(entry)
            n=n+1
            if n==5:
                initial_decision()
    elif choice1 == "b":
        #goodf()
        print("As you go ahead with your investigation, you come across the following clues:")
        decipher_clues()
    elif choice1 == "c":
        print("You have sumbitted the dna samples to the forensic lab...")
        print("The tests are in process")
        print("You will recieve the tests later")
        initial_decision()
    elif choice1 == "d":
        print("During the initial investigation the Maid was arrested!")
        maid()
    else:
        print("Enter again...")
        initial_decision()

def startexe():            
    count=0
    while(count == 0):
        print("welcome Player!")
        print("Welcome to the Decision-Making Game!")
        gender = input("Enter your gender (M/F): ")

        if(gender == "M" or gender =="m"):
            print("Your name is Skerlock House, a famous detective! You have been been requested to solve the murder mystery of a famous businessman - Mr. Sterling")
            a=input("Press 1 if you want details regarding the case or press 2 to exit the game: ")
            if (a=="1"):
                text = """
        Your name is Skerlock House, a famous detective! You have been been requested to solve the murder mystery of a famous businessman - Mr. Sterling
        who is a wealthy and influential businessman known for his empire in finance. He is found dead in the mansion one early morning, by the butler. The initial report suggests a heart attack,
        but you suspect foul play. The maid of the house is arrested. 
                
        As Detective Skerlock House, you delve into the luxurious world of the Sterling estate, navigating through extravagant rooms,
        high-tech security systems, and a staff with their fair share of secrets. The victim's family is a mix of intriguing characters—the rebellious son, and the bitter wife, Suspicious Butler a mysterios secratary and a estranges business-Partner..."

        The mansion itself hides secret rooms and passages, each potentially holding a clue to Sterlin's demise.
        The challenge lies in decrypting the message, interrogating the suspects, 
        and navigating the intricate relationships within the Sterling family and business circles. Your choices will determine the course of the investigation, the revelation of dark secrets, and whether justice prevails in the gilded halls of the Sterling mansion
                
               
                """
                print(text)
                ready=input("Are you ready to take the decisions (Y/N?)")
                if (ready == "Y" or ready == "y"):
                    print("Let's go")
                    count=1
                    initial_decision()
                else:
                    quitv=input("Are you sure you want to quit the game (Y/N?)")
                    if (quitv == "Y" or quitv == "y"):
                        print("Bye!")
                        sys.exit()
                    else:
                        continue
            else:
                quitv=input("Are you sure you want to quit the game (Y/N?)")
                if (quitv == "Y" or quitv == "y"):
                    print("Bye!")
                    sys.exit()
      
        elif(gender == "F" or gender =="f"):
            print("Your name is Pancy draw, a famous detective! You have been been requested to solve the murder mystery of a famous businessman Mr. Sterling.")
            a=input("Press 1 if you want details regarding the case or press 2 to exit the game: ")
            if (a== "1"):
                text = """
        Your name is Pancy Draw, a famous detective! You have been been requested to solve the murder mystery of a famous businessman - Mr. Sterling
        who is a wealthy and influential businessman known for his empire in finance. He is found dead in the mansion one early morning, by the butler. The initial report suggests a heart attack, but you suspect foul play.
        The maid of the house was arrested. 
                
        As Detective Pancy Draw, you delve into the luxurious world of the Sterling estate, navigating through extravagant rooms, 
        high-tech security systems, and a staff with their fair share of secrets. The victim's family is a mix of intriguing characters—the rebellious son, and the bitter wife, Suspicious Butler a mysterios secratary and a estranges business-Partner..."

        The mansion itself hides secret rooms and passages, each potentially holding a clue to Sterlin's demise. 
        The challenge lies in decrypting the message, interrogating the suspects, 
        and navigating the intricate relationships within the Sterling family and business circles. Your choices will determine the course of the investigation, the revelation of dark secrets, and whether justice prevails in the gilded halls of the Sterling mansion
                
               
                """
                print(text)
                ready = input ("Are you ready to take the decisions(Y/N)?")
                if (ready == "Y" or ready == "y"):
                    print("Let's go")
                    count=1
                    initial_decision()
                else:
                    quitv=input("Are you sure you want to quit the game (Y/N?)")
                    if (quitv == "Y" or quitv == "y"):
                        print("Bye!")
                        sys.exit()
                    else:
                        continue

            else:
                quitv=input("Are you sure you want to quit the game (Y/N?)")
                if (quitv == "Y" or quitv == "y"):
                    print("Bye!")
                    sys.exit()

        else:
            print("Restart Game...")
            startexe()
startexe()
