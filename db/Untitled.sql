ALTER TABLE `TM_Product` DROP FOREIGN KEY `fk_TM_Product_TM_ProductType_1`;
ALTER TABLE `TM_OrderDetail` DROP FOREIGN KEY `fk_TM_OrderDetail_TM_OrderMain_1`;

DROP TABLE `TM_User`;
DROP TABLE `TM_Address`;
DROP TABLE `TM_Group`;
DROP TABLE `TM_UserLog`;
DROP TABLE `TM_Product`;
DROP TABLE `TM_ProductType`;
DROP TABLE `TM_OrderMain`;
DROP TABLE `TM_OrderDetail`;
DROP TABLE `TM_Product_LinkInfo`;
DROP TABLE `TM_User_Status`;

CREATE TABLE `TM_User` (
`userId` int(11) NOT NULL AUTO_INCREMENT,
`userCode` varchar(30) CHARACTER SET utf8 NOT NULL,
`userName` varchar(100) NOT NULL,
`userPwd` varchar(255) NULL,
`isValid` varchar(1) NULL DEFAULT 'Y',
`groupId` int(11) NULL,
`addressId` int(11) NULL,
`phone` varchar(30) NULL,
`email` varchar(255) NULL,
`createDate` datetime NULL DEFAULT Current_Timestamp(),
`updateDate` datetime NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`userId`) 
)
DEFAULT CHARACTER SET = utf8;

CREATE TABLE `TM_Address` (
`addressId` int(11) NOT NULL AUTO_INCREMENT,
`userId` int(11) NULL,
`address` text NULL,
`isValid` varchar(1) NULL DEFAULT 'Y',
`createDate` datetime NULL DEFAULT Current_Timestamp(),
PRIMARY KEY (`addressId`) 
);

CREATE TABLE `TM_Group` (
`groupId` int(11) NOT NULL AUTO_INCREMENT,
`groudCode` varchar(30) NULL,
`isValid` varchar(1) NULL DEFAULT 'Y',
`createDate` datetime NULL DEFAULT Current_Timestamp(),
PRIMARY KEY (`groupId`) 
);

CREATE TABLE `TM_UserLog` (
`logId` int(11) NOT NULL AUTO_INCREMENT,
`logType` varchar(10) NULL,
`userId` int(11) NULL,
`createDate` datetime NULL DEFAULT Current_Timestamp(),
`remark` varchar(255) NULL,
PRIMARY KEY (`logId`) 
);

CREATE TABLE `TM_Product` (
`productId` int(11) NOT NULL AUTO_INCREMENT,
`productCode` varchar(30) NULL,
`productName` varchar(255) NULL,
`typeId` int(11) NULL COMMENT '产品分类',
`costPrice` decimal(10,2) NULL,
`salePrice` decimal(10,2) NULL,
`isValid` varchar(1) NULL DEFAULT 'Y',
`defaultImg` varchar(255) NULL COMMENT '默认显示图片路径',
`createDate` datetime NULL DEFAULT Current_Timestamp(),
`updateDate` datetime NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`productId`) 
);

CREATE TABLE `TM_ProductType` (
`typeId` int(11) NOT NULL AUTO_INCREMENT,
`typeCode` varchar(255) NULL,
`isValid` varchar(1) NULL,
`createDate` datetime NULL DEFAULT Current_Timestamp(),
`updateDate` datetime NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`typeId`) 
);

CREATE TABLE `TM_OrderMain` (
`orderId` int(11) NOT NULL AUTO_INCREMENT,
`orderCode` varchar(30) NOT NULL,
`sumCount` decimal(10,2) NULL,
`sumAmout` decimal(10,2) NULL,
`isValid` varchar(1) NULL,
`userId` int(11) NOT NULL,
`addressId` int(11) NULL,
`createDate` datetime NULL DEFAULT Current_Timestamp(),
`updateDate` datetime NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`orderId`) 
);

CREATE TABLE `TM_OrderDetail` (
`detailId` int(11) NOT NULL AUTO_INCREMENT,
`orderId` int(11) NOT NULL,
`productCode` varchar(30) NOT NULL,
`salePrice` decimal(10,2) NULL,
`saleCount` decimal(10,2) NULL,
`saleAmount` decimal(10,2) NULL,
`isValid` varchar(1) NULL DEFAULT 'Y',
`createDate` datetime NULL DEFAULT Current_Timestamp(),
`updateDate` datetime NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`detailId`) 
);

CREATE TABLE `TM_Product_LinkInfo` (
`linkInfoId` int(11) NOT NULL AUTO_INCREMENT,
`productCode` varchar(30) NULL,
`defaultImg` varchar(255) NULL COMMENT 'imgUrl',
`remark` varchar(255) NULL COMMENT '描述',
`isValid` varchar(1) NULL DEFAULT 'Y',
`createDate` datetime NULL DEFAULT Current_Timestamp(),
PRIMARY KEY (`linkInfoId`) 
);

CREATE TABLE `TM_User_Status` (
`userId` int(11) NOT NULL,
`isLogin` varchar(1) NULL DEFAULT 'Y',
`updateDate` datetime NULL DEFAULT Current_Timestamp(),
PRIMARY KEY (`userId`) 
);


ALTER TABLE `TM_Product` ADD CONSTRAINT `fk_TM_Product_TM_ProductType_1` FOREIGN KEY (`typeId`) REFERENCES `TM_ProductType` (`typeId`);
ALTER TABLE `TM_OrderDetail` ADD CONSTRAINT `fk_TM_OrderDetail_TM_OrderMain_1` FOREIGN KEY (`orderId`) REFERENCES `TM_OrderMain` (`orderId`);

