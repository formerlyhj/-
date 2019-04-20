# 建表
```
CREATE TABLE emoloyee1(name VARCHAR(20) ,sex VARCHAR(5) , age INT(10),address VARCHAR(20));
```

1.年龄大于20

```
SELECT * FROM emoloyee1 WHERE age >20;
```

2.年龄小于25的女员工

```
SELECT * FROM emoloyee1 WHERE age <25 AND sex ='女';
```

3.统计男女员工各有多少

```
SELECT sex ,COUNT(*) FROM emoloyee1 GROUP BY sex;
```

4.按照年龄顺序

```
SELECT * FROM emoloyee1 ORDER BY age;
```

5.重名

```
SELECT `Name` FROM emoloyee1 GROUP BY `Name` HAVING COUNT(*)>1;
```

6.查询张姓员工

```
SELECT * FROM emoloyee1 WHERE `Name` LIKE '张%';
```

7.查询地址为北京的前三条

```
SELECT * FROM emoloyee1 WHERE address = '北京' LIMIT 3;
```

8.员工总数

```
SELECT COUNT(*) FROM emoloyee1 `Name`; 
```

9.插入数据

```
INSERT INTO emoloyee1 VALUES('杨过', '男','26','襄阳');
```

10.修改张四的住址为南京

```
 UPDATE emoloyee1 SET emoloyee1.address='南京' WHERE name = '张四'; 
```

11.删除年龄大于24的女员工

```
DELETE FROM emoloyee1 WHERE age>24 AND sex ='女';
```