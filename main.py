#pip install mojang

from mojang import MojangAPI
username = input("Please enter a Minecraft Username to convert to a UUID : ")

uuid = MojangAPI.get_uuid(username)

print("Username Request: {} UUID: {}".format(username, uuid))

test = input("press any key to exit")
