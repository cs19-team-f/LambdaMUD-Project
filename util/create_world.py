
# creates all the rooms in the adventure world


from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(
    title="Outside Cave Entrance",
    description="North of you, the mansion looms forebodingly.",
    x_coord=50,
    y_coord=50
)

r_foyer = Room(
    title="Foyer", description="""Dim light filters in from the south. Dusty passages run north and east and west.""",
    x_coord=50,
    y_coord=51
)

r_overlook = Room(
    title="Grand Overlook",
    description="A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.",
    x_coord=48,
    y_coord=53
)

r_greatroom = Room(
    title="Great Room",
    description="A cavernous room, the ceiling disappears in darkness. The cold floor tiles are covered with huge, darkly colored area rugs. Portraits of glaring ancestors hang on the walls, seemingly watching your every move.",
    x_coord=52,
    y_coord=52
)

r_library = Room(
    title="Library",
    description="Full of dark wood and looming stuffed animal heads, it smells of ominous deeds and stale smoke. Light filters in from the french doors to the patio beyond.",
    x_coord=49,
    y_coord=52
)

r_hallway = Room(
    title="Hallway",
    description="A wide hallway lined with banners and heraldry. Is that garlic?",
    x_coord=49,
    y_coord=51
)

r_terrace = Room(
    title="Terrace",
    description="A wide stone terrace littered with overturned chairs, empty planter boxes, and dead birds. A few stone steps lead down to the Overlook.",
    x_coord=48,
    y_coord=52
)

r_narrow = Room(
    title="Narrow Passage",
    description="The narrow passage bends here from west to north. The smell of gold permeates the air.",
    x_coord=51,
    y_coord=51
)

r_treasure = Room(
    title="Treasure Chamber",
    description="You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.",
    x_coord=51,
    y_coord=52
)

r_basement = Room(
    title="Dark Basement",
    description="You're going to need a torch in here. Crates and boxes stacked everywhere. In the dust on the floor, some faint footprints lead off around the corner of some shelves.",
    x_coord=49,
    y_coord=50
)

r_secret = Room(
    title="Secret Passage",
    description="Very narrow but high-ceilinged passage that twists and turns. An acrid smell gets stronger as you walk.",
    x_coord=48,
    y_coord=50
)

r_laboratory = Room(
    title="Laboratory",
    description="Foul odors rise from buckets on the floor. Some of this large equipment must have been assembled pice by piece in here. What is that on the walls? ",
    x_coord=48,
    y_coord=49
)

rooms = [
    r_outside,
    r_foyer,
    r_narrow,
    r_treasure,
    r_overlook,
    r_greatroom,
    r_library,
    r_hallway,
    r_terrace,
    r_basement,
    r_secret,
    r_laboratory
]

for r in rooms:
    r.save()


room_map = {
    'Outside': [[50, 50], {'n': 'Foyer'}],
    'Foyer': [[50, 52], {'n': 'Great Room', 's': 'Outside', 'e': 'Narrow Passage', 'w': 'Hallway'}],
    'Great Room': [[50, 54], {'s': 'Foyer', 'w': 'Library'}],
    'Narrow Passage': [[53, 52], {'n': 'Treasure Room', 'w': 'Foyer'}],
    'Treasure Room': [[53, 54], {'s', 'Narrow Passage'}],
    'Hallway': [[47, 52], {'n': 'Library', 's': 'Dark basement', 'e': 'Foyer'}],
    'Library': [[47, 54], {'s': 'Hallway', 'e': 'Great Room', 'w': 'Overlook'}],
    'Terrace': [[44, 54], {'n': 'Overlook', 'e': 'Library'}],
    'Overlook': [[44, 56], {'s': 'Overlook'}],
    'Dark basement': [[47, 50], {'n': 'Hallway', 'w': 'Secret Passage'}],
    'Secret Passage': [[44, 50], {'s': 'Laboratory', 'e': 'Dark basement'}],
    'Laboratory': [[44, 48], {'n': 'Secret Passage'}],
}

f = open("map.html", "w")

divs = ""
for roomID in room_map:
    coordinates = room_map[roomID][0]
    exits = room_map[roomID][1]
    coordinates = [coordinates[0] - 30, 30 - (coordinates[1] - 30)]
    style = "position: absolute; display: block; width: 63px; height: 30px;"
    style += "background-color: gray;font-size: 12px;color: black;text-align: center;"
    style += f"left: {coordinates[0] * 31 - 2}px; top:{coordinates[1] * 32}px;"
    div = f"<div style=\"{style}\" id=\"{roomID}\">{roomID}</div>"
    divs += div
    for exit in exits:
        exitStyles = "position: absolute; display: block; width: 12px; height: 12px;"
        exitStyles += "background-color: black;"

        if exit == "n":
            exitStyles += f"left: {coordinates[0] * 32 + 5}px; top:{coordinates[1] * 32 - 20}px;"
        elif exit == "s":
            exitStyles += f"left: {coordinates[0] * 32 + 5}px; top:{coordinates[1] * 32 + 34}px;"
        if exit == "e":
            exitStyles += f"left: {coordinates[0] * 32 + 49}px; top:{coordinates[1] * 32 + 7}px;"
        if exit == "w":
            exitStyles += f"left: {coordinates[0] * 32 - 39}px; top:{coordinates[1] * 32 + 7}px;"

        div = f"<div style=\"{exitStyles}\"></div>"
        divs += div


f.write(divs)


# Link rooms together
r_outside.connectRooms(r_foyer, "n")

r_foyer.connectRooms(r_greatroom, "n")
r_foyer.connectRooms(r_outside, "s")
r_foyer.connectRooms(r_narrow, "e")
r_foyer.connectRooms(r_hallway, "w")

r_greatroom.connectRooms(r_foyer, "s")
r_greatroom.connectRooms(r_library, "w")

r_library.connectRooms(r_hallway, "s")
r_library.connectRooms(r_greatroom, "e")
r_library.connectRooms(r_terrace, "w")

r_hallway.connectRooms(r_library, "n")
r_hallway.connectRooms(r_basement, "s")
r_hallway.connectRooms(r_foyer, "e")

r_terrace.connectRooms(r_library, "e")
r_terrace.connectRooms(r_overlook, "n")

r_overlook.connectRooms(r_terrace, "s")

r_narrow.connectRooms(r_treasure, "n")
r_narrow.connectRooms(r_foyer, "w")

r_treasure.connectRooms(r_narrow, "s")

r_basement.connectRooms(r_hallway, "n")
r_basement.connectRooms(r_secret, "w")

r_secret.connectRooms(r_laboratory, "s")
r_secret.connectRooms(r_basement, "e")

r_laboratory.connectRooms(r_secret, "n")

players = Player.objects.all()
for p in players:
    p.currentRoom = r_outside.id
    p.save()
