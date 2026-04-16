print(r'''
***************************
    _ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(_(__)      _           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|//_      -----__   _  ___-----
_____''.--o/_  \_____()____
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     _|||__     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~
***************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossroad = input("You're at a crossroad. Where would you like to go?\n Type 'left' or 'right' ")

if crossroad == "left" or crossroad == "Left" or crossroad == "LEFT":
    swim = input("You're at a lake and there's an island in the middle.\n Would you like to swim or wait for a boat?\n Type 'swim' to swim or 'wait' to wait for a boat ")
    if swim == "wait" or swim == "wait" or swim == "WAIT":
        door = input("You arrive at the island unharmed.\n There are 3 doors.\n Which one would you like to go through - Red, Yellow or Blue? ")
        if door == "red" or door == "Red" or door == "RED":
            print("You were burned to death.\n GAME OVER")

        if door == "yellow" or door == "Yellow" or door == "YELLOW":
            print("You win!")

        if door == "blue" or door == "Blue" or door == "BLUE":
            print("You were eaten by beasts. \n GAME OVER")

    elif swim == "SWIM" or swim == "swim" or swim == "Swim":
        print("You were eaten by a trout.\n GAME OVER")


elif crossroad == "right" or crossroad == "Right" or crossroad == "RIGHT":
    print("You fell into a pothole and died. \n GAME OVER")