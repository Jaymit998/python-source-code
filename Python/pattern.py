# python turtle code 9
# beautiful design in python 
import turtle as f
f.speed (20)
f.bgcolor('black')
c=['pink','white','green','cyan','yellow','red','magenta']
a=400
for i in range (a):
	f.penup()
	f.goto(10,0)
	f.fd(a/2)
	f.rt(10)
	f.pendown()
	f.begin_fill()
	f.color(c[i%7])
	for j in range (7):
		f.fd(a)
		f.rt(179)
f.rt(180)
f.mainloop()