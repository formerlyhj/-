# 创建Education库
```
CREATE DATABASE `Education` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```
# 创建表
## 表s
```
CREATE TABLE s (sno INT(10) PRIMARY KEY ,sname VARCHAR(40) NOT NULL ,age INT(10),sex VARCHAR(4), sdept VARCHAR(255));
```
## 表sc
```
CREATE TABLE sc (sno INT(10) ,cno VARCHAR(255),grade INT(20));
```
## 表c
```
CREATE TABLE c (cno int(10) PRIMARY KEY, cname VARCHAR(255), cdept VARCHAR(255), tname VARCHAR(255));
```

1.查询所有年龄20岁以下的学生姓名和年龄

```
SELECT sname,age FROM s WHERE age<20;
```
2.查询考试成绩有不及格的学生的学号

```
SELECT DISTINCT sno FROM sc WHERE grade<60;
```
3.查询年龄在20-23岁之间的学生姓名，系别和年龄

```
SELECT sname ,sdept,age FROM s WHERE age BETWEEN 20 AND 23;
```
4.查询计算机系数学系信息系的学生姓名和性别

```
SELECT sname, sex FROM s WHERE sdept in ('cp','math','is');
```
5.查既不是计算机系数学系又不是信息系的学生姓名和性别

```
SELECT sname ,sex FROM s WHERE sdept NOT IN ('cp','math','is');
```
6.查所有姓“刘”的学生的姓名、学号和性别。

```
SELECT sname ,sno ,sex FROM s WHERE sname LIKE '刘%';
```
7：查姓“上官”且全名为3个汉字的学生姓名。

```
SELECT sname FROM s WHERE sname LIKE '上官__';
```
8：查所有不姓“张”的学生的姓名。

```
SELECT sname FROM s WHERE sname NOT LIKE '张%';
```
9：查DB_Design课程的课程号。

```
SELECT cno FROM c WHERE cname LIKE 'DB_Design';
```
10：查缺考的学生的学号和课程号。

```
SELECT sno,cno FROM sc WHERE grade IS NULL;
```
11：查年龄为空值的学生的学号和姓名。

```
SELECT sno,sname FROM s WHERE age IS NULL;
```
12：查计算机系20岁以下的学生的学号和姓名。

```
SELECT sno ,sname FROM s WHERE sdept='cp' AND age <20;
```
13：查计算机系、数学系、信息系的学生姓名、性别

```
SELECT sname ,sex FROM s WHERE sdept IN ('cp','math','is');
```
14：查询选修了C3课程的学生的学号和成绩，其结果按分数的降序排列。

```
SELECT sno,grade FROM sc WHERE cno='c3' ORDER BY grade DESC;
```
15：查询全体学生的情况，查询结果按所在系升序排列，对同一系中的学生按年龄降序排列。

```
SELECT * FROM s ORDER BY sdept ,age DESC;
```
16：查询学生总人数。

```
SELECT COUNT(*) AS '总人数' FROM s;
```
17：查询选修了课程的学生人数。

```
SELECT COUNT(DISTINCT sno ) FROM sc;
```
18：计算选修了C1课程的学生平均成绩。

```
SELECT AVG(grade) FROM sc WHERE cno='c1';
```
19：查询学习C3课程的学生最高分数。

```
SELECT MAX(grade) FROM sc WHERE cno='c3';
```
20：查询各个课程号与相应的选课人数。

```
SELECT cno ,COUNT(sno) FROM sc GROUP BY cno;
```
21：查询计算机系选修了3门以上课程的学生的学号。

```
SELECT sno FROM sc WHERE sdept ='cp' GROUP BY sno HAVING COUNT(*)>3;
```
22：求基本表S中男同学的每一年龄组（超过50人）有多少人？要求查询结果按人数升序排列，人数相同按年龄降序排列。

```
SELECT age,COUNT(sno) FROM s WHERE sex='男' GROUP BY age HAVING COUNT(*)>50 ORDER BY 2,age DESC;
```
23：查询每个学生及其选修课程的情况。

```
SELECT s.sno,sname ,age,sex,sdept ,cno,grade FROM s ,sc WHERE s.sno=sc.sno;
```
24：查询选修了C2课程且成绩在90分以上的所有学生。

```
SELECT s.sno,sname FROM s,sc WHERE s.sno=sc.sno AND sc.cno='c2' AND sc.grade>90;
```
25：查询每个学生选修的课程名及其成绩。

```
SELECT s.sno ,sname ,cname,sc.grade FROM s,sc,c WHERE s.sno=sc.sno AND sc.cno=c.cno;
```
26：统计每一年龄选修课程的学生人数。

```
SELECT age, COUNT(DISTINCT s.sno) FROM s,sc WHERE s.sno=sc.sno GROUP BY age;
```
27：查询选修了C2课程的学生姓名。

```
SELECT sname FROM s WHERE sno IN (SELECT sno FROM sc WHERE cno='c2');
```
28：查询与“张三”在同一个系学习的学生学号、姓名和系别。

```
SELECT sno,snaem,sdept FROM s WHERE sdept IN (SELECT sdept FROM s WHERE sname='张三');
```
29：查询选修课程名为“数据库”的学生学号和姓名。

```
SELECT sno,sname FROM s WHERE sno IN (SELECT sno FROM sc WHERE cno IN (SELECT cno FROM c WHERE cname='数据库'));
```
30：查询与“张三”在同一个系学习的学生学号、姓名和系别。

```
SELECT sno,snaem,sdept FROM s WHERE sdept IN (SELECT sdept FROM s WHERE sname='张三');
```
31：查询选修课程名为“数据库”的学生学号和姓名。(同29)

32：查询选修了C2课程的学生姓名。（同27）

33：查询所有未选修C2课程的学生姓名。

```
SELECT sname FROM s WHERE NOT EXISTS (SELECT * FROM sc WHERE sno=s.sno AND cno='c2');
```
34：查询与“张三”在同一个系学习的学生学号、姓名和系别。

```
SELECT sno,sname,sdept FROM s AS s1 WHERE EXISTS (SELECT * FROM	s AS s2 WHERE s2.sdept=s1.sdept AND s2.sname='张三');
```
35：查询选修了全部课程的学生姓名。

```
SELECT sname FROM s WHERE NOT EXISTS (SELECT * FROM c WHERE NOT
 EXISTS(SELECT * FROM sc WHERE sno=s.sno AND cno=c.cno));
```
36：查询所学课程包含学生S3所学课程的学生学号

```
SELECT DISTINCT sno FROM sc a WHERE NOT EXISTS 
                            (SELECT * FROM sc b WHERE b.sno='s3' AND NOT EXISTS
                            (SELECT * FRO	sc c WHERE c.sno=a.sno AND c.cno=b.cno));
```