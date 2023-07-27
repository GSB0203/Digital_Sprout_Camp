# 터틀런 만들기1
import turtle as t
import random

score=0
playing=False
green_food_count = 0

te2 = t.Turtle()     # 악당 거북이(빨간색)
te2.shape("circle")
te2.color("red")
te2.speed(0)
te2.up()
te2.goto(0, 200)
te2.hideturtle()

te = t.Turtle()     # 악당 거북이(빨간색)
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()     # 먹이(초록색 동그라미)
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)



def check_boundary():  # 화면 넘어가면 반대쪽에서 나옴
    x, y = t.position()
    screen_width = t.window_width() / 2
    screen_height = t.window_height() / 2

    if x > screen_width:
        t.goto(-screen_width, y)
    elif x < -screen_width:
        t.goto(screen_width, y)

    if y > screen_height:
        t.goto(x, -screen_height)
    elif y < -screen_height:
        t.goto(x, screen_height)


def turn_right():   # 오른쪽으로 방향을 바꿉니다.
    t.setheading(0)

def turn_up():      # 위로 방향을 바꿉니다.
    t.setheading(90)

def turn_left():    # 왼쪽으로 방향을 바꿉니다.
    t.setheading(180)

def turn_down():    # 아래로 방향을 바꿉니다.
    t.setheading(270)


def change_turtle_size():
    global green_food_count
    te.shapesize(1 + green_food_count * 0.1)  # 초록 먹이 먹은 횟수에 따라 크기 증가



def creat():
    x = random.randint(-230, 230)
    y = random.randint(-230, 230)
    te2.goto(x, y)
    
    
def start():
    global playing
    if playing == False:
        playing = True
        t.clear()

        play()

def play():         # 게임을 실제로 플레이하는 함수입니다.

    global score
    global playing


    t.forward(10)
    t.ontimer(creat, 50000)

    if random.randint(1, 5)==3:
        ang = te2.towards(t.pos())
        te2.setheading(ang)
    if random.randint(1, 5)==3:
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed=score+3
    if speed>15:
        speed=15
    te.forward(speed)
    if t.distance(te)<12:
        text="Score : "+str(score)
        message("Game Over", text)
        playing=False
        score=0
    if t.distance(te2)<12:
        text="Score : "+str(score)
        message("Game Over", text)
        playing=False
        score=0
    if t.distance(ts)<12: # 주인공과 먹이와의 거리가 12보다 작을 때(가깝게 있으면)

        score=score+1
        t.write(score)
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)         # 먹이를 다른 곳으로 옮깁니다.
        if score % 5 == 0:
            global green_food_count
            green_food_count += 1
            change_turtle_size()
            te2.showturtle()
    check_boundary()   
    if playing:           # 주인공과 악당의 거리가 12이상이면 (멀리 있으면)
        t.ontimer(play, 50)           # 0.1초후 play 함수를 실행합니다(게임을 계속 합니다).
        


def message(m1, m2):
    t.clear()
    t.goto(0,100)
    t.write(m1, False, "center",("",20))
    t.goto(0,-100)
    t.write(m2,False, "center",("",15))

t.title("Turtle Run")
t.setup(500, 500)
t.bgcolor("black")
t.shape("turtle")   # ‘거북이 모양’의 커서를 사용합니다.
t.speed(0)          # 거북이 속도를 가장 빠르게로 지정합니다.
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")   # [→]를 누르면 turn_right 함수를 실행하도록 합니다.
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()          # 거북이 그래픽 창이 키보드 입력을 받도록 합니다.
message("Turtle Run", "[Space]")            
