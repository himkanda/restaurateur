CREATE DATABASE  IF NOT EXISTS `restaurateur` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `restaurateur`;
-- MySQL dump 10.13  Distrib 8.0.33, for macos13 (arm64)
--
-- Host: localhost    Database: restaurateur
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` varchar(20) NOT NULL,
  `total_amount` decimal(5,0) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `orderId_UNIQUE` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1,'12',351),(2,'16',545),(3,'1',162);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Dosa',60),(2,'Bread Pakoda',15),(3,'Jalebi',40),(4,'Sambhar',30),(5,'Idli Vada',45),(6,'Pepsi 750ml',45),(7,'Cold Coffee',120),(8,'Palak Paneer',140),(9,'Shahi Paneer',160),(11,'Chaat',40),(12,'Rice',25),(13,'Chapati',5),(14,'Grilled Sandwich',80),(15,'Samosa',15),(16,'Cheese Burger',100);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_items`
--

DROP TABLE IF EXISTS `order_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `menu_id` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_items`
--

LOCK TABLES `order_items` WRITE;
/*!40000 ALTER TABLE `order_items` DISABLE KEYS */;
INSERT INTO `order_items` VALUES (1,1,5,2),(2,6,6,4),(3,6,9,1),(4,6,9,2),(5,6,3,3),(6,6,6,2),(7,6,5,1),(8,6,1,1),(9,9,8,1),(10,9,6,3),(11,9,4,2),(12,9,1,4),(13,12,1,1),(14,12,1,2),(15,12,9,1),(16,12,12,1),(17,12,9,1),(18,12,1,1),(19,15,16,2),(20,16,3,1),(21,16,16,2),(22,16,15,3),(23,16,5,4),(24,16,3,1),(27,1,1,1),(28,15,15,3);
/*!40000 ALTER TABLE `order_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(45) NOT NULL,
  `phone` varchar(45) DEFAULT '-',
  `email` varchar(45) DEFAULT '-',
  `order_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `order_type` varchar(45) NOT NULL,
  `reference` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'Ishu Gupta','8567349910','ishu.gupta@gmail.com','2023-06-20 10:10:33','Dine In','485G54GH5555555'),(2,'Bhoomika','7677251190','bhoomika@gmail.com','2023-06-20 11:19:33','Dine In','45G45VV5B55B5B5'),(3,'Bhumika','8999365788','bhumika@gmail.co.in','2023-06-29 00:10:33','Dine In','VERV56JK1QQ23S'),(4,'Nancy','8788767677','','2023-06-30 16:10:33','Dine In','5GK00DHDHWEHR'),(5,'Nancy','','nancy@gmail.com','2023-07-01 12:10:33','Dine In','54G4VJVKK54VVF'),(6,'Nano','','','2023-07-20 08:00:36','Dine In','54545G4I33FGG4P0'),(7,'Sharda','9899229988','','2023-07-28 18:09:36','Take Away','5G5GVKV84V3443F'),(8,'Sharda Gupta','339353536','','2023-07-29 15:19:36','Take Away','GVVERBTRT55GG'),(9,'Yogesh','9560604681','','2023-07-29 18:09:36','Dine In','P00AZMCNCF445G'),(10,'Yogesh2','','yog@gmail.com','2023-07-29 18:24:46','Take Away','LOLLQSSE881QIIK'),(11,'Himanshu kanda','8766721382','','2023-07-29 20:41:29','Dine In','SBBCG49N5NJ215G'),(12,'Jaya','','','2023-07-30 01:11:42','Dine In','G77UYSIIHK3RF556'),(13,'Raj Kumar','','raj.kumar@yahoo.com','2023-07-30 01:17:33','Take Away','658W6DKT96O2VY8F'),(14,'Himanshu Kanda','9718369108','fgg','2023-08-21 20:39:24','Online','2HC1L36CYB8QGLLT'),(15,'Bhoomika Gupta','','bhoomika.gupta@gmail.com','2023-09-03 13:35:45','Dine In','XCK5KKUKBWBKDC6R'),(16,'Yogesh','','','2023-09-03 23:17:50','Dine In','V8FUUIEOI386FFRM');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-04  0:18:18
