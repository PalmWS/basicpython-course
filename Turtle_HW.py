import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #แปลงปากกาเป็นเต่า
def Rectangle():
    '''วาดรูปสี่เหลี่ยม'''
    for i in range(4):
        tao.forward(100)
        tao.left(90)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(200,200)
Rectangle()

for i in range(10):
    tao.circle(i*10)

    
tao.clear()
for i in range(10):
    tao.circle(i*10)
    tao.left(180)
    tao.circle(i*10)
    tao.left(180)

    
for i in range(10):
    tao.circle(90)
    tao.left(36)
