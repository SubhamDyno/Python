class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1;
        self.coor2 = coor2;
    def distance(self):
        x1,x2 = self.coor1;
        y1,y2 = self.coor2;
        return ((x2-x1)**2 + (y2-y1)**2)**0.5;

coor1 = (2,3);
coor2 = (9,8);

L = Line(coor1,coor2);
print(L.distance());
L.distance()
