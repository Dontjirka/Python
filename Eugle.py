import sys

def isEugle(g):
    h = []
    e = []
    idk = 0
    for i in g:
        h.append(sum(i))
    for j in h:
        e.append(j%2)
    for k in e:
        if k == 1:
            idk += 1
            if idk == 3:
                return False
    return True

print("Enter nums: ")
g = []
nums = input()
running = True

'''
while running:

'''

if nums:
    try:
        int(nums)
    except ValueError:
        print("Please enter a number")
        sys.exit()

else:
    print("write something you stupido")
    sys.exit()
print("k")
