# noinspection SqlNoDataSourceInspectionForFile
/*
*********************************************************************
http://www.mysqltutorial.org
*********************************************************************
Name: MySQL Sample Database for Python
Link: http://www.mysqltutorial.org/
Version 1.0
*********************************************************************
*/

-- /*!40101 SET NAMES utf8 */;
-- 
-- /*!40101 SET SQL_MODE=``*/;
-- 
-- /*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
-- /*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
-- /*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE=`NO_AUTO_VALUE_ON_ZERO` */;
-- /*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
-- CREATE DATABASE /*!32312 IF NOT EXISTS*/`python_mysql` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `python_mysql`;

DROP TABLE IF EXISTS `projects`;
CREATE TABLE `projects` (
  `proj_id` int(11) NOT NULL AUTO_INCREMENT,a
  `name` varchar(255) NOT NULL,
  `company_id` int(11) NOT NULL,
  `proj_url` varchar(255),
  `patent_writer_id` int(11),
  PRIMARY KEY (`proj_id`)
) ENGINE=InnoDB AUTO_INCREMENT= 1 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Employees`;

CREATE TABLE `Employees` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_email` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT= 1 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Companies`;
CREATE TABLE `Companies` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT= 1 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Patent_Writers`;

CREATE TABLE `Patent_Writers` (
  `patent_writer_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `project_id` int(11),
  PRIMARY KEY (`patent_writer_id`)
) ENGINE=InnoDB AUTO_INCREMENT= 1 DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `M_Iterations`;

CREATE TABLE `M_Iterations` (
  `project_id` int(11) NOT NULL,
  `iteration_number` int(11) NOT NULL,
  `date` date NOT NULL,
  `sig_ord` int(2) NOT NULL,
  `text` text NOT NULL,
  `key_alterations` text
) ENGINE=InnoDB AUTO_INCREMENT= 1 DEFAULT CHARSET=latin1;
-- /*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
-- /*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
-- /*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
-- /*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;