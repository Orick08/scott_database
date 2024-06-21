-- -----------------------------------------------------
-- Schema SCOTT
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SCOTT` DEFAULT CHARACTER SET utf8 ;
USE `SCOTT` ;

-- -----------------------------------------------------
-- Table `SCOTT`.`DEPT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SCOTT`.`DEPT` (
  `DEPTNO` INT NOT NULL AUTO_INCREMENT,
  `DNAME` VARCHAR(14) NULL,
  `LOC` VARCHAR(13) NULL,
  PRIMARY KEY (`DEPTNO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SCOTT`.`EMP`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SCOTT`.`EMP` (
  `EMPNO` INT NOT NULL AUTO_INCREMENT,
  `ENAME` VARCHAR(10) NOT NULL,
  `JOB` VARCHAR(8) NULL,
  `MGR` INT NULL,
  `HIREDATE` DATE NULL,
  `SAL` DECIMAL NULL,
  `COMM` DECIMAL NULL,
  `DEPTNO` INT NOT NULL,
  PRIMARY KEY (`EMPNO`),
  INDEX `fk_EMP_DEPT_idx` (`DEPTNO` ASC) VISIBLE,
  CONSTRAINT `fk_EMP_DEPT`
    FOREIGN KEY (`DEPTNO`)
    REFERENCES `SCOTT`.`DEPT` (`DEPTNO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
