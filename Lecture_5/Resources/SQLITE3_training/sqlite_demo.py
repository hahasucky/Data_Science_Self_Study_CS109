import sqlite3

#conn = sqlite3.connect('workers.db') # 결과가 쌓인다. 
conn = sqlite3.connect(':memory:') # 매번 돌릴 때 마다 업데이트 되어, 결과가 쌓이지 않는다. !! testing

c = conn.cursor()

c.execute("""CREATE TABLE employees(
	first text,
	last text,
	salary integer)
	""")

# make 2 instance and try to put it into the workers.db employees table
from employee_class import employee
emp_1 = employee('jeongwoo','han',1000)
emp_2 = employee('hyokyung','han',2000)
emp_3 = employee('hyokyung','kim',1500)
emp_4 = employee('hyo','lim',2001)

#c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first, emp_1.last, emp_1.salary))
#c.execute("INSERT INTO employees VALUES (:first,:last,:salary)",  # key of the dict to be passed 
#	{'first':emp_2.first, 'last':emp_2.last, 'salary':emp_2.salary})

#conn.commit()

#c.execute("INSERT INTO employees VALUES ('jihun','han',1000)") # 중복입력 가능
#conn.commit()

#c.execute("SELECT * FROM employees WHERE last = ?", ('han',)) # query of placeholder pass with ? and tuple,
#c.execute("SELECT * FROM employees WHERE last =:last", {'last': 'han'}) # placeholder pass with dict
#print(c.fetchall())

#conn.commit()
#conn.close()

# make an app
def insert_emp(emp):
	with conn: # automatically committed to the database i am working on.
		c.execute("INSERT INTO employees VALUES (:first,:last,:salary)",  # key of the dict to be passed 
		{'first':emp.first, 'last':emp.last, 'salary':emp.salary})

def get_emps_by_name(lastname):
	#with conn: no need to commit
	c.execute("SELECT * FROM employees WHERE last =:last", {'last': lastname})
	return c.fetchall()

def update_pay(emp, salary):
	with conn:
		c.execute("UPDATE employees SET salary = :salary WHERE first = :first AND last = :last",
			{'first': emp.first, 'last': emp.last, 'salary': salary})

def remove_emp(emp):
	with conn:
		c.execute("DELETE FROM employees WHERE first=:first AND last=:last",
			{'first': emp.first, 'last': emp.last})

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)
insert_emp(emp_4)
emps = get_emps_by_name('han')
print(emps)

update_pay(emp_2, 5000)
remove_emp(emp_1)
emps = get_emps_by_name('han')
print(emps)
