CREATE DATABASE  IF NOT EXISTS `Webapp` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `Webapp`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(128) NOT NULL,
  `passwd` char(32) DEFAULT NULL,
  `is_admin` tinyint(1) NOT NULL DEFAULT '0',
  `is_suspended` tinyint(1) NOT NULL DEFAULT '0',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `account` (`account`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `applicants`;
CREATE TABLE `applicants` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;


INSERT INTO `users` VALUES (1,'admin','21232f297a57a5a743894a0e4a801fc3',1,0,0);
INSERT INTO `users` VALUES (2,'test@test.com','098f6bcd4621d373cade4e832627b4f6',0,0,0);

/* it's same as web-app/config/db_tool.py */
CREATE USER 'webapp'@'localhost' IDENTIFIED BY 'webapp@www';
GRANT ALL ON Webapp.* TO 'webapp'@'localhost';
