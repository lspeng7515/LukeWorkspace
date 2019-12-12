from PythonTest.PyDemo.com.luke.py.db.MyDB import MyDB
db=MyDB('localhost','root','123123','runoob_db')
aaa='testname'
url='testurl'
db.cursor.execute('insert into runoob_db.sites values (%s,%s)',[aaa,url])
db.db.commit()