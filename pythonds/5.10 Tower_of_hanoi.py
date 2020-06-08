"""
Recursion:
At the beginning of time, the priests were given three poles and a stack of 64 gold disks, each disk a little smaller than the one beneath it. Their assignment was to transfer all 64 disks from one of the three poles to another, with two important constraints.

They could only move one disk at a time, and they could never place a larger disk on top of a smaller one. 

Here is a high-level outline of how to move a tower from the starting pole, to the goal pole, using an intermediate pole:

Move a tower of height-1 to an intermediate pole, using the final pole.
Move the remaining disk to the final pole.
Move the tower of height-1 from the intermediate pole to the final pole using the original pole.

"""
def moveTower(height, frompole, topole, withpole):
    if height >= 1:
        # we move all but the bottom disk on the initial tower to an intermediate pole.
        moveTower(height-1, frompole, withpole, topole)
        # The next line simply moves the bottom disk to its final resting place. 
        moveDisk(frompole, topole)
        # we move the tower from the intermediate pole to the top of the largest disk.
        moveTower(height-1, withpole, topole, frompole)



# All it does is print out that it is moving a disk from one pole to another.
def moveDisk(fp, tp):
    print(f"move from {fp} to {tp}")


moveTower(3, "A", "B", "C")