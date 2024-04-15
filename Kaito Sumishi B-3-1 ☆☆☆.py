import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 201, 20): #a is the x axis of the starting point、Repeat every twenty intervals, Within the range of zero to two hundrend. 
     for b in range(0, 201, 20): #b is the x axis of the ending point、Repeat every twenty intervals, Within the range of zero to two hundrend. 
         pyxel.line(a, 0, b, 200, 0)#Draw a straight line from (a,0) to (b,200) 
pyxel.show()
