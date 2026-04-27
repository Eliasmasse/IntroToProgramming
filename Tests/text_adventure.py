def start_adventure():
    print("you are in 5th grade and faced with a choice, what instrument will you play for band/orchestra?:")
    print("1. Clarinet")
    print("2. Trumpet")
    print("3. French horn")
    print("4. strings (orchestra by default)")

    choice = input("> ")

    if choice == "1":
        play_instrument("Clarinet")
    elif choice == "2":
        play_instrument("Trumpet")
    elif choice == "3":
        play_instrument("French horn")
    elif choice == "4":
        play_instrument("Strings")
        ensamble_choice("Orchestra")
    else:
        print("Invalid choice. Try again.")
        return



def clarinet_type(type):
    print(f"You choose to play the {type}.")

def strings_type(type):
    print(f"You choose to play the {type}.")

def play_instrument(instrument):
    print(f"You choose to play the {instrument}.")

    if instrument == "Clarinet":
        print("will you play Saprano clarinet or bass clarinet?:")
        print("1. Saprano")
        print("2. Bass")

        choice = input("> ")

        if choice == "1":
            clarinet_type("Saprano clarinet")
        elif choice == "2":
            clarinet_type("Bass clarinet")
        else:
            print("Invalid choice. Try again.")
            return
    elif instrument == "Strings":
        print("will you play violin, viola, cello, or bass?:")
        print("1. Violin")
        print("2. Viola")
        print("3. Cello")
        print("4. double bass")

        choice = input("> ")

        if choice == "1":
            print("You choose to play the Violin.")
            strings_type("violin")
        elif choice == "2":
            print("You choose to play the Viola.")
            strings_type("Viola")
        elif choice == "3":
            print("You choose to play the Cello.")
            strings_type("Cello")
        elif choice == "4":
            print("You choose to play the Bass.")
            strings_type("Bass")
        else:
            print("Invalid choice. Try again.")
            return

    if instrument == "Clarinet" or instrument == "Trumpet" or instrument == "French horn":
        print("will you join band or orchestra?:")
        print("1. Band")
        print("2. Orchestra")
        
        
        choice = input("> ")

        if choice == "1":
            ensamble_choice("Band")
        elif choice == "2":
            ensamble_choice("Orchestra")
        else:
            print("Invalid choice. Try again.")
            return

def practice(result):
    print(f"You're perfomance was {result}")

def ensamble_choice(ensamble):
    print(f"You choose to join the {ensamble}.")


    if ensamble == "Band":
        print("you are now in your junior year, your last song for your concert is Arabesque by Samuel N. Hazo, how many hours will you practice?")    
        print("1. none:")
        print("2. 30 min")
        print("3. 1 hour")
        print("4. 1.5 hours")

        choice = input("> ")

        if choice == "1":
            practice("poor")
        elif choice == "2":
            practice("ok")
        elif choice == "3":
            practice("good")
        elif choice == "4":
            practice("amazing")
        else:
            print("Invalid choice. Try again.")
            return
    elif ensamble == "Orchestra":
            print("you are now in your junior year, your last song is Danzon no. 2 by Arturo Marquez, how many hours will you practice?")
            print("1. none:")
            print("2. 30 min")
            print("3. 1 hour")
            print("4. 1.5 hours")

            choice = input("> ")

            if choice == "1":
                practice("poor")
            elif choice == "2":
                practice("ok")
            elif choice == "3":
                practice("good")
            elif choice == "4":
                practice("amazing")
            else:
                print("Invalid choice. Try again.")
                return   
def practice(result):
    print(f"You're perfomance was {result}")

    if result == "poor":
        print("due to lack of practice you were not able to play your part and decided not to pursue music anymore.")
    elif result == "ok":
        print("you played your part decently but decide that a music career is not for you.")
    elif result == "good":
        print("you played amazingly and decide to further pursue music in college.")
    elif result == "amazing":
        print("you played perfectly and made it into all state, you decide to further pursue music in college")

    if result == "amazing" or result == "good":
        print("you now have to decide if you want to be a music education major or a performance major:")
        print("1. Music education")
        print("2. Performance")

        choice = input("> ")

        if choice == "1":
            decision("Music education")
        elif choice == "2":
            decision("Performance")
        else:
            print("Invalid choice. Try again.")
            return
def decision(major):
    print(f"You choose to be a {major} major.")

    if major == "Music education":
        print("you now have to decide if you want to be a band director, orchestra director, or general music teacher:")
        print("1. Band director")
        print("2. Orchestra director")
        print("3. General music teacher")

        choice = input("> ")

        if choice == "1":
            print("you become a band director and have a successful career teaching high school students and local community bands.")
        elif choice == "2":
            print("you become an orchestra director and have a successful career teaching high school student and youth orchestras.")
        elif choice == "3":
            print("you become a general music teacher and have a successful career teaching elementary school students and direceting community events.")
        else:
            print("Invalid choice. Try again.")
            return
       
    elif major == "Performance":
        print("you now have to decide if you want to be a soloist, chamber musician, or orchestral musician:")
        print("1. Soloist")
        print("2. Chamber musician")
        print("3. Orchestral musician")

        choice = input("> ")

        if choice == "1":
            profession("Soloist")
        elif choice == "2":
            profession("Chamber musician")
        elif choice == "3":
            profession("Orchestral musician")
        else:
            print("Invalid choice. Try again.")
            return
def chamber(result):
    print(f"Your performance was {result}.")

    if result == "okay":
        print("your perfomance was okay but not good enough for other chamber groups to play with you, you decide to be a music teacher instead.")
    elif result == "good":
        print("you played good but rarely get picked up by other chamber groups, you double as a chamber musician and a music teacher.")
    elif result == "amazing":
        print("you played very well and were picked up by 10-15 chamber groups a year, you get a seccond part time job.")
    elif result == "perfect":
        print("you played perfectly and get multiple performances a month, you are considered a renowned chamber musician and will have a very successful career ahead of you.")

def orchestra(result):
    print(f"Your performance was {result}.")

    if result == "okay":
        print("your audition was a fail, you end up playing with community orchestras and teach music lessons.")
    elif result == "good":
        print("you get to in-person auditions but dont make it, you end up joining a less renowned orchestra.")
    elif result == "amazing":
        print("you got into the las vegas philharmonic, but you are on seccond part")
    elif result == "perfect":
        print("you played perfectly and get first chair, you get lots of money every year and will probably end up becoming a renowned orchestral musician.")
def solo(result):
    print(f"Your performance was a {result}.")

    if result == "25/40":
        print("your perfomance was okay but not good enough for other orchestras to play with you, you decide to be a music teacher instead.")
    elif result == "30/40":
        print("you played good but rarely get picked up by other orchestras, you double as a soloist and a music teacher.")
    elif result == "35/40":
        print("you played very well and were picked up by 10-15 orchestras a year, you get a seccond part time job.")
    elif result == "40/40":
        print("you played perfectly and get multiple performances a month, you are considered a renowned soloist and have a very successful career ahead of you.")

def profession(profession):
    print(f"you have decided to be a {profession}")
    


    if profession == "Soloist":
        print("you have to prepare for your first solo with the las vegas philharmonic, how many hours will you practice a day?")
        print("1. 1 hour")
        print("2. 2 hours")
        print("3. 3 hours")
        print("4. 4 hours")
    
        choice = input("> ")

        if choice == "1":
            solo("25/40")
        elif choice == "2":
            solo("30/40")
        elif choice == "3":
            solo("35/40")
        elif choice == "4":
            solo("40/40")
        else:
            print("Invalid choice. Try again.")
            return
    elif profession == "Chamber musician":
        print("you have to prepare for you first chamber music performance with your quintet, how many hours will you practice a day?")
        print("1. 1 hour")
        print("2. 2 hours")
        print("3. 3 hours")
        print("4. 4 hours")
    
        choice = input("> ")

        if choice == "1":
            chamber("okay")
        elif choice == "2":
            chamber("good")
        elif choice == "3":
            chamber("amazing")
        elif choice == "4":
            chamber("perfect")
        else:
            print("Invalid choice. Try again.")
            return
    elif profession == "Orchestral musician":
        print("you have to prepare for your first audition for the las vegas philharmonic, how many hours will you practice a day?")
        print("1. 1 hour")
        print("2. 2 hours")
        print("3. 3 hours")
        print("4. 4 hours")
    
        choice = input("> ")

        if choice == "1":
            orchestra("okay")
        elif choice == "2":
            orchestra("good")
        elif choice == "3":
            orchestra("amazing")
        elif choice == "4":
            orchestra("perfect")
        else:
            print("Invalid choice. Try again.")
            return
start_adventure()
print("you have finished your musical journey, thanks for playing!")




        
    

    
    

        

