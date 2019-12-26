CREATE SCHEMA IF NOT EXISTS `Shop` DEFAULT CHARACTER SET utf8 ;
USE `Shop` ;
CREATE TABLE IF NOT EXISTS `Shop`.`Comments` (`ID` INT NOT NULL,`Body` VARCHAR(5000) NULL,`Rating` INT NULL,`Customers_ID` INT NOT NULL,`Products_ID` INT NOT NULL,PRIMARY KEY (`ID`),INDEX `fk_Comments_Customers1_idx` (`Customers_ID` ASC) VISIBLE,INDEX `fk_Comments_Products1_idx` (`Products_ID` ASC) VISIBLE,CONSTRAINT `fk_Comments_Customers1`FOREIGN KEY (`Customers_ID`)REFERENCES `Shop`.`Customers` (`ID`)ON DELETE NO ACTIONON UPDATE NO ACTION,CONSTRAINT `fk_Comments_Products1`FOREIGN KEY (`Products_ID`)REFERENCES `Shop`.`Products` (`ID`)ON DELETE NO ACTIONON UPDATE NO ACTION);
CREATE TABLE IF NOT EXISTS `Shop`.`Products` (`ID` INT NOT NULL,`Name` VARCHAR(45) NULL,`PrdouctNumber` VARCHAR(45) NULL,`Description` VARCHAR(5000) NULL,PRIMARY KEY (`ID`));
CREATE TABLE IF NOT EXISTS `Shop`.`Storrage` (`HowMany` INT NULL,`Products_ID` INT NOT NULL,PRIMARY KEY (`Products_ID`),INDEX `fk_Storrage_Products1_idx` (`Products_ID` ASC) VISIBLE,CONSTRAINT `fk_Storrage_Products1`FOREIGN KEY (`Products_ID`)REFERENCES `Shop`.`Products` (`ID`)ON DELETE NO ACTIONON UPDATE NO ACTION);
CREATE TABLE IF NOT EXISTS `Shop`.`Transactions` (`Products_ID` INT NOT NULL,`Type` VARCHAR(500) NULL,`ID` INT NOT NULL,INDEX `fk_Transactions_Products1_idx` (`Products_ID` ASC) VISIBLE,PRIMARY KEY (`ID`),CONSTRAINT `fk_Transactions_Products1`FOREIGN KEY (`Products_ID`)REFERENCES `Shop`.`Products` (`ID`)ON DELETE NO ACTIONON UPDATE NO ACTION);
CREATE TABLE IF NOT EXISTS `Shop`.`User` (`USERID` INT NOT NULL,`ROLE` VARCHAR(45) NULL,`UserName_Hashed` VARCHAR(500) NULL,`Password_Hashed` VARCHAR(500) NULL,`Customers_ID` INT NOT NULL,PRIMARY KEY (`USERID`),INDEX `fk_User_Customers_idx` (`Customers_ID` ASC) VISIBLE,CONSTRAINT `fk_User_Customers`FOREIGN KEY (`Customers_ID`)REFERENCES `Shop`.`Customers` (`ID`)ON DELETE NO ACTIONON UPDATE NO ACTION);
CREATE TABLE IF NOT EXISTS `Shop`.`Products` (`ID` INT NOT NULL,`Name` VARCHAR(45) NULL,`PrdouctNumber` VARCHAR(45) NULL,`Description` VARCHAR(5000) NULL,`Calories` INT NULL,`Protein` INT NULL,`Fat` INT NULL,`Sodium` INT NULL,`Fiber` INT NULL,`Carbo` INT NULL,`Sugar` INT NULL,`Vitamins` INT NULL,PRIMARY KEY (`ID`));