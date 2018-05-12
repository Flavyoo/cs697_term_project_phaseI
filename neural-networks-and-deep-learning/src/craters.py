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

    def add(self, center, radius):
        self.craters.append(Crater(center, radius))

    def found_crater(self, point, scale, s):
        x = float(point[0]) * pow(scale, -s)
        y = float(point[0]) * pow(scale, -s)
        for crater in self.craters:
            if crater.contains_pt([x, y]):
                return True
        return False


if __name__ == '__main__':

    # print "Testing Crater data structure"
    # crater = Crater([0,0], 10)
    # p_in = [1,1]
    # p_out = [40,40]
    # print crater.contains_pt(p_in)
    # print crater.contains_pt(p_out)

    print "\nTesting CraterList data structure"
    craters = CraterList()
    craters.add([0,0], 10)
    craters.add([0,0], 20)
    print craters.found_crater(p_in, 1, 0)
    print craters.found_crater(p_out, 1, 0)
    craters.add([0,0], 100)
    print craters.found_crater(p_out, 1, 0)
