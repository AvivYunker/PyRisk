# color assign (human)
# level 0:
# "INITIAL CLAIM" (in player color)
# level 1:
# "0123456, select territory to claim" (in player color)

# color assign (computer)
# level 0:
# "INITIAL CLAIM" (in player color)
# level 1:
# "waiting for 0123456 to claim territory" (in player color)

# initial fortify (human)
# level 0:
# "INITIAL FORTIFY" (in player color)
# level 1:
# "0123456, select territory to fortify" (in player color)

# intial fortify (computer)
# level 0:
# "INITIAL FORTIFY" (in player color)
# level 1:
# "waiting for 0123456 to forify territory" (in player color)

# fortify (human)
# level 0:
# "FORTIFY" (in player color)
# level 1:
# "0123456, select territory to fortify" (in player color)

# fortify (computer)
# level 0:
# "FORTIFY" (in player color)
# level 1:
# "waiting for 0123456 to fortify territory" (in player color)

# attack (human)
# level 0:
# "ATTACK" (in player color)
# level 1 (left)
# "0123456, select attacking territory" (in player color)
# level 1 (right)
# "0123456, select territory to attack" (in player color)
# level 2 (left)
# "ATTACKER: ABCDE" (in player color)
# level 2 (right)
# "ATTACKED: EDCBA" (in foreign player color)
# DICE?
# SINGLE / AUTO

# attack (computer)
# level 0:
# "ATTACK" (in player color)
# level 1 (left)
# "waiting for 0123456 to select attacking territory" (in player color)
# level 1 (right)
# "waiting for 0123456 to select foreign territory" (in player color)
# level 2 (left)
# "attacking: ABCDE" (in player color)
# level 2 (right)
# "attacked: EDCBA" (in foreign player color)
# DICE?
# SINGLE / AUTO

# move (human)
# level 0:
# "MOVE" (in player color)
# level 1 (left)
# "0123456, select source territory"  (in player color)
# level 1 (right)
# "0123456, select destination territory" (in player color)

# move (computer)
# level 0:
# "MOVE"
# level 1 (left)
# "waiting for 0123456 to select source territory" (in player color)
# level 1 (right)
# "waiting for 0123456 to select destination territory" (in player color)
# level 2 (left)
# "source: ABCDE"
# level 2 (right)
# "destination: EDCBA"

# ERRORS:
# "0123456, cannot attack yourself" (in player color)
# "0123456, cannot attack allies" (in player color) (QWERTYU) (in allies color)
# "0124567, not enough forces for attacking" (in player color)
# "0123456, cannot select -foreign- (in foreign color) territory as attacker" (in player color)
# "0123456, not enough forces for moving (in player color)
# "0123456, ABCDE does not board with" (int player color) "EDCBA" (in foreign color)

# GROUPS:
# group_1 - WIDTH=1227 - countries.
# group_2 = WIDTH=1200 - hexagons.
# group_3 = WIDTH=1000 - pyramid, quick-triangles, serious-triangles, squares, stadium.
# group_4 = WIDTH=1300 - keyboard.

# level 0: 