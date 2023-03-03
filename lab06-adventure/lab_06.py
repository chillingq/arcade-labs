import arcade


class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west



def main():
    next_room = 0
    current_room = 0
    done = False
    room_list = []
    room = Room("You are at the center hall of a house, it feels lonely and empty. There are halls in the four \n"
                
                "cardinal "
                "directions.", 1, 2, 3, 4)
    room_list.append(room)
    room = Room("You are at the entrance hall, feels cold here and you can hear cars passing by from time to time.\n"
                "There is a big door in the north, a smaller "
                "white door in the west and \n"
                "another small door in the east that feels warm, there is a large hallway to the south.", 5, 6, 0, 10)
    room_list.append(room)
    room = Room("You are at the east hallway, feels warm in between the walls. There is a door looking north\n"
                "with piano sounds coming from it, a "
                "similar door in the south with a name on it and a dark big room to the west.",
                6, None, 7, 0)
    room_list.append(room)
    room = Room("You are at the south hallway, feels cold, you can hear an owl making sounds. You can see a big\n"
                "hall going north and a double glass door in the south, you can´t see through the glass due to the\n"
                "darkness. You see another two doors, a latch door in the east and a frame without door in the west.",
                0, 7, 8, 9)
    room_list.append(room)
    room = Room("You are at the west hallway, there is cold atmosphere here. You see a white door with latch in\n"
                "the north, a big empty hall to the east and a flat door in the south.", 10, 0, 9, None)
    room_list.append(room)
    room = Room("You are at the front porch, its freezing here (you aren´t wearing any jacket and you are in the\n"
                "middle of the night in autumn). You see a big door to the south with a doorbell next to it, there "
                "aren´t much more\n"
                "ways to go if you want to stay alive and warm.", None, None, 1, None)
    room_list.append(room)
    room = Room("You are at the living room, there is a fireplace on the wall and a person you know playing the piano."
                "\n"
                "You see a door in the south which feels warmer than the door in the west of the living room."
                , None,
                None, 2, 1)
    room_list.append(room)
    room = Room("You are at the bedroom, you feel comfortable and safe in here.\n"
                "You see a door in the north with nothing special on it and a door in the west with some food on the "
                "floor."
                , 2, None,
                None, 3)
    room_list.append(room)
    room = Room("You are at the balcony, you start to feel a bit hypothermic. Your only safe exit\nis going through"
                " the"
                " glass door in the north.", 3, None, None, None)
    room_list.append(room)
    room = Room("You are at the kitchen, you start to feel hungry. You see a frameless flat door in the north and\n"
                "a frame without door in the east."
                , 4, 3, None, None)
    room_list.append(room)
    room = Room("You are at the bathroom, you could wash your teeth or something here. You see a white door\n"
                "with latch in the "
                "east which feels ice cold and a normal door with latch in the south."
                , None, 1, 4, None)
    room_list.append(room)

    while done == False:
        print()
        print(room_list[current_room].description)
        print("Direction chosen: ")
        response = input(str())
        response.lower()
        if response == "north":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You can´t go that way")
            else:
                current_room = next_room
        elif response == "east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("You can´t go that way")
            else:
                current_room = next_room
        elif response == "south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You can´t go that way")
            else:
                current_room = next_room
        elif response == "west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You can´t go that way")
            else:
                current_room = next_room
        else:
            print("Can´t understand that")



main()
