blocks = int(input("Enter the number of blocks: "))
block_need = 0
height = 0

#
# Write your code here.
while True:
    height += 1
    block_need += height
    if block_need>blocks:
        print("Insufficient blocks, can't make further")
        height -=1
        break

print("Current height of the pyramid is:  ", height)

