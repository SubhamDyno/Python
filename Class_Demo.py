class Line():
    def __init__(self, coor1, coor2):
        self.x1 = coor1[0];
        self.x2 = coor1[1];
        self.y1 = coor2[0];
        self.y2 = coor2[1];
    def distance(self):
        return ((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**0.5;
    def distance2(self):
        return ((coor1[1]-coor1[0])**2 + (coor2[1]-coor2[0])**2)**0.5

coor1 = (2,3);
coor2 = (9,8);

L = Line(coor1,coor2);
print(L.distance());
print(L.distance2());
