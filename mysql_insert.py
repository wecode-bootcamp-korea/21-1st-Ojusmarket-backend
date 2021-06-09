import pymysql
import csv


# 개인 db 정보 
conn = pymysql.connect(
    user = 'root',
    passwd= '1234',
    host= '127.0.0.1',
    db = 'ojus',
    charset= 'utf8'
)

cursor = conn.cursor(pymysql.cursors.DictCursor)


sql = """INSERT INTO recipes(name ,image_url ,필드3..... ) values (%s, %s, %s  #필드 갯수에따라서 ) """  


f= open('csv 파일 위치','r',encoding = 'utf=8')
rd = csv.reader(f)


for line in rd :
    cursor.execute(sql, (line[0],line[1],line[2],line[3])) # field 갯수

conn.commit()
conn.close()
f.close()


