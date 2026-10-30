from math import pi

pos = [
    [ 250, 945, 0, 0, 0, 0 ],
    [ -250, 945, 0, 0, 0, 0 ],
    [ -250, -945, 0, 0, 0, 0 ],
    [ 250, -945, 0, 0, 0, 0 ],
    [ 750, 945, 0, 0, 0, 0 ],
    [ -750, 945, 0, 0, 0, 0 ],
    [ -750, -945, 0, 0, 0, 0 ],
    [ 750, -945, 0, 0, 0, 0 ],
    [ 0, 500, 0, 0, 0, pi/2 ],
    [ 0, -500, 0, 0, 0, pi/2 ],
]

for i in range(len(pos)):
    pos[i][0] /= 1000
    pos[i][1] /= 1000
    pos[i][2] += 0.11/2

i = 0
def uid():
    global i
    i += 1
    return i

for p in pos:
    for a in range(3):
        print('<include> <uri>pierre</uri> <name>pierre{}</name> <pose>{} {} {} {} {} {}</pose> </include>'.format(uid(), *p))
        p[2] += 0.11
