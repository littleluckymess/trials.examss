from turtle import*

screensize(3000, 3000)
tracer(False)
m = 10

for i in range(3):
    fd(32 * m)
    rt(90)
    fd(38 * m)
    rt(90)
up()
fd(25 * m)
rt(90)
fd(21 * m)
lt(90)
down()
for i in range(3):
    fd(29 * m)
    rt(90)
    bk(18 * m)
    rt(90)
up()
for x in range(0, 8):
    for y in range(-35, -16):
        goto(x * m, y * m)
        dot(3, 'purple')
update()
done()