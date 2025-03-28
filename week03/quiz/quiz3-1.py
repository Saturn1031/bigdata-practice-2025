# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 13:37:47 2025

@author: DS
"""

import numpy as np
import pandas as pd

# [질의 3-1] emp.csv를 읽어서 DataFrame emp 만들기
emp = pd.read_csv('emp.csv')

# [질의 3-2] SELECT * FROM Emp;
emp
emp.loc[:, :]
emp.iloc[:, :]

# [질의 3-3] SELECT ename FROM Emp;
emp.ENAME
emp['ENAME']
emp.loc[:, 'ENAME']
emp.loc[:]['ENAME']
emp.iloc[:, 1]

# [질의 3-4] SELECT ename, sal FROM Emp;
emp[['ENAME', 'SAL']]
emp.loc[:, ['ENAME', 'SAL']]
emp.iloc[:, [1, 5]]

# [질의 3-5] SELECT DISTINCT job FROM Emp;
emp['JOB'].unique()
emp['JOB'].drop_duplicates()

# [질의 3-6] SELECT * FROM Emp WHERE sal < 2000;
emp[emp.SAL < 2000]

# [질의 3-7] SELECT * FROM Emp WHERE sal BETWEEN 1000 AND 2000;
emp[(emp.SAL >= 1000) & (emp.SAL <= 2000)]

# [질의 3-8] SELECT * FROM Emp WHERE sal >= 1500 AND job = ‘SALESMAN’;
emp[(emp.SAL >= 1500) & (emp.JOB == 'SALESMAN')]

# [질의 3-9] SELECT * FROM Emp WHERE job IN ('MANAGER', 'CLERK');
emp[emp.JOB.isin(['MANAGER', 'CLERK'])]

# [질의 3-10] SELECT * FROM Emp WHERE job NOT IN ('MANAGER', 'CLERK');
emp[~emp.JOB.isin(['MANAGER', 'CLERK'])]

# [질의 3-11] SELECT ename, job FROM Emp WHERE ename LIKE 'BLAKE';
emp[emp.ENAME == 'BLAKE'][['ENAME', 'JOB']]

# [질의 3-12] SELECT ename, job FROM Emp WHERE ename LIKE '%AR%';
emp[emp.ENAME.str.contains('AR')][['ENAME', 'JOB']]

# [질의 3-13] SELECT * FROM Emp WHERE ename LIKE '%AR%' AND sal >= 2000;
emp[(emp.ENAME.str.contains('AR')) & (emp.SAL >= 2000)]

# [질의 3-14] SELECT * FROM Emp ORDER BY ename;
emp.sort_values('ENAME')

# [질의 3-15] SELECT SUM(sal) FROM Emp;
emp.SAL.sum()

# [질의 3-16] SELECT SUM(sal) FROM Emp WHERE job LIKE 'SALESMAN';
emp[emp.JOB == 'SALESMAN'].SAL.sum()

# [질의 3-17] SELECT SUM(sal), AVG(sal), MIN(sal), MAX(sal) FROM Emp;
emp.SAL.agg(['sum', 'mean', 'min', 'max'])

# [질의 3-18] SELECT COUNT(*) FROM Emp;
emp.count()

# [질의 3-19] SELECT COUNT(*), SUM(sal) FROM Emp GROUP BY job;
emp.groupby('JOB').SAL.agg(['count', 'sum'])

# [질의 3-20] SELECT * FROM Emp WHERE comm IS NOT NULL;
emp[emp.COMM.notna()]

# [질의 4-0] emp.csv를 읽어서 DataFrame emp 만들기
emp = pd.read_csv('emp.csv')

# [질의 4-1] emp에 age 열을 만들어 다음을 입력하여라(14명)
# [30,40,50,30,40,50,30,40,50,30,40,50,30,40]
emp["AGE"] = [30, 40, 50, 30, 40, 50, 30, 40, 50, 30, 40, 50, 30, 40]
emp

# [질의 4-2] INSERT INTO Emp(empno, ename, job) Values (9999, ‘ALLEN’, ‘SALESMAN’)
df4_2 = pd.DataFrame([{"EMPNO": 9999, "ENAME": "ALLEN", "JOB": "SALESMAN"}])
emp = pd.concat([emp, df4_2], ignore_index = True)
emp

# [질의 4-3] emp의 ename=‘ALLEN’ 행을 삭제하여라
# (DELETE FROM emp WHERE ename LIKE ‘ALLEN’;)
emp = emp.drop(emp[emp["ENAME"] == "ALLEN"].index).reset_index(drop=True)
emp

# [질의 4-4] emp의 hiredate 열을 삭제하여라
# (ALTER TABLE emp DROP COLUMN hiredate;)
emp = emp.drop(columns=["HIREDATE"])
emp

# [질의 4-5] emp의 ename=‘SCOTT’의 sal을 3000으로 변경하여라
# (UPDATE emp SET sal=3000 WHERE ename LIKE ‘SCOTT’;)
emp.loc[emp["ENAME"] == "SCOTT", "SAL"] = 3000
emp

# [질의 5-1] emp의 sal 컬럼을 oldsal 이름으로 변경하여라.
# (ALTER TABLE emp RENAME sal TO oldsal;)
emp = emp.rename(columns={"SAL": "OLDSAL"})
emp

# [질의 5-2] emp에 newsal 컬럼을 추가하여라, 값은 oldsal 컬럼값
# (ALTER TABLE emp ADD newsal ...;)
emp["NEWSAL"] = emp["OLDSAL"]
emp

# [질의 5-3] emp의 oldsal 컬럼을 삭제하여라
# (ALTER TABLE emp DROP COLUMN oldsal;)
emp = emp.drop(columns=["OLDSAL"])
emp
