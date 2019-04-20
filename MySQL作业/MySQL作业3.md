# 建库
```
CREATE DATABASE `gongsi` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```
# 建表
```
CREATE TABLE 部门表 (b_id INT(10) PRIMARY KEY AUTO_INCREMENT, b_name VARCHAR(40) NOT NULL);
CREATE TABLE 员工表 (y_id INT(10) PRIMARY KEY AUTO_INCREMENT,y_name VARCHAR(20), y_sexVARCHAR(4),
y_age INT(10), y_addres VARCHAR(50) DEFAULT '不详',b_id INT(10), FOREIGN KEY(b_id) REFERENCES 部门表(b_id));
```
1.25 至 30岁之间男员工的姓名和地址

```
SELECT y_name,y_addres FROM 员工表  WHERE y_age BETWEEN 25 and 30;
```

2.财务部40岁以下员工

```
SELECT * FROM `员工表` a LEFT JOIN `部门表` b ON a.b_id=b.b_id WHERE a.y_age<40 AND b.b_name='财务部';
```

3.人事部年龄最大的女员工

```
Select * from `员工表` where y_age=(Select max(y_age)from `员工表` a,`部门表` b where b.b_id=a.b_id And y_sex='女' AND b_name='人事部')
And y_sex='女'AND b_id=(Select b_id from `部门表` where b_name='人事部');
```

4.加入新员工

```
INSERT INTO `员工表`(y_name,y_sex,y_age) VALUES ('王麻子','男','30');
```

5.将人事部年龄大于30的女同事，调入后勤部

```
UPDATE `员工表` SET b_id=113 WHERE y_age>30 AND y_sex='女' AND b_id =111;
```

6.查询每个部门年龄最大的员工，显示部门名字和年龄

```
SELECT b.b_name,MAX(y_age) FROM `员工表` a JOIN `部门表` b ON a.b_id=b.b_id GROUP BY a.b_id;
```

7.查询每个部门，按部门编号正序

```
SELECT b_name,COUNT(*) FROM `员工表` a,`部门表` b WHERE 
a.b_id=b.b_id 
GROUP BY b.b_id
ORDER BY COUNT(*)DESC,b.b_id ASC;
```

8.将张三的名字改为李四，并调到财务部

```
UPDATE `员工表` a SET a.y_name='李四' ,a.b_id=(SELECT b.b_id FROM `部门表` b WHERE b.b_name='财务部') WHERE a.y_name='张三';
```

9.将后勤部年龄大于60的员工删除

```
DELETE FROM `员工表`  WHERE y_age>60 AND `员工表`.b_id=(SELECT b.b_id FROM `部门表` b WHERE b.b_name='后勤部');
```

10.查询财务部年龄不在20-30之间的男生

```
SELECT * FROM `员工表` a JOIN`部门表` b ON a.b_id=b.b_id WHERE b.b_name='财务部' AND a.y_age NOT BETWEEN 20 AND 30;
```