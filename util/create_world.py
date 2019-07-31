from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance",
                 description="North of you, the mansion looms forebodingly.")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east and west.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_greatroom = Room(title="Great Room", description="""A cavernous room, the ceiling disappears in darkness. The cold floor tiles are covered with huge, darkly colored area rugs. Portraits of glaring ancestors hang on the walls, seemingly watching your every move.""")

r_library = Room(title="Library", description="""Full of dark wood and looming stuffed animal heads, it smells of ominous deeds and stale smoke. Light filters in from the french doors to the patio beyond.""")

r_hallway = Room(
    title="Hallway", description="""A wide hallway lined with banners and heraldry. Is that garlic?""")

r_terrace = Room(title="Terrace", description="""A wide stone terrace littered with overturned chairs, empty planter boxes, and dead birds. A few stone steps lead down to the Overlook.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_basement = Room(title="Dark Basement", description="""You're going to need a torch in here. Crates and boxes stacked everywhere. In the dust on the floor, some faint footprints lead off around the corner of some shelves.""")

r_secret = Room(title="Secret Passage",
                description="""Very narrow but high-ceilinged passage that twists and turns. An acrid smell gets stronger as you walk.""")

r_laboratory = Room(title="Laboratory", description="""Foul odors rise from buckets on the floor. Some of this large equipment must have been assembled pice by piece in here. What is that on the walls? """)

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
