import sqlite3
import sys





test_file = "newdata3.sqlite3"

lw= 'light'
ww= 'welt'
mw= 'middle'
lh= 'light'
hw ='heavy'
p4p= 'pound4pound'
conn = sqlite3.connect(test_file)
c = conn.cursor()



print " we need to update the fighter records constantly "
record = raw_input()
i_d = raw_input() 

c.execute("UPDATE light SET record=? where id=?", (record, i_d))## this should work but not sure why it is blocked 















print "incase a fighter gets relased from the ufc"

print " give the fighters ID"

data3 = raw_input() 
mydata = c.execute('DELETE FROM light WHERE id=?',(data3,))


print " What weight class do you want? "

line = raw_input()


if line == "lightweight":
	line="light"
	c.execute('select * from {tn}'\
        .format(tn=lw))
	all_rows = c.fetchall()
	for row in all_rows:
   		print row[0] , row[1], row[3], row[4]

elif line =="welterweight":
	line="welt"
	c.execute('select * from {tn}'\
        .format(tn=lw))
	all_rows = c.fetchall()
	for row in all_rows:
   		print row[0] , row[1], row[3], row[4]
elif line =="pound4pound":
	
	c.execute('select * from {tn}'\
        .format(tn=p4p))
	all_rows = c.fetchall()
	for row in all_rows:
   		print row[0] , row[1]
elif line == "compare"
 
	c.execute('select * from light where records = 0-0')
	all_rows = c.fetchall()
	for row in all_rows:
   		print row[0]


print " okay lets add in a fighter in the lightwieght divsion "

print " What is the fighters name " 
name = raw_input()
print "where is he from "
country = raw_input() 
print " what is his record " 
record = raw_input()
print "give him an ID that ends in a w"
ID = raw_input() 
print "give his nick name"
nickname= raw_input()

for newfighter in [(country,name,nickname,record,ID)]: 
	
	c.execute('insert into light values (?,?,?,?,?)',newfighter)

print "incase a fighter gets relased from the ufc"

print " give the fighters ID"

Data3 = raw_input() 
mydata = c.execute('DELETE FROM light WHERE id=?', (data3,))



conn.commit()

conn.close()	
	 

