# MySQL考试

### 第一题

```
SELECT DISTINCT a.teat_id from train as a LEFT JOIN train as b on a.teat_id=b.teat_id-1 or a.teat_id=b.teat_id+1 WHERE a.is_free=1 and b.is_free=1 ORDER BY a.teat_id;


```

### 第二题

```
SELECT a.name, b.bonus FROM employee a LEFT JOIN bonus b ON a.empid=b.empid WHERE b.bonus<1000 OR b.bonus IS NULL;
```
### 第三题

```
SELECT `name` FROM salesperson WHERE sales_id NOT IN (SELECT sales_id FROM `order` WHERE com_id=(SELECT com_id FROM company WHERE name='red'));
```

### 第四题

```
```

### 第五题

```
SELECT `name` FROM (SELECT CandidateId,COUNT(*) AS a FROM Vote GROUP BY CandidateId ORDER BY a DESC LIMIT 1)AS b JOIN Candidate ON b.CandidateId=Candidate.id; 
```