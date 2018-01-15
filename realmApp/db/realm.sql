/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 50710
 Source Host           : localhost:3306
 Source Schema         : realm

 Target Server Type    : MySQL
 Target Server Version : 50710
 File Encoding         : 65001

 Date: 15/01/2018 22:31:18
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for TM_Address
-- ----------------------------
DROP TABLE IF EXISTS `TM_Address`;
CREATE TABLE `TM_Address` (
  `addressId` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) DEFAULT NULL,
  `address` text,
  `isValid` varchar(1) DEFAULT 'Y',
  `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`addressId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for TM_Group
-- ----------------------------
DROP TABLE IF EXISTS `TM_Group`;
CREATE TABLE `TM_Group` (
  `groupId` int(11) NOT NULL AUTO_INCREMENT,
  `groudCode` varchar(30) DEFAULT NULL,
  `isValid` varchar(1) DEFAULT 'Y',
  `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`groupId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for TM_Level
-- ----------------------------
DROP TABLE IF EXISTS `TM_Level`;
CREATE TABLE `TM_Level` (
  `levelId` int(11) NOT NULL AUTO_INCREMENT COMMENT '层次',
  `levelName` varchar(255) DEFAULT NULL COMMENT '单层、双层',
  `isValid` varchar(1) DEFAULT 'Y',
  PRIMARY KEY (`levelId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of TM_Level
-- ----------------------------
BEGIN;
INSERT INTO `TM_Level` VALUES (1, '单层', 'Y');
INSERT INTO `TM_Level` VALUES (2, '双层', 'Y');
COMMIT;

-- ----------------------------
-- Table structure for TM_Model
-- ----------------------------
DROP TABLE IF EXISTS `TM_Model`;
CREATE TABLE `TM_Model` (
  `modelId` int(11) NOT NULL AUTO_INCREMENT,
  `modelName` varchar(255) DEFAULT NULL,
  `isValid` varchar(1) DEFAULT 'Y',
  PRIMARY KEY (`modelId`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of TM_Model
-- ----------------------------
BEGIN;
INSERT INTO `TM_Model` VALUES (1, 'S', 'Y');
INSERT INTO `TM_Model` VALUES (2, 'M', 'Y');
INSERT INTO `TM_Model` VALUES (3, 'L', 'Y');
INSERT INTO `TM_Model` VALUES (4, 'XL', 'Y');
INSERT INTO `TM_Model` VALUES (5, 'XXL', 'Y');
INSERT INTO `TM_Model` VALUES (6, 'XXXL', 'Y');
COMMIT;

-- ----------------------------
-- Table structure for TM_OrderDetail
-- ----------------------------
DROP TABLE IF EXISTS `TM_OrderDetail`;
CREATE TABLE `TM_OrderDetail` (
  `detailId` int(11) NOT NULL AUTO_INCREMENT,
  `orderId` int(11) NOT NULL,
  `productCode` varchar(30) NOT NULL,
  `salePrice` decimal(10,2) DEFAULT NULL,
  `saleCount` decimal(10,2) DEFAULT NULL,
  `saleAmount` decimal(10,2) DEFAULT NULL,
  `isValid` varchar(1) DEFAULT 'Y',
  `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `updateDate` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`detailId`),
  KEY `fk_TM_OrderDetail_TM_OrderMain_1` (`orderId`),
  CONSTRAINT `fk_TM_OrderDetail_TM_OrderMain_1` FOREIGN KEY (`orderId`) REFERENCES `TM_OrderMain` (`orderId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for TM_OrderMain
-- ----------------------------
DROP TABLE IF EXISTS `TM_OrderMain`;
CREATE TABLE `TM_OrderMain` (
  `orderId` int(11) NOT NULL AUTO_INCREMENT,
  `orderCode` varchar(30) NOT NULL,
  `sumCount` decimal(10,2) DEFAULT NULL,
  `sumAmout` decimal(10,2) DEFAULT NULL,
  `isValid` varchar(1) DEFAULT NULL,
  `userId` int(11) NOT NULL,
  `addressId` int(11) DEFAULT NULL,
  `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `updateDate` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`orderId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for TM_Product
-- ----------------------------
DROP TABLE IF EXISTS `TM_Product`;
CREATE TABLE `TM_Product` (
  `productId` int(11) NOT NULL AUTO_INCREMENT,
  `productCode` varchar(30) NOT NULL COMMENT '产品代码',
  `productName` varchar(255) NOT NULL COMMENT '产品名称',
  `typeCode` varchar(255) NOT NULL COMMENT '产品分类',
  `costPrice` decimal(10,2) DEFAULT NULL COMMENT '成本价(订单产生时)',
  `salePrice` decimal(10,2) DEFAULT NULL COMMENT '销售价',
  `isValid` varchar(1) DEFAULT 'Y',
  `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `updateDate` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`productId`),
  KEY `fk_1` (`typeCode`),
  CONSTRAINT `fk_1` FOREIGN KEY (`typeCode`) REFERENCES `TM_ProductType` (`typeCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for TM_Product_LinkInfo
-- ----------------------------
DROP TABLE IF EXISTS `TM_Product_LinkInfo`;
CREATE TABLE `TM_Product_LinkInfo` (
  `linkInfoId` int(11) NOT NULL AUTO_INCREMENT,
  `productCode` varchar(30) DEFAULT NULL,
  `defaultImg` varchar(255) DEFAULT NULL COMMENT 'imgUrl',
  `remark` varchar(255) DEFAULT NULL COMMENT '描述',
  `isValid` varchar(1) DEFAULT 'Y',
  `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`linkInfoId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for TM_ProductType
-- ----------------------------
DROP TABLE IF EXISTS `TM_ProductType`;
CREATE TABLE `TM_ProductType` (
  `typeId` int(11) NOT NULL AUTO_INCREMENT,
  `typeCode` varchar(255) NOT NULL,
  `version` varchar(255) DEFAULT NULL COMMENT '版本名称',
  `projectId` int(11) DEFAULT NULL COMMENT '项目',
  `styleId` int(11) DEFAULT NULL COMMENT '款式',
  `modelId` int(11) DEFAULT NULL COMMENT '型号',
  `levelId` int(11) DEFAULT NULL COMMENT '层次',
  `isValid` varchar(1) DEFAULT NULL,
  `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `updateDate` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`typeId`),
  KEY `typeCode` (`typeCode`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of TM_ProductType
-- ----------------------------
BEGIN;
INSERT INTO `TM_ProductType` VALUES (1, '010101010001', 'V1.0', 1, 1, 1, 1, 'Y', '2018-01-15 22:26:03', NULL);
COMMIT;

-- ----------------------------
-- Table structure for TM_Project
-- ----------------------------
DROP TABLE IF EXISTS `TM_Project`;
CREATE TABLE `TM_Project` (
  `projectId` int(11) NOT NULL AUTO_INCREMENT,
  `projectName` varchar(255) DEFAULT NULL,
  `isValid` varchar(1) DEFAULT 'Y',
  PRIMARY KEY (`projectId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of TM_Project
-- ----------------------------
BEGIN;
INSERT INTO `TM_Project` VALUES (1, '布', 'Y');
INSERT INTO `TM_Project` VALUES (2, '纱', 'Y');
INSERT INTO `TM_Project` VALUES (3, '幔', 'Y');
COMMIT;

-- ----------------------------
-- Table structure for TM_Style
-- ----------------------------
DROP TABLE IF EXISTS `TM_Style`;
CREATE TABLE `TM_Style` (
  `styleId` int(11) NOT NULL AUTO_INCREMENT,
  `styleName` varchar(255) DEFAULT NULL COMMENT '款式(四叉勾、打孔 、、)',
  `isValid` varchar(1) DEFAULT 'Y',
  PRIMARY KEY (`styleId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of TM_Style
-- ----------------------------
BEGIN;
INSERT INTO `TM_Style` VALUES (1, '四叉勾', 'Y');
INSERT INTO `TM_Style` VALUES (2, '打孔', 'Y');
INSERT INTO `TM_Style` VALUES (3, '幔头', 'Y');
INSERT INTO `TM_Style` VALUES (4, '其他', 'Y');
COMMIT;

-- ----------------------------
-- Table structure for TM_User
-- ----------------------------
DROP TABLE IF EXISTS `TM_User`;
CREATE TABLE `TM_User` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `userCode` varchar(30) NOT NULL,
  `userName` varchar(100) NOT NULL,
  `userPwd` varchar(255) DEFAULT NULL,
  `isValid` varchar(1) DEFAULT 'Y',
  `groupId` int(11) DEFAULT NULL,
  `addressId` int(11) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `updateDate` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for TM_User_Status
-- ----------------------------
DROP TABLE IF EXISTS `TM_User_Status`;
CREATE TABLE `TM_User_Status` (
  `userId` int(11) NOT NULL,
  `isLogin` varchar(1) DEFAULT 'Y',
  `updateDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for TM_UserLog
-- ----------------------------
DROP TABLE IF EXISTS `TM_UserLog`;
CREATE TABLE `TM_UserLog` (
  `logId` int(11) NOT NULL AUTO_INCREMENT,
  `logType` varchar(10) DEFAULT NULL,
  `userId` int(11) DEFAULT NULL,
  `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`logId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
