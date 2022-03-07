CREATE DATABASE  IF NOT EXISTS `tc_store_new` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `tc_store_new`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tc_store_new
-- ------------------------------------------------------
-- Server version	5.7.37

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
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `product_id` bigint(20) DEFAULT NULL,
  `transaction_id` varchar(50) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `user_id` (`user_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `order_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_ID` bigint(20) NOT NULL,
  `product_name` text,
  `product_price` bigint(20) DEFAULT NULL,
  `picture_URL` text,
  `product_description` text,
  PRIMARY KEY (`product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'綜合巧克力禮盒(小盒)',650,'https://cdn.store-assets.com/s/632442/i/37826436.jpg?width=480','想嘗試不同風味的黑巧克力嗎這款綜合口味提供給您有更多的新選擇65%、75%、85%黑巧克力一次滿足，送禮自用兩相宜。(60 g/12 片/盒)'),(2,'柴燒黑糖巧克力',350,'https://cdn.store-assets.com/s/632442/i/30824617.jpg?width=480','柴燒黑糖巧克力黑糖片刻的溫暖，傳遞對土地友善種植無毒甘蔗的熱情，搭上屏東在地黑金巧克力，孕育出獨特的風味，柴燒黑糖口感濃郁果酸豐富的層次感，黑糖香氣與巧克力果香完美順口結合，製程可可原豆研磨時期道手續總共72小時完工、從產地到餐桌完全零距離，天然健康無負擔，回甘的滋味更是念念不忘。從屏東的可可果實到巧克力工序13道'),(3,'100%無糖巧克力磚',350,'https://cdn.store-assets.com/s/632442/i/20596809.jpg?width=480','嚴選屏東可可豆研磨72小時，完全保留可可豆本身的可可油脂，天然養生，果香四溢，微微的天然果酸會回甘。（100%可可豆+0%台糖=100%無糖巧克力磚）非常適合喜歡無加糖的養生族群粉絲們唷?微酸微苦，入口後慢慢回甘的滋味，千萬別錯過囉'),(4,'95%巧克力磚',350,'https://cdn.store-assets.com/s/632442/i/20595475.jpg?width=480','嚴選屏東可可豆研磨72小時，完全保留可可豆本身的可可油脂，天然養生，果香四溢，微微的天然果酸會回甘。（95%可可豆+5%台糖=95%巧克力磚）微微糖微苦的感覺，適合喜歡不甜的您唷'),(5,'85%巧克力磚',350,'https://cdn.store-assets.com/s/632442/i/20595455.jpg?width=480','嚴選屏東可可豆研磨72小時，完全保留可可豆本身的可可油脂，天然養生，果香四溢，微微的天然果酸會回甘。（85%可可豆+15%台糖=85%巧克力磚）微糖甜度適中，非常平衡的口感，人氣首選之一唷'),(6,'75%巧克力磚',350,'https://cdn.store-assets.com/s/632442/i/20595383.jpg?width=480','嚴選屏東可可豆研磨72小時，完全保留可可豆本身的可可油脂，天然養生，果香四溢，微微的天然果酸會回甘。（75%可可豆+25%台糖=75%巧克力磚）適合喜歡少糖的感覺粉絲們唷大眾口味的最佳選擇?'),(7,'65%巧克力磚',350,'https://cdn.store-assets.com/s/632442/i/20595215.jpg?width=480','嚴選屏東可可豆研磨72小時，完全保留可可豆本身的可可油脂，天然養生，果香四溢，微微的天然果酸會回甘。（65%可可豆+35%台糖=65%巧克力磚）可可香氣濃郁，喜歡甜甜的您天然的葡萄乾的香氣，入口回甘，甜甜的幸福感'),(8,'紅藜巧克力BAR',390,'https://cdn.store-assets.com/s/632442/i/20281474.png?width=480','紅色質感外觀體面，打開驚喜連連，當紅藜米香碰上屏東黑金巧克力，爆出味蕾新滋味。(50g/盒)'),(9,'牛奶巧克力BAR',390,'https://cdn.store-assets.com/s/632442/i/20281396.png?width=480','奶香溫醇的口感，散發迷人的甜美，是牛奶控者的喜愛。(50g/盒)'),(10,'洛神花巧克力BAR',390,'https://cdn.store-assets.com/s/632442/i/20281239.png?width=480','當洛神花果干遇見黑金巧克力，蹦出讓你想像不到的美味，微果酸襯托出在地黑金巧克力的天然風味。(50g/盒)'),(11,'杏仁巧克力豆',380,'https://cdn.store-assets.com/s/632442/i/20213537.png?width=480','嚴選杏仁堅果裹了一層焦糖再披覆上三層的65%黑巧克力，杏仁堅果與巧克力的巧妙結合，最後在灑上可可粉，完全無違和感，享受健康堅果又多了層次的口感，兼具幸福好滋味，不膩口的養生點心。(100g/瓶)'),(12,'天然可可豆茶',300,'https://cdn.store-assets.com/s/632442/i/20212594.jpg?width=480','你絕對沒有喝過透明的巧克力吧!沒錯它就是做巧克力的重要原料，天然養生零添加物，完全無糖，有可可豆的輕烘培香氣，茶香回韻的微果酸令人著迷。(10入/包)'),(13,'95%黑巧克力冰淇淋',120,'https://cdn.store-assets.com/s/632442/i/20212428.jpg?width=480','使用含量95%在地巧克力作為原料，保留了巧克力原本的果酸，讓顧客吃到不同於市售巧克力冰淇淋只有苦與甜的口感，多了果酸讓享受冰涼口感之外又添加了層次口感。(120ml/杯)'),(14,'烘培可可豆',390,'https://cdn.store-assets.com/s/632442/i/20199157.jpg?width=480','低溫烘培後可可豆可直接食用，保留了最原始的風味，經由天然發酵可可豆，無任何香精香料，口感有如堅果一般，微微的果酸及可可香氣讓您齒頰留香。（150g/包）'),(15,'杏仁可可瓦片',380,'https://cdn.store-assets.com/s/632442/i/20199099.jpg?width=480','嚴選杏仁片灑在濃醇的65%黑巧克力上，巧妙融合濃郁巧克力可可香，全程純手工製作，口感紮實獨特，香脆可口，齒頰留香，完全不膩口。(180g/盒)'),(16,'海鹽巧克力BAR',390,'https://cdn.store-assets.com/s/632442/i/20280280.png?width=480','嚴選天然和曬製成珍貴的鹽花，含豐富礦物質，每一粒鹽都飽含天然氣息，風味溫醇，結合屏東黑金巧克力成了舌尖跳舞的鑽石。50g/盒'),(17,'花生巧克力BAR',390,'https://cdn.store-assets.com/s/632442/i/20280325.png?width=480','(2019-AOC英國皇家學院巧克力大賽-銀獎之座)嚴選來自屏東內埔客庄的手工鹽炒花生，每一粒花生味甘氣香顆顆飽滿順口，配上在地黑金巧克力突顯客家刻苦耐勞的精神。(50g/盒)'),(18,'抹茶拿鐵生巧克力',490,'https://cdn.store-assets.com/s/632442/i/20123932.jpg?width=480','抹茶口味愛好者千萬別錯過唷!香醇濃郁，入口即化的口感讓您享受美好生活，甜而不膩的滋味是您最佳選擇。(100g/盒)'),(19,'經典生巧克力',490,'https://cdn.store-assets.com/s/632442/i/20280445.jpg?width=480','生巧克力為日本人發明，『生』意指『新鮮』通常含鮮奶油質地很軟，表面無巧克力硬殼，常見有可可粉。口感柔軟，堅持嚴選在地的可可，天然絕無防腐劑添加物，濃郁純香，獨家風味。(100g/盒)'),(20,'綜合巧克力禮盒(大盒)',1000,'https://cdn.store-assets.com/s/632442/i/20113307.jpg?width=480','想嘗試不同風味的黑巧克力嗎這款綜合口味提供給您有更多的新選擇65%、75%、85%、95%黑巧克力一次滿足，送禮自用兩相宜。(100g/20片/盒)'),(21,'65%巧克力禮盒',800,'https://cdn.store-assets.com/s/632442/i/20058560.jpg?width=480','(2019-ICA亞太區巧克力大賽銅牌-65%黑巧克力)以屏東在地種植的可可所生產出來的巧克力，有別於一般市售巧克力，使用65%屏東可可原豆及35%蔗糖精細研磨48小時，沒有經過脫脂的程序讓巧克力的風味更獨特!微甜帶點微酸就似初戀的味道~TC巧舖用心製作的巧克力，讓消費者都能品嚐到兼俱養身與美味的巧克力!(100g/20片/盒)'),(22,'75%巧克力禮盒',999,'https://cdn.store-assets.com/s/632442/i/20058559.jpg?width=480','以屏東在地種植的可可所生產出來的巧克力，使用75%屏東可可原豆及25%蔗糖精細研磨48小時讓巧克力的風味更獨特!微甜帶點微酸就似初戀的味道~(100g/20片/799盒)'),(23,'85%巧克力禮盒',1000,'https://cdn.store-assets.com/s/632442/i/20058553.jpg?width=480','使用85%屏東可可原豆及15%蔗糖精細研磨48小時，沒有經過脫脂的程序讓巧克力的風味更獨特!有別於一般市售巧克力，濃郁果香極微果酸，(100g/20片/盒)'),(24,'95%巧克力禮盒',1000,'https://cdn.store-assets.com/s/632442/i/20058552.jpg?width=480&format=webp','使用95%屏東可可原豆及5%蔗糖精細研磨48小時，巧克力入口後苦中帶酸，可可香氣撲鼻而來，養生主義最佳首選。(100g/20片/盒)'),(25,'草莓季限定款巧克力禮盒',499,'https://img.ihappyday.tw/2021/01/1611083854-bf188049f672ac77e6ea0ab141f7478b-768x512.jpg','以金牌可可豆搭配新鮮草莓，採用粉紅夢幻紛色系，不僅色彩繽紛，每一口都可以感受草莓的鮮甜與金牌巧克力豆的豐富果香');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(40) NOT NULL,
  `password` text,
  `name` text,
  `address` text,
  `created_on` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'aaa@yahoo.com.tw','sha256$bU4FNDZ9lgR34BUX$167095dde8e94242ff2a6c8aca81e46bfc52e1fe0d18f06a2586d332d1ea381b','Ken','台北市信義區','2022-02-26 15:05:51'),(2,'eee@yahoo.com.tw','sha256$4Uy98QcdnIabHSeC$997199140f853003db689c461729d8a4ffd569c4b404d404537f9c7878357a2d','Kendy','台北市信義區','2022-03-02 09:32:29'),(3,'bbb@yahoo.com.tw','sha256$bGSYxDAZXqMGNDMg$e79d5eba375285d1b7b3b82339da17a931ad302547c06eb3ecbc7f1770e55b3f','Ian','台北市信義區','2022-03-02 09:39:21');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-04  2:20:41
