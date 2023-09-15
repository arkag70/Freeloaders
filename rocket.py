from math import floor


AGE=1
DROP=50
class Rocket:

    def __init__(self, l, b, x, y, vx, vy, ax, ay) -> None:
        
        self.length = l
        self.breadth = b
        self.xpos = x
        self.ypos = y
        self.xvel = vx
        self.yvel = vy
        self.xacc = ax
        self.yacc = ay
        self.age = AGE
        self.red = 0
        self.green = 0
        self.blue = 255

    def move(self):

        self.xpos += self.xvel
        self.ypos += self.yvel

        self.xvel += self.xacc
        self.yvel += self.yacc

    def boundaryCheck(self, canvaswidth, canvasheight, damp):
        if(self.xpos < 0 or self.xpos > (canvaswidth - self.breadth)):
            self.xrev(damp)
        if(self.ypos < 0 or self.ypos > (canvasheight - self.length)):
            self.yrev(damp)
    
    def objectCheck(self, position, dimension, damp):
        x,y = position
        width,height = dimension

        #object on left
        if (self.ypos >= y and self.ypos <= (y + height)) and self.xpos <= (x+width):
            self.lifespan-=1
            self.xrev(damp)
        #object on right
        if (self.ypos >= y and self.ypos <= (y + height)) and (self.xpos + self.breadth) > (x):
            self.lifespan-=1
            self.xrev(damp)

        #object on top
        if (self.xpos >= x and self.xpos <= (x + width)) and self.ypos <= (y+height):
            self.yrev(damp)
        #object on bottom
        if (self.xpos >= x and self.xpos <= (x + width)) and (self.ypos + self.length) > y:
            self.yrev(damp)

    def onCollision(self):
        self.age+=1

        if self.blue > 0:
            self.blue = (self.blue - DROP) if (self.blue - DROP) > 0 else 0
            if self.green < 255:
                self.green = (self.green + DROP) if (self.green + DROP) < 255 else 255
        else:
            if self.green > 0:
                self.green = (self.green - DROP) if (self.green - DROP) > 0 else 0
                if self.red < 255:
                    self.red = (self.red + DROP) if (self.red + DROP) < 255 else 255

    def xrev(self, damp):
        self.xvel *= -1
        self.xacc *= damp
        self.onCollision()
    
    def yrev(self, damp):
        self.yvel *= -1
        self.yacc *= damp
        self.onCollision()