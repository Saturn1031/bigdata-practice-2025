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

# [질의 3-10] SELECT * FROM Emp WHERE job NOT IN ('MANAGER', 'CLERK');

# [질의 3-11] SELECT ename, job FROM Emp WHERE ename LIKE 'BLAKE';

# [질의 3-12] SELECT ename, job FROM Emp WHERE ename LIKE '%AR%';

# [질의 3-13] SELECT * FROM Emp WHERE ename LIKE '%AR%' AND sal >= 2000;

# [질의 3-14] SELECT * FROM Emp ORDER BY ename;

# [질의 3-15] SELECT SUM(sal) FROM Emp;

# [질의 3-16] SELECT SUM(sal) FROM Emp WHERE job LIKE 'SALESMAN';

# [질의 3-17] SELECT SUM(sal), AVG(sal), MIN(sal), MAX(sal) FROM Emp;

# [질의 3-18] SELECT COUNT(*) FROM Emp;

# [질의 3-19] SELECT COUNT(*), SUM(sal) FROM Emp GROUP BY job;

# [질의 3-20] SELECT * FROM Emp WHERE comm IS NOT NULL;

