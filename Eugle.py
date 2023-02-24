import sys

#######################################################
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
#######################################################

#######################################################
def pathExists():
    return
#######################################################

#######################################################
class FIFO():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, value):
        self.queue1.append(value)

    def pop(self):
        return self.queue1.pop(0)
#######################################################

#######################################################
print("Enter nums, seperate them by ',' and press 'ENTER' if you want to end one array, press '.' to end it all: ")
g = []
while True:
    row = input().strip()
    if row == ".":
        break
    row_nums = row.split(",")
    try:
        row_nums = [int(num) for num in row_nums]
    except ValueError:
        print("Please enter integers only")
        sys.exit()
    g.append(row_nums)

print(f"It is Eugle: {isEugle(g)}")
#######################################################
