# 创建student表
```
CREATE TABLE student (Id INT(10) PRIMARY KEY NOT NULL auto_increment UNIQUE ,Name VARCHAR(20) NOT NULL ,
Sex VARCHAR(4) ,Birth YEAR,Department VARCHAR(20) NOT NULL,Address VARCHAR(50));
```
# 创建score表
```

CREATE  TABLE  score (id  INT(10)  NOT NULL  UNIQUE  PRIMARY KEY  AUTO_INCREMENT ,
										stu_id  INT(10)  NOT NULL ,
										c_name  VARCHAR(20) ,
										grade  INT(10));
```
## 插入数据
```
INSERT INTO student VALUES( 101,'张大', '男',1985,'计算机系', '北京市朝阳群众');
INSERT INTO student VALUES(102,'张小', '男',1986,'中文系', '北京市中关村');
INSERT INTO student VALUES( 103,'张三', '女',1990,'中文系', '湖南省永州市');
INSERT INTO student VALUES( 104,'李若彤', '女',1990,'英语系', '辽宁省沈阳市');
INSERT INTO student VALUES( 105,'刘亦菲', '女',1991,'英语系', '福建省泉州');
INSERT INTO student VALUES( 106,'王安石', '男',1988,'计算机系', '湖南省常德市');
```
## 插入数据
```
INSERT INTO score VALUES(NULL,101, '计算机',98);
INSERT INTO score VALUES(NULL,101, '英语', 80);
INSERT INTO score VALUES(NULL,102, '计算机',65);
INSERT INTO score VALUES(NULL,102, '中文',88);
INSERT INTO score VALUES(NULL,103, '中文',95);
INSERT INTO score VALUES(NULL,104, '计算机',70);
INSERT INTO score VALUES(NULL,104, '英语',92);
INSERT INTO score VALUES(NULL,105, '英语',94);
INSERT INTO score VALUES(NULL,106, '计算机',90);
INSERT INTO score VALUES(NULL,106, '英语',85);
```

3.查询书所有记录

```
SELECT * FROM student;
```

4.查询第2条到底4条

```
SELECT * FROM student LIMIT 1,3;
```

5.查询学号，姓名、院系

```
SELECT id ,name ,department FROM student;
```

6.查询计算机系和英语系的学生

```
SELECT * FROM student WHERE department IN ('计算机系','英语系');
```

7.查询年龄18~22岁的

```
SELECT * FROM student WHERE (YEAR(now())-birth) BETWEEN 18 AND 22;
```

8.查询每个院系有多少人

```
SELECT department,COUNT(*) AS '人数' FROM student GROUP BY department;
```

10.查询李四的考试科目和考试成绩

```
SELECT b.c_name,b.grade FROM student a JOIN score b ON a.Id=b.stu_id AND a.`Name`='王安石';
```

11.用连接的方式查询所有学生的信息和考试信息

```
SELECT * FROM student LEFT JOIN score ON student.Id=score.stu_id;
```

12.计算每个学生的总成绩

```
SELECT student.id,name,SUM(grade) FROM student,score WHERE student.id=score.stu_id GROUP BY Id;
```

13.计算每个考试科目的平均成绩

```
SELECT c_name, AVG(grade) '平均成绩'FROM score GROUP BY c_name;
```

14.查询计算机成绩低于95的学生信息

```
SELECT * FROM student a JOIN score b ON a.Id=b.stu_id AND c_name='计算机' AND b.grade<95;
SELECT * FROM student a LEFT JOIN score b ON a.id=b.stu_id WHERE c_name='计算机' AND b.grade<95;
SELECT * FROM student WHERE Id IN (SELECT stu_id FROM score WHERE grade<95 AND c_name='计算机');
```

15.查询同时参加计算机和英语考试的学生信息

```
SELECT *  FROM student WHERE Id IN( SELECT stu_id FROM score WHERE stu_id IN 
								(SELECT stu_id FROM score WHERE c_name=  '计算机')AND c_name= '英语' );

```

16.将计算机考试成绩按从高到低进行排序

```
SELECT c_name , grade FROM score WHERE c_name='计算机' ORDER BY grade DESC
```

18.查询姓张或者姓王的同学的姓名、院系、考试科目和成绩

```
SELECT  a.`Name` ,a.department, b.c_name , b.grade FROM student a JOIN score b ON a.Id=b.stu_id AND (a.Name LIKE '张%' OR a.Name LIKE '王%')
```

19.查询湖南的学生姓名年龄院系考试科目和成绩

```
SELECT `Name`,(YEAR(NOW())- Birth) AS '年龄', department, c_name, grade FROM student AS a, score AS b WHERE a.Address LIKE '湖南%' AND a.Id=b.stu_id;
```

20.把张三的姓名改为张三丰，课程改为Java 分数100

```
UPDATE student a, score b SET a.`Name`='张三丰' ,b.c_name='java',b.grade='100'  WHERE a.`Name`='张三'  AND b.stu_id=a.Id
```