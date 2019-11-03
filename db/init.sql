CREATE DATABASE lostandfound;
use lostandfound;

CREATE TABLE `users` (
  `userid` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`userid`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC)
);
CREATE TABLE `items` (
  `itemid` INT NOT NULL AUTO_INCREMENT,
  `item_category` VARCHAR(100) NULL,
  `item_name` VARCHAR(100) NULL,
  `location` VARCHAR(100) NULL,
  `description` VARCHAR(500) NULL,
  `date` VARCHAR(100) NULL,
  PRIMARY KEY (`itemid`)
);
