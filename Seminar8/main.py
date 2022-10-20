import init_enter as init
import user_interface as intf


#conn = sqlite3.connect('orders.db')
#conn = sqlite3.connect(":memory:")

init.CreateDB()
intf.StartMenu()

# cur.execute("""INSERT INTO users(userid, fname, lname, gender)
#    VALUES('00001', 'Alex', 'Smith', 'male');""")
# conn.commit()
# user = ('00003', 'Lois', 'Lane', 'Female')
# cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
# conn.commit()
#
# cur.execute("SELECT * FROM users;")
# all_results = cur.fetchall()
# print(all_results)