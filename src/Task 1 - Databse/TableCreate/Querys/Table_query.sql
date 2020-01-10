CREATE SCHEMA IF NOT EXISTS `Shop`;
USE `Shop` ;
CREATE TABLE IF NOT EXISTS `Shop`.`Products` (`ID` INT NOT NULL,`Name` VARCHAR(45) NULL,`Description` VARCHAR(5000) NULL,`Calories` INT NULL,`Protein` INT NULL,`Fat` INT NULL,`Sodium` INT NULL,`Fiber` INT NULL,`Carbo` INT NULL,`Sugar` INT NULL,`Vitamins` INT NULL,`Price` INT NULL,PRIMARY KEY (`ID`),UNIQUE INDEX `Name_UNIQUE` (`Name` ASC) VISIBLE);
CREATE TABLE IF NOT EXISTS `Shop`.`Transactions` (`Type` VARCHAR(500) NOT NULL,`ID` INT NOT NULL AUTO_INCREMENT,`Products_Name` VARCHAR(45) NOT NULL,PRIMARY KEY (`ID`),INDEX `Fremd` (`Products_Name` ASC) VISIBLE,CONSTRAINT `Fremd`FOREIGN KEY (`Products_Name`)REFERENCES `Shop`.`Products` (`Name`)ON DELETE NO ACTION ON UPDATE NO ACTION)
CREATE TABLE IF NOT EXISTS `Shop`.`Customers` (`ID` INT NOT NULL,`Name` VARCHAR(45) NULL,`Surname` VARCHAR(45) NULL,`DateOfFirstContact` DATETIME NULL,`username` VARCHAR(45) NOT NULL,PRIMARY KEY (`ID`),UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE);
CREATE TABLE IF NOT EXISTS `Shop`.`Comments` ( `Body` VARCHAR(5000) NOT NULL, `Rating` INT NOT NULL, `Customers_ID` INT NOT NULL, `Products_Name` VARCHAR(45) NOT NULL, `ID` INT NOT NULL AUTO_INCREMENT, INDEX `fk_Comments_Customers1_idx` (`Customers_ID` ASC) VISIBLE, INDEX `fk_Comments_Products1_idx` (`Products_Name` ASC) VISIBLE, PRIMARY KEY (`ID`), CONSTRAINT `fk_Comments_Customers1` FOREIGN KEY (`Customers_ID`) REFERENCES `Shop`.`Customers` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `fk_Comments_Products1` FOREIGN KEY (`Products_Name`) REFERENCES `Shop`.`Products` (`Name`) ON DELETE NO ACTION ON UPDATE NO ACTION)
CREATE TABLE IF NOT EXISTS `Shop`.`User` (`USERID` INT NOT NULL,`ROLE` VARCHAR(45) NULL,`UserName_Hashed` VARCHAR(6000) NULL,`Password_Hashed` VARCHAR(6000) NULL,`Customers_ID` INT NOT NULL,PRIMARY KEY (`USERID`),INDEX `fk_User_Customers_idx` (`Customers_ID` ASC) VISIBLE,CONSTRAINT `fk_User_Customers`FOREIGN KEY (`Customers_ID`)REFERENCES `Shop`.`Customers` (`ID`)ON DELETE NO ACTION ON UPDATE NO ACTION);