# MySQL
创建库
```language
CREATE DATABASE `何健` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```
# 雇员表
```
create table emoloyee (empid INT(10) primary key, Name VARCHAR(255),sex VARCHAR (255),title VARCHAR(255) , birthday date,depid INT(10));

INSERT INTO emoloyee (empid,Name,sex,title,birthday,depid) VALUES ('1001','张三','男','高级工程师','1975-1-1','111');

INSERT INTO emoloyee (empid,Name,sex,title,birthday,depid) VALUES ('1002','李四','女','助工','1985-1-1','111');

INSERT INTO emoloyee (empid,Name,sex,title,birthday,depid) VALUES ('1003','王五','男','工程师','1978-11-11','222');

INSERT INTO emoloyee (empid,Name,sex,title,birthday,depid) VALUES ('1004','赵六','男','工程师','1979-1-1','222');
```
# 部门表
```
CREATE TABLE department (depid INT(10) primary key, depname VARCHAR(255),部门简介 VARCHAR(255) NULL);

INSERT INTO department (depid, depname) VALUES ('111', '生产部');

INSERT INTO department (depid, depname) VALUES ('222', '销售部');

INSERT INTO department (depid, depname) VALUES ('333', '人事部');
```
# 工资表
```
CREATE TABLE salary (empid INT(10) PRIMARY KEY, basesalary INT ,titlesalary INT ,deduction INT);

INSERT INTO salary (empid , basesalary , titlesalary , deduction) VALUES ('1001', '2200', '1100', '200');

INSERT INTO salary (empid , basesalary , titlesalary , deduction) VALUES ('1002', '1200', '200', '100');

INSERT INTO salary (empid , basesalary , titlesalary , deduction) VALUES ('1003', '1900', '700', '200');

INSERT INTO salary (empid , basesalary , titlesalary , deduction) VALUES ('1004', '1950', '700', '150');
```

更改李四职称和工资：

```
UPDATE emoloyee a,salary b SET a.title ='工程师', b.basesalary='1700' ,

b.titlesalary='600'  WHERE  a.empid=1002 AND b.empid=1002;
```

删除人事部：

```
DELETE FROM department WHERE depname='人事部';
```

查询雇员编号，实发工资和应发工资：

```
SELEC empid ,(basesalary+titlesalary-deduction) AS netpay,(basesalary+titlesalary) AS send_salary FROM salary;
```

姓张且年龄小于40：

```
SELECT *FROM emoloyee WHERE YEAR(CURDATE()) - YEAR(birthday)<40 AND Name LIKE '张%';
```

查询雇员的编号，姓名，职称，部门名称，实发工资

```
SELECT d.empid ,`Name`,title,depname,(basesalary+titlesalary-deduction) AS 实发工资 FROM salary LEFT JOIN (SELECT a.empid ,a.`Name`,a.title,b.depname FROM emoloyee AS a LEFT JOIN department AS b on a.depid= b.depid) AS d ON d.empid=salary.empid;
```

查询销售部的雇员姓名和工资：

```
SELECT a.empid,`Name`, b.depname, c.basesalary, c.titlesalary, c.deduction FROM emoloyee a JOIN department b ON a.depid =b.depid JOIN salary c ON a.empid =c.empid AND b.depname='销售部';
```

统计各职称的人数：

```
SELECT title, COUNT(*) AS 人数 FROM emoloyee GROUP BY title;
```

统计各部门的人数（扩展）： 

```
SELECT department.depname ,COUNT(*) AS 人数 FROM emoloyee JOIN department ON emoloyee.depid = department.depid GROUP BY emoloyee.depid
```

统计部门名称，实发工资和平均工资：
