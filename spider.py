from bs4 import BeautifulSoup
import lxml
import requests
import pymysql

soup =BeautifulSoup(open('demo.html',encoding='utf-8'),'lxml');
#print(soup.prettify());

table=soup.table;
#print (table);

counter=-1;
num=0;
TimeList=[];
day=0;
strnum=0;
id=0;

conn=pymysql.connect(host='localhost', user='root', password='root', database='spider', 
port=3306, charset='utf8')
cur=conn.cursor()
print("SQL Connected")

for trs in table.find_all("tr"):
    counter=counter+1;
    if counter==0:
        continue;
    elif counter==1:
        for tds in trs.find_all("td"):
            ind=tds.string;
            if ind == "0102":
                day=day+1;
                print("geted");
           # strnum=0;
            if ind!='教室\\节次':
                strnum=int(ind);
                strnum=day*10000+strnum;
            TimeList.append(strnum);
           # print(tds.string);
        print(TimeList);
    else:
        index=0;
        class_room="str";
        for tds in trs.find_all("td"):
            if index==0:
                class_room=tds.nobr.string;
            else:
                if tds.nobr.div != None:
                    #print(tds.nobr.div.get_text());
                    #print(TimeList[index]);
                    for divs in tds.find_all("div"):
                        classStr=divs.get_text('@','<br>');
                        print(classStr);
                        strlist='@'.join(classStr.split());
                        sqllist=strlist.split('@');
                        #print(sqllist);
                        id=id+1;
                        sql ='insert into sanxia (name,teacher,week,student,time,date,room) values (%s,%s,%s,%s,%s,%s,%s);';
                        time=str(TimeList[index]%10000);
                        date=str(int(TimeList[index]/10000));
                        print("inserted:",sqllist[0],sqllist[1],sqllist[2],sqllist[3],time,date,class_room);
                        cur.execute(sql, [sqllist[0],sqllist[1],sqllist[2],sqllist[3],time,date,class_room]);
                        print("ok");
                        conn.commit();

                    #print('@'.join(classStr.split()));
            index=index+1;
print(id);

    





