
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
        if(self.ypos < 0 or self.ypos > (canvasheight - self.length) ):
            self.yrev(damp)

    def xrev(self, damp):
        self.xvel *= -1
        self.xacc *= damp
    
    def yrev(self, damp):
        self.yvel *= -1
        self.yacc *= damp