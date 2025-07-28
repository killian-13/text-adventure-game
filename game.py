from random import randint
def game_over():
  print("GAME OVER")
  return
def you_win():
  print("YOU WIN")
  return
def action_menu(action_1, action_2, action_3):
  print("ACTION MENU:")
  print(f"1. {action_1}")
  print(f"2. {action_2}")
  print(f"3. {action_3}")

def location_1(has_key=False):
  print("You were eaten by zombies")
  game_over()
  return

def location_2(has_key):
  print("You are in a room with rotted planks and a bed with a moth eaten blanket.")
  print("")
  action_menu("go north", "go east", "look around")
  print("")

  while True:
    action = input("ENTER: ")
    if action == ("look around"):
      print("")
      print("You are clearly in a young child's room, as evidenced by the stuffies and bright colors, now faded.")
      print("You notice a shine as a light catches in between the stuffed animals. ")
      print("")
      print("ACTION MENU: ")
      print("1. look closer")
      print("")

      action = input("ENTER: ")

      if action == ("look closer"):
        chance = randint(1, 3)
        print("")
        print("You look closer")
        if chance == 1:
          print("You find a key")
          print("")
          action_menu("go north", "go east", " ")
          print("")
          has_key = True
          action = input("ENTER: ")
          if action == ("go north"):
            location_3(has_key)
            break
          elif action == ("go east"):
            location_1(has_key)
            break
          else:
            print("Invalid action")

        else:
          print("It was a trick of the light. There is nothing there.")
          print("")
          action_menu("go north", "go east", " ")
          print("")
          action = input("ENTER: ")
          if action == ("go north"):
            location_3(has_key)
            break
          elif action == ("go east"):
            location_1(has_key)
            break
          else:
            print("Invalid action")

    elif action == ("go north"):
      location_3(has_key)
      break

    elif action == ("go east"):
      location_1(has_key)
      break

    else:
      print("Invalid action")
      print("")

def location_3(has_key, has_sword=False):
  print("")
  print("As your eyes adjust to the dark, you see a massive shape looming over you. Could it be the door?")
  print("Uh-oh. Look out ahead. Something seems to be moving towards you.")
  print("")
  print("ACTION MENU: ")
  print("look around")
  print("")
  action = input("ENTER: ")
  print("You're in luck! A sword was left behind from a previous traveler.")
  print("")
  print("ACTION MENU: ")
  print("pick it up")
  print("prepare to die")
  print("")
  action = input("ENTER: ")
  if action == ("prepare to die"):
    print("You faced the fly with 100% courage and 0% skill. Congrats!")
    game_over()
  elif action == ("pick it up"):
    print("Nice skills! You just cut a fly perfectly in half under the cover of darkness. Where did you even learn how to do that?")
    print("")
    print("ACTION MENU: ")
    print("go east")
    print("go south")
    print("")
    has_sword = True
    action = input("ENTER: ")
    if action == ("go east"):
      location_4(has_key, has_sword)
    elif action == ("go south"):
      location_2(has_key)
  else:
    print("Invalid action")
    game_over()

from random import randint

def location_4(has_key, has_sword):
  print("You find a huge computer blocking your way!")
  print("On the screen, it says 'ENTER PASSWORD' ")
  action_menu("go west", "go south", "guess password")
  print("")

  action = input("ENTER: ")
  if action == ("guess password"):
    secret_number = randint(1, 100)
    print("Guess a number between 1 and 100")
    print("")

    for guess_count in range(1,11):

      guess = int(input(f"Guess {guess_count}: "))

      if guess == secret_number:
          print(f"Congratulations!")
          if has_key:
              you_win()
              return
          else:
              print("But you still need the key to unlock the final door! Go to the bedroom to search for it.")
              print("")
              action_menu("go west", "", "go south")
              print("")
              action = input("ENTER: ")
              if action == ("go west"):
                location_3(has_key)
              elif action == ("go south"):
                location_1()
              else:
                print("Invalid action")
                print("")

      elif guess < secret_number:
          print("Too low!")
          print("")
      elif guess > secret_number:
          print("Too high!")
          print("")
      else:
          print("Invalid input. Please enter a number.")
    else:
        print(f"Sorry, you've run out of guesses.")
        game_over()
        return
  elif action == ("go west"):
    location_3(has_key, has_sword)
  elif action == ("go south"):
    location_1()

  else:
    print("Invalid action")
    print("")

print("WELCOME TRAVELER")
print("You are trapped in a room with 3 doors. You must choose one to enter.")
print("You are facing north.")
print("One door is located behind you and holds an army of zombies.")
print("One room lies to your left and the other is in front of you.")
print("Pick wisely, as the wrong door could lead to danger.")
print("Your goal is to find a key that will allow you to unlock the final door.")
print("Move quickly to avoid getting eaten by the zombies, as it will result in game over.")
print("Good luck")
input("Press enter to continue")

action_menu("go north", "", "go west")

has_key = False

while True:
  action = input("ENTER: ")

  if action == ("go west"):
    location_2(has_key)
    break
  elif action == ("go north"):
    location_4(has_key, False)
    break
  else:
    print("Invalid action")
