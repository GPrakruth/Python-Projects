# Py's Haunted House
print("Welcome to Py/n's Haunted House!")
greet = input("Are you ready to play? \n enter yes or no ")
if greet.lower() == "yes":
  print("""Great! let's get playing! 
  There's a house with a small lawn in front of you. 
  You knock to ask if they want to buy that your coding club 
  is selling for ergonomic keyboards. 
  The door is open and you hear a cry.""")
  enter = input("What do you do, go in or leave? ")
  if enter.lower() == "go in":
    print("""You walk across the threshold and feel a chill run down your spine. 
    You're standing in an entrance way
    infront of a living room and hallway that has four doors in front of you.""")
    door = input("There's a door with a poster and one with a wreath near you. Do you go into either door, yes or no? ") 
    if door.lower() == "yes":
      which1 = input("Do you grab the poster door, yes or no? ")
      if which1.lower() == "yes":
        print("""You enter the room and there's an empty rocking chair 
        with a creepy doll. You step closer to get a better look.""")
        doll = input("Do you touch the doll, yes or no? ")
        if doll.lower() == "yes":
          print("""The doll bites you and you scream! You run out
          of the house and leave. Swearing to never ever buy
          another ergonomic keyboard ever again.""")
        else:
          print("""The doll laughs. You run out of the house screaming
          and leave.""")
      else:
        print("""You open the door with the wreath and gently tread into the room.
        There's a low moaning coming from the closet.""")
        closet = input("Do you open the closet, yes or no? ")
        if closet.lower() == "yes":
          print("""A crow flies into your face and chases you out of the house, 
          pecking your face and arms. You quickly get into your car and leave.""")
        else:
          print("""The moaning gets louder and then there's a banging. You look for your phone
          and realize its not there. You look back up and there's a pair of eyes watching you,
          hiding behind the chair next to the closet.
          You jump and run out of the house, leaving.""")
    else:
      print("""You continue down the hall to two other doors. The doors both pop open 
      and at each door there is a dog. They chase you out of the house
      biting at your heels. You get into your car and leave.""")
  else:
    print("So you're walking back to your car when you hear another cry. You reach for your cell phone. ")
    phone = input("Do you leave without you cell? Yes or no? ")
    if phone.lower() == "yes":
      print("""You jump in the car and try to start the car. But then a cat jumps on the hood and hisses at you. 
      you start the car, but the cat doesn't move.""")
      cat = input("Do you leave or get out?")
    else:
      print("""You return to the porch to look for the phone. 
      As you walk across the porch a light bulb explodes and you scream.""")
      porch = input("Do you return to the car without your phone, yes or no? ")
      if porch.lower() == "yes":
        print("You get into your car and return your coding club without any desire for ergonomic keyboards.")
      else:
        print("""You continue looking for your phone 
        when a potted plant unexpectedly falls just behind you. 
        You see your phone under it.""")
        plant = input("Do you grab the phone? ")
        if plant.lower() == "yes":
          print("""You grab the phone and return to the car. 
          You leave and decide ergonomic keyboards are lousy.""")
        else:
          print("""You grab the phone and return to the car. 
          You leave and decide ergonomic keyboards are lousy.""")
else:
  print("That's too bad. Maybe another time.")