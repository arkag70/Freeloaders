
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
            self.xrev(damp)
        #object on right
        if (self.ypos >= y and self.ypos <= (y + height)) and (self.xpos + self.breadth) > (x):
            self.xrev(damp)

        #object on top
        if (self.xpos >= x and self.xpos <= (x + width)) and self.ypos <= (y+height):
            self.yrev(damp)
        #object on bottom
        if (self.xpos >= x and self.xpos <= (x + width)) and (self.ypos + self.length) > y:
            self.yrev(damp)

        

    def xrev(self, damp):
        self.xvel *= -1
        self.xacc *= damp
    
    def yrev(self, damp):
        self.yvel *= -1
        self.yacc *= damp