import os
import sys
import time
import json
import re
from design import Banner, Story, textColor
playerDetails = {}
userinfo = {}
characterInformation = {}
data = {}
scoreCard = {}
winng_trails = 0

"""
 Launch_game is main function of the game. which connects with game introduction , title design etc .
"""
def launch_game():
    entries = 0
    while entries < 3:
        entries = entries + 1
        print()
        print(textColor.purple + textColor.bold + "Welcome to ALONE AND UNAFRAID" + textColor.close)
        launch = input(textColor.purple + textColor.bold + "Please enter Start to begin game\n >" + textColor.close)
        if launch.upper() == 'START':
            entries = 0
            Banner.title()
            Story.intro()
            print(textColor.purple + textColor.bold + "Would like to proceed ?? (Y/N)" + textColor.close)
            w_proceed = input('>')
            if w_proceed.lower() == 'y' or w_proceed.lower() == 'yes':
                Banner.game_menu()
                option = input('> ')
                print()
                if option == 'l' or option.lower() == 'load':
                    pl_exists = check_player_existence('existing')
                    if pl_exists == True:
                        print()
                        existing_user = userinfo['name']
                        print(textColor.green + "Welcome } " + textColor.close)
                        loadgame(existing_user)
                elif option == 'new game' or option.lower() == 'n':
                    print(textColor.blue + textColor.bold + "NEW GAME" + textColor.close)

                    pl_exists = check_player_existence('new')
                    if pl_exists == True:
                        print(textColor.yellow + "Username alredy existed please enter diffent user name")
                        fetch_userinfo()
                    create_player()
                elif option == '4' or option.lower() == 'q':
                    sys.exit()
            elif w_proceed.lower() == 'n' or w_proceed.lower() == 'no':
                sys.exit()
            else:
                print(textColor.red + "Invalid entry. Please enter valid entry..!" + textColor.close)
                launch_game()
            print()
            break
        else:
            print(textColor.red + "Invalid entry. Please enter valid entry..!" + textColor.close)
    if entries == 3:
        print(textColor.red + "you have entered 3 wrong entries in a row")
        sys.exit()
"""
load-game()-- This function allows user to load the game 
after completion of certain levels.
"""
def loadgame(player_name):
    try:
        with open(player_name +'.txt') as loaded_file:
            user_data = loaded_file.read()
            characterInformation = json.loads(user_data)
            scoreCard = characterInformation['scoreCard']
            if not scoreCard:
                drill_level()
            elif characterInformation['level'] == 1:
                level_one()
            elif characterInformation['level'] == 2:
                level_two()
            elif characterInformation['level'] == 3:
                level_three()
    except FileNotFoundError:
        print()
"""
leave_game()-- This function allows users to 
save their game.
"""
def leave_game():
    characterInformation['user_data'] = userinfo
    characterInformation['scoreCard'] = scoreCard
    try:
        with open(userinfo['name'] + ".txt", "w") as file_object:
            file_object.write(json.dumps(characterInformation))
    except:
        print(textColor.red + "Unable to write to file" + textColor.close)
    print(textColor.green + textColor.bold +
          "------------------------SAVING GAME PROGRESS AND EXITING GAME-----------------------"
          + textColor.close)
    print()
    time.sleep(2)
    sys.exit()


"""
playerNameValidations()-- function perform validations to maintain 
username in a standard way.
manages length of the username between 4 to 15 and it should not 
allow special characters and no null values are allowed.
"""
reg_exp = re.compile('[^0-9a-zA-Z]+')
def playerNameValidation():
    entries = 0
    while entries < 3:
        entries += 1
        player_name = input(textColor.yellow + textColor.bold + 'Enter your character name:' + textColor.close)
        if len(player_name) == 0:
            print(textColor.yellow + 'Please enter valid name to proceed further!!' + textColor.close)
        elif len(player_name) < 3 or len(player_name) > 15:
            print(
                textColor.yellow + 'Length of user name should be between 3 and 15!Please enter a valid one!' + textColor.close)
        elif reg_exp.search(player_name):
            print(
                textColor.yellow + 'Username should not contain special characters!Please enter a valid one!' + textColor.close)
        else:
            entries == 0
            break
        print()

    if entries == 3:
        print(textColor.red + "you have entered 3 wrong entries in a row" + textColor.close)
        sys.exit()
    return player_name


"""
passwordValidations() function perform validations to maintain 
password in a standard way.
manages length of the password between 4 to 15 and it should not 
allow special characters and no null values are allowed.
"""


def validate_player_password():
    attempts = 0
    while attempts < 3:
        attempts += 1
        player_pwd = input(textColor.yellow + 'Enter your password:' + textColor.close)
        if len(player_pwd) == 0:
            print(textColor.yellow + 'Please enter valid password to proceed further!!' + textColor.close)
        elif len(player_pwd) < 6 or len(player_pwd) > 10:
            print(
                textColor.yellow + 'Length of password should be between 6 and 10!Please enter a valid one!' + textColor.close)
        elif reg_exp.search(player_pwd):
            print(
                textColor.yellow + 'Password should not contain special characters!Please enter a valid one!' + textColor.close)
        elif userinfo['name'].lower() == player_pwd.lower():
            print(
                textColor.yellow + " Password and character name are not allowed to be the same! Please enter a valid one" + textColor.close)
        else:
            attempts == 0
            break
    if attempts == 3:
        print(textColor.red + "you have entered 3 wrong entries in a row" + textColor.close)
        sys.exit()
    return player_pwd


# ----------------------------------------------------------------------------------------------------------------------

"""
Function to fetch user name and password
"""


def fetch_userinfo():
    player_name = playerNameValidation()
    userinfo['name'] = player_name
    player_pwd = validate_player_password()
    userinfo['password'] = player_pwd


# ----------------------------------------------------------------------------------------------------
"""
create_player()-- function allows users to create 
new player. later it takes user age as input and 
redirects to select_gender() function.
"""


def create_player():
    entries = 0
    while entries < 3:
        entries += 1
        confirm_pwd = input(textColor.yellow + textColor.bold + 'Confirm password:' + textColor.close)
        if userinfo['password'].lower() != confirm_pwd.lower():
            print(textColor.yellow + textColor.bold + 'Passwords does not match! Please try again!' + textColor.close)
        else:
            entries = 0
            break
    entries = 0
    while entries < 3:
        entries += 1
        player_age = input(textColor.yellow + textColor.bold + 'Enter your age:' + textColor.close)
        if len(player_age) == 0:
            print(textColor.yellow + textColor.bold + 'Please enter valid age!!' + textColor.close)
        try:
            player_age = int(player_age)
            if player_age < 13:
                print(
                    textColor.yellow + textColor.bold + 'You should be atleast 13 years old to play this game!!' + textColor.close)
            elif player_age >= 13:
                attempts = 0
                playerDetails = Storage(userinfo['name'], userinfo['password'])
                playerDetails.secure_uname_password()
                select_gender()
                break
        except ValueError:
            print('Please enter valid age!!')
    if attempts == 3:
        print(textColor.red + 'You have exceeded maximum limits!!Please try again later.' + textColor.close)
        sys.exit()


# -------------------------------------------------------------------------------------------------------------
"""
select_gender()-- This function allows user to enter their gender.
if the user make right entry , then it redirects to role_selection()
otherwise it exits the user from the game.
"""


def select_gender():
    gender_data = ['M', 'F', 'MALE', 'FEMALE']
    entries = 0
    print("select your gender")
    while entries < 3:
        entries = entries + 1
        print("Enter your gender: Type:(Male or Female)(M or F) ")
        gender = input('> ')
        if gender.upper() not in gender_data:
            print("Please enter a valid gender!! ")
        else:
            entries = 0
            userinfo['gender'] = gender
            role_selection()
            break
    if entries == 3:
        print(textColor.red + "you have entered 3 wrong entries in a row")
        sys.exit()


# -------------------------------------------------------------------------------------------------------------
"""
check_player_existence() function used to
Check whether the player details already existed or not 
"""
def check_player_existence(game_type):
    fetch_userinfo()
    player_found = False
    try:
        if os.path.isfile(os.getcwd() + '\log.txt') and not os.stat(os.getcwd() + '\log.txt').st_size == 0:
            with open('log.txt') as logfile:
                for i in logfile:
                    (player_name, player_pwd) = i.split(':')
                    if userinfo['player_name'].lower() == player_name.lower():
                        entries = 0
                        while entries < 3:
                            entries += 1
                            if userinfo['password'].lower() != player_pwd.rstrip().lower():
                                print('incorrect password ')
                                userinfo['password'] = input('Enter your password:')
                            else:
                                return True
                        if entries == 3:
                            print('You have exceeded maximum limits!!Please try again later.')
                            sys.exit()
                        break
                if player_found == False and game_type.lower() == 'existing':
                    print('User does not exist!! Do you want to create a new character? ')
                    dec = input('> ')
                    if dec.lower() == 'y' or dec.lower() == 'yes':
                        fetch_userinfo()
                        create_player()
                elif player_found == False and game_type.lower() == 'new':
                    return False
                else:
                    return True
    except FileNotFoundError:
        print('user deatails not found. Please try again!!')


# ----------------------------------------------------------------------------------
"""
Function to select role
"""


def role_selection():
    races = ['CAPTAIN', 'CHIEF', 'HELMSMAN', 'CADET']
    Banner.roles_menu()
    roles = input('> ')
    roles_list = Story.get_role_info(roles)
    if roles.upper() in races:
        print()
        userinfo['selected_role'] = roles.upper()
        print(f'Perfect! You have selected:{roles.upper()}')
        time.sleep(2)
        print()
        for r in roles_list:
            for key in r.keys():
                if roles.upper() == key:
                    print('')
                    print(roles.upper())
                    print()
                    print(r[key]['description'])
                    print()
                    print("""It's default STATISTICS is:""")
                    print()
                    print('STRENGTH: ', (r[key]['statistics']['Strength']))
                    print('Movements: ', (r[key]['statistics']['Movements']))
                    print('Intelligence: ', (r[key]['statistics']['Intelligence']))
                    print('Knowledge: ', (r[key]['statistics']['Knowledge']))
                    print('Accuracy: ', (r[key]['statistics']['Accuracy']))
        print()
        mode_selection()
    else:
        print("Please select any one of the role!")
        print()


# ----------------------------------------------------------------------------------
"""
Function defined to select class during account creation
"""


def mode_selection():
    mode_list = ['Normal', 'EASY', 'HARD']
    print(textColor.purple + textColor.bold + ' GAME MODE SELECTION ' + textColor.close)
    print()
    print(textColor.purple + "Please select your GAME MODE !" + textColor.close)
    print()
    print(textColor.purple + 'NORMAL' + textColor.close)
    print(textColor.purple + ' EASY ' + textColor.close)
    print(textColor.purple + ' HARD  ' + textColor.close)
    mode = input('> ')
    if mode.upper() in mode_list:
        print(textColor.purple + f'You have selected {mode.upper()}' + textColor.close)
    extra_feature_selection()


# ----------------------------------------------------------------------------------
"""
extra_feature_selection() -- allows users to choose extrafeature regardless of 
existing features.
"""


def extra_feature_selection():
    print()
    ext_feature = {'Sniping': 20, 'Bombing': 18, 'Hacking': 15}
    print('EXTRA FEATURE SELECTION ')
    print()
    print('Please select your STATISTICS!! ')
    print('1. SNIPING: 20')
    print('2. BOMBING: 18')
    print('3. HACKING: 15')
    extf = input('> ')
    print(' Thank you for choosing your extra feature')
    print()
    time.sleep(2)
    print('Congrats!!Your ACCOUNT has been created Successfully')
    carryon_or_exit()
    drill_level()


# ---------------------------------------------------------------------------------------------------------
"""
carryon_or_exit()-- This Function allows users to continue for 
further steps of the game or exit
"""


def carryon_or_exit():
    print('Are you interested in continuing the game? Type (c) to carry-on or (e) to exit ')
    decision = input('> ')
    if decision.lower() == 'e':
        leave_game()


# ------------------------------------------------------------------------------------------------------------------
"""
As per the game story player should complete the drill (training)
level before playing the actual levels.
So,this function contains game training session details.
"""


def drill_level():
    global winng_trails
    player_name = userinfo['name']
    print()
    print('CONDUCTING DRILL')
    print("""Malaysian Naval Base Located between the Kumara Hills.""")
    print("""The Moment there is no security on the top of the hill.SO,""")
    print("""Its a good time to make ralley point for helicoptor.""")
    print(f"""Ramanujan:Hello {player_name} , Im lieutenant Ramanujan , Tactical officer from southern indian navy.""")
    print("I was appointed by our chief of naval opertions to train you for the mission")
    print("Are you ready officer ??")
    print('please type READY to start training session')
    entries = 0
    while entries < 3:
        entries += 1
        drill_input = input('> ')
        if drill_input.lower() == 'ready':
            entries = 0
            print(f"That's perfect! {player_name}, I hear about punjab sailors having lot of courage")
            print("Hopefully you are gonna show that...!")
            break
        else:
            print('Please enter a valid command to continue playing! ')
    if entries == 3:
        leave_game()
    print("Press YES to continue")
    train_cmd = input('> ')
    if train_cmd.lower() == 'y' or train_cmd.lower() == 'yes':
        print()

        print(f'Alright {player_name}, Here I brought a weapons for you pick them.')
        print()
        print('PISTOL, KNIFE, MOLTOV, STUNGUN, DETONATOR, AK47')
        weapons = ['PISTOL, KNIFE, MOLTOV, STUNGRANADE, DETONATOR, AK47']
        print('Type PICK to take a weapon')
        action = input('> ')
        if action.lower() == 'pick':
            print()
            print(' picked weapons\n ')

            print(f'Ramanujan: {player_name}, you found two guards near the entrance.kill them sneakily')
            print("Hint::Killing with knife can escape you from the enemies noise detection alarm.")
            print('Type STAB to take it from the BAG and kill the enemy ')
            while True:
                stab_drill = input('> ')
                if stab_drill.lower() == 'stab':
                    print(f"HELL OF A JOB {player_name}.!")
                    break
                else:
                    winng_trails += 1
                    lost_game(winng_trails)

            while True:
                print()
                print(f"Ramanujan:Now {player_name}, lets practice throwing moltov cocktail on enemy")
                print("Please type THROW for throwing moltov cocktail")
                throw_drill = input('> ')
                if throw_drill.lower() == 'throw':
                    print(f"Ramanujan:Bravo..! , {player_name} you are better than I imagined")
                    break
                else:
                    winng_trails += 1
                    lost_game(winng_trails)

            while True:
                print(f"Ramanujan:Now Imagine {player_name}, what if you surrounded by bunch of enemies??")
                time.sleep(0.2)
                print(f'{player_name}', 'I believe Stun granade would be helpful')
                print(f"Ramanujan: Proceed {player_name}..!")
                print("Type STUNN for throwing stunn granade")

                stunn_drill = input('> ')
                if stunn_drill.lower() == 'stunn':
                    print(f"Ramanujan: Bloody Hell you made them Blind {player_name}")
                    break
                else:
                    winng_trails += 1
                    lost_game(winng_trails)

            while True:
                print()
                print(f"Ramanujan: Okay {player_name}, Now its time to break security system")
                print("Type HACK to break security systems")
                hack_drill = input('> ')
                if hack_drill.lower() == 'hack':
                    print(f"Well done {player_name} . You made it . it would be helpful once enter into the warship")
                    break
                else:
                    winng_trails += 1
                    lost_game(winng_trails)

            while True:
                print()
                print(" Type  SHOOT to use the PISTOL! ")
                pistol_drill = input('> ')
                if pistol_drill.lower() == 'shoot':
                    print(" You have given a perfect head blow")
                    break
                else:
                    winng_trails += 1
                    lost_game(winng_trails)

            while True:
                print()
                print(
                    f"Ramanujan:{player_name} There is a gunner on the watch tower, 800 yards from your position  need snipe him.")
                print("Type SNIPE to shoot the gunner")
                gun_cmd = input('> ')
                if gun_cmd.lower() == 'snipe':
                    print("You have hit the perfect target")
                    break
                else:
                    winng_trails += 1
                    lost_game(winng_trails)
            while True:
                print()
                print(
                    f'Ramanujan:{player_name} Climbing from sea level to top of the ship would be the last part of this drill ')
                time.sleep(1)
                print(f"Ramanujan:{player_name}, You need to pick RopeGun from the bag and shoot at ship railing")
                print("type SHOOT to use Rope Gun")
                ropegun_drill = input('> ')
                if ropegun_drill.lower() == 'shoot':
                    print("take deep breath before climbing")
                    print("type CLIMB to climb on top of the ship")
                    break
                else:
                    winng_trails += 1
                    lost_game(winng_trails)
            print()
            print(f"Raamanujan:Excellent {player_name}, you have finished simulation drill,")
            print()
            print(' You have successfully completed your training!! ')
            scoreCard['points'] = 100
            print("I belive we can finish our mission together")
            print(f"Chief of naval operations(CNO): Hello {player_name} ,Its time to Dive in")

            while True:
                print()
                print(" Type BOARD to board the helicopter.")
                board_helo = input('> ')
                if board_helo.lower() == 'board':
                    print(f"Pilot:Hello {player_name}, My name is OM im your pilot")
                    print(" It takes 2 hours to reach our ralley point ALPHA, have a tight sleep.")
                    print(f"{player_name}: Thank you OM.")
                    break
                else:
                    winng_trails += 1
                    lost_game(winng_trails)

            while True:
                print()
                print(f"OKAY {player_name} its time dive , take the radio with you.")
                print("Ramanujan will ping in our secret channel")
                time.sleep(0.5)
                print("Type JUMP to jump from the helicopter.")
                jump_drill = input('> ')
                if jump_drill.lower() == 'jump':
                    print('Move fast. We donot have sufficient time')
                    break
                else:
                    winng_trails += 1
                    lost_game(winng_trails)

            print()
            characterInformation['level'] = 1
            carryon_or_exit()
            level_one()
        else:
            print(' Invalid command! Please try again ')
            leave_game()
    carryon_or_exit()
    characterInformation['level'] = 1

    level_one()


# -------------------------------------------------------------------------------------

"""
level_one():-- This is a function that allows the player to navigate with instructions 
through the first level of the game.
"""


def level_one():
    name = userinfo['name']
    winng_trails = 0
    print()
    print('FIRST LEVEL')
    print('Now its time to find the Radio tower')
    while True:
        print(" Type LOOK for finding Radio communication tower")
        look_act1 = input('> ')
        if look_act1.upper() == 'LOOK':
            print('Found Radio Tower at north side of the Base')
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    winng_trails = 0
    while True:
        print(" Type RUN to move towards Radio tower")
        run_act1 = input('> ')
        if run_act1.upper() == 'RUN':
            print("Found a guard near the radio tower")
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    winng_trails = 0
    while True:
        print(" Type HIDE to camouflage in bush")
        hide_act1 = input('> ')
        if hide_act1.upper() == 'HIDE':
            print("wait until guard reaches to you")
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    winng_trails = 0
    while True:
        print(" Type FIGHT to beat the guard")
        fight_act1 = input('> ')
        if fight_act1.upper() == 'FIGHT':
            print("Guard knocked out")
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    winng_trails = 0
    while True:
        print(" Type SET to set Radio frequency to communicate ")
        fight_act1 = input('> ')
        if fight_act1.upper() == 'SET':
            print(f"Ramanujan:{name} Can you hear me?")
            print(f"{name}: Yes your voice loud and clear")
            print(f"Ramanujan:{name} Perfect mate Looking Forward to complete the mission")
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(f"{name}:I Found Guard is having the MapComputer ")
    print(f"Ramanujan :You can find a way to reach the ship, Forward IP address of it i can help you out.")
    winng_trails = 0
    while True:
        print(" Type SEND to send MapComputer Details ")
        send_act1 = input('> ')
        if send_act1.upper() == 'SEND':
            print(f"Ramanujan:{name} Now i can acces your MapComputer")
            print(f"Ramanujan:Our mission becomes much simpler now")
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(f"Ramanujan:{name}, just gothrough the ship manifest before reaching there")
    while True:
        print(" Type VIEW to See ship's manifest ")
        see_act1 = input('> ')
        if see_act1.upper() == 'VIEW':
            Banner.nuclear_ship_manifest()
            print(" Now  you have to get into the ship you what todo")
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
        while True:
            print()
            print(f"Ramanujan:{name}, You need to pick RopeGun from the bag and shoot at ship railing")
            print("type SHOOT to use Rope Gun")
            ropegun_drill = input('> ')
            if ropegun_drill.lower() == 'shoot':
                print("take deep breath before climbing")
                print("type CLIMB to climb on top of the ship")
                break
            else:
                winng_trails += 1
                lost_game(winng_trails)

    while True:
        print(f"Ramanujan:{name},there is a sea man on your right near the 5-inch gun point")
        print("Type FIGHT to with sea man")
        fight_seaman_act1 = input('> ')
        if fight_seaman_act1.upper() == 'FIGHT':
            print("You have entered into museum hall in ground floor!!")
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print()
    while True:
        print("Type TAKE to collect the key")
        weapon = input('> ')
        if weapon.upper() == 'TAKE':
            print("Keys collected")
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(f"{name},two sailors are coming towards you")
    while True:
        print("Type SHOOT to kill the sailors")
        shoot_act1 = input('> ')
        if shoot_act1.upper() == 'SHOOT':
            print("Sailors Died")
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    while True:
        print("Now its time to Disarm the security system")
        print("Type HACK to proceed")
        hack_act1 = input('> ')
        if hack_act1.upper() == 'HACK':
            print(f"Ramanujan:{name} now go to weapons room and lock it")
            print("")
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)

    print("")
    scoreCard['points'] += 100
    characterInformation['level'] = 2
    print(textColor.yellow + textColor.bold +
          "PRESS 'C or c ' to continue or PRESS 'Q or q to exit"
          + textColor.close)
    cq = input(textColor.yellow + '>' + textColor.close)
    # cq= continue or quit
    if cq.lower() == 'q':
        launch_game()
    elif cq.lower() == 'c':
        print(textColor.yellow + textColor.bold +
              "---------------------LEVEL-1 Completed moving to LEVEL-2----------------"
              + textColor.close)
        time.sleep(1.5)
        level_two()


"""
Players can navigate through the game with guidance on level-2 using this function.
"""


def level_two():
    winng_trails = 0
    time.sleep(1)
    name = userinfo['name']

    print(textColor.yellow + "" + textColor.close)
    print(textColor.yellow + f"Ramanujan:{name},Heat map shows remaining sailors are gone to mess deck for dinner\n"
                             f"There might be chance they gonna comeback enable the security system.\n"
                             f"I recommend you to close the mess deck hatch" + textColor.close)
    while True:
        print("Type CLOSE to shut the mess deck hatch")
        shoot_act1 = input('> ')
        if shoot_act1.upper() == 'CLOSE':
            print(textColor.green + "mess deck hatch is closed" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(textColor.yellow + f"Good job ,{name}" + textColor.close)
    print(
        textColor.yellow + f"{name},Apart from this mission it might be helpful if you steal the command control logs from\n"
                           f"their Combat information center (CIC)." + textColor.close)
    print(textColor.yellow + "Ramanujan: There are many benefits to learning war tactics from the enemy.\n"
                             "But Entering CIC is not an easy task be careful our heat might not work there." + textColor.close)
    while True:
        print("Type MOVE to move towards Combat information center")
        shoot_act1 = input('> ')
        if shoot_act1.upper() == 'MOVE':
            print(textColor.green + "you are in Combat Information Center" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(textColor.yellow + f"Ramanujan:{name},Please acknowledge your position." + textColor.close)
    print(textColor.yellow + f"{name}:Im in  ************** found ******* waiting for your ****..!" + textColor.close)
    time.sleep(0.3)
    print(textColor.yellow + f"{name}:Damm it ..!\n"
                             f"Radio is down i think there might be signal jammer here\n"
                             f"let's break it down" + textColor.close)
    while True:
        print("Type BREAK to smash signal jammer")
        shoot_act1 = input('> ')
        if shoot_act1.upper() == 'BREAK':
            print(textColor.green + "Signal Jammer Down!!" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(textColor.yellow + f"Ramanujan:{name},What Happend ??" + textColor.close)
    print(textColor.yellow + f"{name}:There is a signal jammer i smashed it" + textColor.close)
    print(textColor.yellow + f"Ramanujan:{name},great..!\n"
                             f"Gather all the classified documents and get move ASAP." + textColor.close)
    while True:
        print("Type PICK to collect documents")
        shoot_act1 = input('> ')
        if shoot_act1.upper() == 'PICK':
            print(textColor.green + "Docments Collected!!" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(textColor.yellow + f"Ramanujan:{name},Message from our OOD (Officer of the deck)\n"
                             f"ship you lying on heading towards our helicopter speed of 15 knots\n"
                             f"you have to stop the ship...!" + textColor.close)
    print(textColor.yellow + f"{name}:Wait lemme get into the Engine Room and Blow it out" + textColor.close)
    while True:
        print("Type MOVE to move towards Engine room")
        shoot_act1 = input('>')
        if shoot_act1.upper() == 'MOVE':
            print(textColor.green + "you are in Engine Room\n" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(textColor.yellow + f"Ramanujan:{name} search engine room plan document from stolen docs" + textColor.close)
    while True:
        print("Type FIND to search Engine room plan")
        shoot_act1 = input('>')
        if shoot_act1.upper() == 'FIND':
            print(textColor.green + "_________ENGINE ROOM PLAN_____________" + textColor.close)
            Banner.nuclear_engineroom_manifest()
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(textColor.yellow +
          f"Ramanujan:{name},If you cut down the supplies to propulsion unit Ship wont move anywhere and takes 30 mins"
          f"to fix it . Meantime, you can finish the mission" + textColor.close)
    while True:
        print("Type OK to cutdown supplies")
        shoot_act1 = input('>')
        if shoot_act1.upper() == 'OK':
            print(textColor.green + "Engine Stopped\n" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)

    scoreCard['points'] += 100
    characterInformation['level'] = 3
    print(textColor.yellow + textColor.bold +
          "PRESS 'C or c ' to continue or PRESS 'Q or q to exit"
          + textColor.close)
    cq = input(textColor.yellow + '>' + textColor.close)
    # cq= continue or quit
    if cq.lower() == 'q':
        launch_game()
    elif cq.lower() == 'c':
        print(textColor.yellow + textColor.bold +
              "---------------------LEVEL-2 Completed moving to LEVEL-3----------------"
              + textColor.close)
        time.sleep(1.5)

    level_three()


def level_three():
    winng_trails = 0
    name = userinfo['name']

    print(
        textColor.yellow + f"Ramanujan:{name}, no time for chat though we blocked everything if you dont kill the commander\n"
                           f"all the activities will be restarted\n try to find the commander and finish him." + textColor.close)
    print(
        textColor.yellow + f"Ramanujan:{name} ,i can help you if you come out side of the ship and update the map computer\n " + textColor.close)
    while True:
        print("Type OUT to reach the DECK")
        shoot_act1 = input('>')
        if shoot_act1.upper() == 'OUT':
            print(textColor.green + "Reached to DECK\n" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    while True:
        print("Type MAP to update the map computer ")
        shoot_act1 = input('>')
        if shoot_act1.upper() == 'MAP':
            print(textColor.green + "Update completed\n" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(
        textColor.yellow + f"Ramanujan:{name}, I have seen One GIANT person with cigar discussing with one sailor\n"
                           f"in missle pad.\n Get in there ASAP...! " + textColor.close)
    while True:
        print(textColor.yellow + "Type GETIN to reach Missle pad\n" + textColor.close)
        shoot_act1 = input('>')
        if shoot_act1.upper() == 'GETIN':
            print(textColor.green + "Reached missile launch pad\n" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    while True:
        print(textColor.yellow + "Type FIGHT to fight with commander\n" + textColor.close)
        shoot_act1 = input('>')
        if shoot_act1.upper() == 'FIGHT':
            print(textColor.green + "Commander unconscious\n" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(textColor.red + "Commander companion is escaping from there\n")
    while True:
        print(textColor.yellow + "Type CATCH to chase the companion" + textColor.close)
        shoot_act1 = input('>')
        if shoot_act1.upper() == 'CATCH':
            print(textColor.green + textColor.bold + "Chasing sailor\n" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(textColor.yellow + textColor.bold + "kill both of them with knife")
    while True:
        print(textColor.yellow + "Type KILL to cut the throat of commander and his companion " + textColor.close)
        shoot_act1 = input('>')
        if shoot_act1.upper() == 'KILL':
            print(textColor.green + textColor.bold + "Commander and Enemy sailor are dead\n" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(textColor.yellow+f"Ramanujan:{name},you made it our country will proud of you.!\n ")
    time.sleep(0.5)
    print(textColor.yellow + f"Ramanujan:{name},get the life jacket and evacuate from the ship immediately\n ")
    while True:
        print(textColor.yellow + "Type ESC to Evacuate from ship" + textColor.close)
        shoot_act1 = input('>')
        if shoot_act1.upper() == 'ESC':
            print(textColor.green + textColor.bold + "Jumped into Sea water" + textColor.close)
            break
        else:
            winng_trails += 1
            lost_game(winng_trails)
    print(textColor.green+textColor.bold+"----------MISSION COMPLETED------------")
    scoreCard['points'] += 100
    print(" Type SCORE to see the score ")
    score = input('> ')
    if score.upper() == 'SCORE':
        playerScoreboard()
        sys.exit()


"""
lost_game() - shows player game loosing information. 
"""
def lost_game(winng_trails):
    print('Please try again!!')
    if winng_trails > 3:
        print()
        userinfo['status'] = 'GAME_LOST'
        leave_game()


def playerScoreboard():
    for key, value in scoreCard.items():
        print(key.upper(), ":", value)


"""
 Class Storage used to save the user name and password of all players
"""
class Storage:
    def __init__(self, uname, password):
        self.user_name = uname
        self.user_password = password

    def secure_uname_password(self):
        try:
            with open("log.txt", "a") as log:
                log.write(self.user_name + ':')
                log.write(self.user_password)
                log.write('\n')
        except:
            print("Sorry unable to write the file")


"""
 launch_game fucntion to start the game
"""
launch_game()
