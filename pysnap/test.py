from pprint import pprint
from pysnap import Snapchat

s = Snapchat()
s.login('lokikoki777', 'asdfghjkl1')
snaps = s.get_snaps()

pprint(snaps)
