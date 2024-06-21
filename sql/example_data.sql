-- -----------------------------------------------------
-- SCOTT example data
-- -----------------------------------------------------

-- DEPT

INSERT INTO `scott`.`dept` (`DEPTNO`, `DNAME`, `LOC`) VALUES ('1', 'IT', 'Chihuahua');
INSERT INTO `scott`.`dept` (`DEPTNO`, `DNAME`, `LOC`) VALUES ('2', 'RH', 'Hermosillo');
INSERT INTO `scott`.`dept` (`DEPTNO`, `DNAME`, `LOC`) VALUES ('3', 'Cont', 'CDMX');

-- EMP
INSERT INTO `scott`.`emp` (`EMPNO`, `ENAME`, `JOB`, `MGR`, `HIREDATE`, `SAL`, `COMM`, `DEPTNO`) VALUES ('1', 'Erick', 'Dev', '1', '1996-12-8', '36000', '720', '1');
INSERT INTO `scott`.`emp` (`EMPNO`, `ENAME`, `JOB`, `MGR`, `HIREDATE`, `SAL`, `COMM`, `DEPTNO`) VALUES ('2', 'David', 'Dev', '1', '2000-11-9', '20000', '720', '1');
INSERT INTO `scott`.`emp` (`EMPNO`, `ENAME`, `JOB`, `MGR`, `HIREDATE`, `SAL`, `COMM`, `DEPTNO`) VALUES ('3', 'Alice', 'RH', '3', '2000-12-26', '20000', '4684', '3');
INSERT INTO `scott`.`emp` (`EMPNO`, `ENAME`, `JOB`, `MGR`, `HIREDATE`, `SAL`, `COMM`, `DEPTNO`) VALUES ('4', 'Rebeca', 'Acc', '4', '1998-12-8', '26000', '1500', '4');

