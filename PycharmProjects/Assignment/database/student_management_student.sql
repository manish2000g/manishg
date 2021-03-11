-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: student_management
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `First_Name` varchar(45) DEFAULT NULL,
  `Last_Name` varchar(45) DEFAULT NULL,
  `Class` varchar(45) DEFAULT NULL,
  `ID_No` int DEFAULT NULL,
  `Emai` varchar(45) DEFAULT NULL,
  `Contact` varchar(45) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('Sujit','Subedi','First Year(CS)',11750,'sujit22@gmail.com','9741701567','2000-06-09','kathmandu\n\n','Male'),('manish','gautam','Second Year(CS)',85193,'manish@gmail.com','123456789','2000-07-04','bhaktapur\n\n','Male'),('Sakriya ','Thapa','Third Year(CS)',12445,'sakriyathapa20@gmail.com','987456321','2000-12-03','lalitpur\n\n','Male'),('manish','gautam','first year',10012,'sujit22@gmail.com','123456789','2000-06-09','kathmandu','male'),('manish','gautam','first year',10012,'sujit22@gmail.com','123456789','2000-06-09','kathmandu','male'),('manish','gautam','first year',10012,'sujit22@gmail.com','123456789','2000-06-09','kathmandu','male'),('manish','gautam','first year',10012,'sujit22@gmail.com','123456789','2000-10-19','kathmandu','male'),('manish','gautam','first year',10022,'sujit22@gmail.com','123456789','2000-10-19','kathmandu','male'),('manish','gautam','first year',10022,'sujit22@gmail.com','123456789','2000-10-19','kathmandu','male'),('manish','gautam','first year',10022,'sujit22@gmail.com','123456789','2000-10-19','kathmandu','male'),('manish','gautam','first year',10022,'sujit22@gmail.com','123456789','2000-10-19','kathmandu','male'),('manish','gautam','first year',10022,'sujit22@gmail.com','123456789','2000-10-19','kathmandu','male'),('manish','gautam','first year',10022,'sujit22@gmail.com','123456789','2000-10-19','kathmandu','male'),('manish','gautam','first year',10022,'sujit22@gmail.com','123456789',NULL,'kathmandu','male'),('manish','gautam','first year',10032,'sujit22@gmail.com','123456789','2000-10-19','pokhara','male'),('manish','gautam','first year',10032,'sujit22@gmail.com','123456789','2000-10-19','pokhara','male'),('manish','gautam','first year',10032,'sujit22@gmail.com','123456789','2000-10-19','pokhara','male'),('manish','gautam','first year',10032,'sujit22@gmail.com','123456789','2000-10-19','pokhara','male');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-11 17:34:21
