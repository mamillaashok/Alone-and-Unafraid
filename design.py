class textColor:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    close = '\033[0m'
    bold = '\033[1m'


class Banner:
    @staticmethod
    def title():
        print(textColor.purple + textColor.bold + "Welcome to ALONE AND UNAFRAID" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                                                                                                      +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+      *       *          ***    *    *  ********                                                                      +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+    *   *     *        *     *  **   *  *                                                                             +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+   *******    *        *     *  * *  *  ********                                                                      +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+  *       *   ******     ***    *   **  ********                                                                      +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                                                                                                      +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                          *     *   *  *****                                                          +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                        *   *   **  *  *     *                                                        +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                       *******  * * *  *     *                                                        +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                      *       * *  **  *****                                                          +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                                                                                                      +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                                       *    *  *   *     *     **** *****    *   ***** *****          +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                                       *    *  **  *   *   *   *    *****  *  *    *   *     *        +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                                       *    *  * * *  *******  **** **    ******   *   *     *        +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+                                                        ***    *  **  *     *  *    *  *  *    * ***** * ***          +" + textColor.close)
        print(
            textColor.purple + textColor.bold + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++" + textColor.close)

    @staticmethod
    def game_menu():
        print(textColor.green + textColor.bold + ".-----------------------------------------." + textColor.close)
        print(textColor.green + textColor.bold + "|------------GAME MENU--------------------|" + textColor.close)
        print(textColor.green + textColor.bold + "|          (L)-LOAD-GAME                  |" + textColor.close)
        print(textColor.green + textColor.bold + "|          (N)-NEW-GAME                   |" + textColor.close)
        print(textColor.green + textColor.bold + "|          (E)-Exit-GAME                  |" + textColor.close)
        print(textColor.green + textColor.bold + ".-----------------------------------------." + textColor.close)

    @staticmethod
    def roles_menu():
        print()
        print(textColor.green  + textColor.bold   +"  _________________________" + textColor.close)
        print(textColor.green  + textColor.bold   +"|Please select your ROLE!!|" + textColor.close)
        print(textColor.green  + textColor.bold   +"| ________________________|" + textColor.close)
        print(textColor.yellow + textColor.bold   +"|         CAPTAIN         |" + textColor.close)
        print(textColor.yellow + textColor.bold   +"|         CHIEF           |" + textColor.close)
        print(textColor.yellow + textColor.bold   +"|         HELMSMAN        |" + textColor.close)
        print(textColor.yellow + textColor.bold   +"|         CADET           |" + textColor.close)
        print(textColor.green  + textColor.bold   +"|_________________________|" + textColor.close)
        print()
    @staticmethod
    def nuclear_ship_manifest():

        print(textColor.bold + textColor.blue + " " + textColor.close)
        print(textColor.bold + textColor.blue + " " + textColor.close)
        print(textColor.bold + textColor.blue + "                                                                                           " + textColor.close)
        print(textColor.bold + textColor.blue + "                                        ____________ _______________                                                        " + textColor.close)
        print(textColor.bold + textColor.blue + "                                       |     6      |               |                   " + textColor.close)
        print(textColor.bold + textColor.blue + "                              ._||_.   |____________|      2        |                                 " + textColor.close)
        print(textColor.bold + textColor.blue + "                   __________ |    |   |            |               |                                " + textColor.close)
        print(textColor.bold + textColor.blue + "                        ______|___ |___|     3      |_______________|                                " + textColor.close)
        print(textColor.bold + textColor.blue + "                        |       5      |            |      1        |                                " + textColor.close)
        print(textColor.bold + textColor.blue + "   \____________________|_____________ |____________|_______________|_________________/        .______________________.             " + textColor.close)
        print(textColor.bold + textColor.blue + "    \                                                                                /         |___ SHIP_PLAN_________|           " + textColor.close)
        print(textColor.bold + textColor.blue + "     \                                                                              /          |  1.MESS DECK         | " + textColor.close)
        print(textColor.bold + textColor.blue + "       \                                ___________                                /           |  2.CIC               | " + textColor.close)
        print(textColor.bold + textColor.blue + "        \                              |           |                              /            |  3.Weapons Room      | " + textColor.close)
        print(textColor.bold + textColor.blue + "         \                             |      4    |                             /             |  4.Engine  Room      |          | " + textColor.close)
        print(textColor.bold + textColor.blue + "          \                            |           |                            /              |  5.MISSILE pad       | " + textColor.close)
        print(textColor.bold + textColor.blue + "           \___________________________|___________|___________________________/               |______________________| " + textColor.close)

    @staticmethod
    def nuclear_engineroom_manifest():
        f = open("engineroom.txt", "r")
        print(f.read())





class Story:
    @staticmethod
    def intro():
        print(textColor.bold + textColor.blue + "Story:Crude oil revenues are very lucrative in the Indian economy.\n "
                                                "The Government of India has recently set up some oil rigs in various parts of the Bay of Bengal.\n "
                                                "The enemy country sent a nuclear warship to destroy them." + textColor.close)
        print(textColor.blue + textColor.bold + "The Indian Raw team recognized that the enemy ship dropped its anchor"
                                                " at the Malaysian Naval Base Camp for food supplies." + textColor.close)

        print(
            textColor.blue + textColor.bold + "The Indian Navy planned a secret operation to protect the oil rigs. \nCurrently, in this game the character must enter the ship and fight alone with them, "
                                              "kill the leader of the enemy and capture the important documents on the ship, and escape. " + textColor.close)
        print(textColor.blue + textColor.bold + "" + textColor.close)

    def get_role_info(r):
        role_info = [{
            'CAPTAIN': {'description':"""
                                The captain, also known as the master, shipmaster or ship captain, 
                                is the commander of the ship and its highest-ranking individual. 
                                The captain may not own the ship,but it's 'his' ship while he's aboard.
                                It's the captain's job to direct the ship and manage all of its operations.
                                On a sailboat, the captain is responsible for complying with regulations and navigating, 
                                along with steering and trimming the sails if the crew is small. 
                           """,
                        'statistics': {
                            'Strength': 7,
                            'Movements': 9,
                            'Intelligence': 9,
                            'Knowledge': 9,
                            'Accuracy': 7}
                        }

        },
            {
                'CHIEF': {'description': """ 
                                                    chief officer, is second in command below the captain. 
                                                    The first mate is often charged with commanding the vessel when 
                                                    the captain is sleeping, 
                                                    ill, or otherwise absent.
                                                    """,
                          'statistics': {'Strength': 8,
                                         'Movements': 7,
                                         'Intelligence': 6,
                                         'Knowledge': 7,
                                         'Accuracy': 9}
                          }
            },
            {
                'HELMSMAN': {'description': """ 
                                                    the helmsman is responsible for steering and keeping the vessel on 
                                                    course. The helmsman takes direct orders from the captain usually in the
                                                     form of (direction) then (compass degrees).Keeping the vessel on course
                                                     is actually quite challenging, as boats never track completely straight 
                                                     courses.The helmsman must be delicate and skilled, as they're often tasked
                                                      with making constant and minute side-to-side course corrections.

                                                   """,
                             'statistics': {'Strength': 8,
                                            'Movements': 7,
                                            'Intelligence': 6,
                                            'Knowledge': 7,
                                            'Accuracy': 9}
                             }
            },
            {
                'CADET': {'description': """A cadet is a trainee or inexperienced sailor who comes aboard and 
                                             participates (usually in a limited capacity) in shipboard duties. 
                                             Cadets are the lowest-ranking sailors aboard a ship.
                                         """,
                          'statistics': {
                              'Strength': 7,
                              'Movements': 5,
                              'Intelligence': 4,
                              'Knowledge': 3,
                              'Accuracy': 6
                          }
                          }
            },

        ]
        return role_info

