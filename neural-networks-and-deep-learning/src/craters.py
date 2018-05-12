from math import pow

class Crater(object):

    def __init__(self, center, radius):
        self.x = float(center[0])
        self.y = float(center[1])
        self.radius = float(radius)

    def contains_pt(self, point):
        x = float(point[0])
        y = float(point[1])
        r2 = self.radius * self.radius
        return pow(x - self.x, 2) + pow(y - self.y, 2) < r2

class CraterList(object):

    def __init__(self):
        self.craters = []

    def size(self):
        return len(self.craters)

    def get_crater(self, i):
        return self.craters[i]

    def add(self, center, radius):
        self.craters.append(Crater(center, radius))

    def found_crater(self, point, scale, s):
        x = float(point[0]) * pow(scale, -s)
        y = float(point[1]) * pow(scale, -s)
        for crater in self.craters:
            if crater.contains_pt([x, y]):
                return True
        return False


if __name__ == '__main__':

    print "Testing Crater data structure"
    crater = Crater([0,0], 8)
    p_in = [1.3,2.9]
    p_out = [40,40]
    print crater.contains_pt(p_in)
    print crater.contains_pt(p_out)

    print "\nTesting CraterList data structure"
    craters = CraterList()
    #craters.add([0,0], 10)
    craters.add([0,0], 8)
    print craters.found_crater(p_in, 1, 0)
    print craters.found_crater(p_out, 1, 0)
    #craters.add([0,0], 100)
    scale = 2
    for s in range(-4, 4, 1):
        x = float(p_in[0]) * pow(scale, -s)
        y = float(p_in[1]) * pow(scale, -s)
        print "[%s, %s] in craters: %s" \
                    % (x,y,craters.found_crater(p_in, scale, s))
