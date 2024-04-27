# Code challenge Treasure Map Exercise
row1 = ["🫰"] * 3
row2 = ["🤌"] * 3
row3 = ["🙏"] * 3

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")  # This is the way to print the map