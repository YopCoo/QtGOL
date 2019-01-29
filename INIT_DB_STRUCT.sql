BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `PATTERN_NAME` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`NAME`	TEXT NOT NULL,
	`CATEGORY`	INTEGER NOT NULL,
	FOREIGN KEY(`CATEGORY`) REFERENCES `PATTERN_CATEGORY`(`ID`)
);
INSERT INTO `PATTERN_NAME` VALUES (1,'DOT',1);
INSERT INTO `PATTERN_NAME` VALUES (2,'BLOCK',1);
INSERT INTO `PATTERN_NAME` VALUES (3,'BLINK',2);
INSERT INTO `PATTERN_NAME` VALUES (4,'GLIDER',3);
CREATE TABLE IF NOT EXISTS `PATTERN_CELL` (
	`NAME`	INTEGER NOT NULL,
	`CX`	INTEGER NOT NULL,
	`CY`	INTEGER NOT NULL,
	`STATE`	INTEGER NOT NULL,
	PRIMARY KEY(`NAME`,`CX`,`CY`),
	FOREIGN KEY(`NAME`) REFERENCES `PATTERN_NAME`(`ID`)
);
INSERT INTO `PATTERN_CELL` VALUES (1,0,0,1);
INSERT INTO `PATTERN_CELL` VALUES (2,0,0,1);
INSERT INTO `PATTERN_CELL` VALUES (2,1,0,1);
INSERT INTO `PATTERN_CELL` VALUES (2,0,1,1);
INSERT INTO `PATTERN_CELL` VALUES (2,1,1,1);
INSERT INTO `PATTERN_CELL` VALUES (3,0,0,1);
INSERT INTO `PATTERN_CELL` VALUES (3,-1,0,1);
INSERT INTO `PATTERN_CELL` VALUES (3,1,0,1);
INSERT INTO `PATTERN_CELL` VALUES (4,0,0,1);
INSERT INTO `PATTERN_CELL` VALUES (4,0,-1,1);
INSERT INTO `PATTERN_CELL` VALUES (4,0,-2,1);
INSERT INTO `PATTERN_CELL` VALUES (4,-1,0,1);
INSERT INTO `PATTERN_CELL` VALUES (4,-2,-1,1);
CREATE TABLE IF NOT EXISTS `PATTERN_CATEGORY` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`CATEGORY`	TEXT NOT NULL
);
INSERT INTO `PATTERN_CATEGORY` VALUES (1,'STATIC');
INSERT INTO `PATTERN_CATEGORY` VALUES (2,'PERIODIC');
INSERT INTO `PATTERN_CATEGORY` VALUES (3,'MOVING');
CREATE TABLE IF NOT EXISTS `CONFIG` (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`XCELL`	INTEGER NOT NULL,
	`YCELL`	INTEGER NOT NULL,
	`SIZECELL`	INTEGER NOT NULL,
	`DENSITY`	REAL NOT NULL,
	`SPEED`	INTEGER NOT NULL,
	`INACTIVE_COLOR_R`	INTEGER NOT NULL,
	`INACTIVE_COLOR_G`	INTEGER NOT NULL,
	`INACTIVE_COLOR_B`	INTEGER NOT NULL,
	`ACTIVE_COLOR_R`	INTEGER NOT NULL,
	`ACTIVE_COLOR_G`	INTEGER NOT NULL,
	`ACTIVE_COLOR_B`	INTEGER NOT NULL,
	`NEW_COLOR_R`	INTEGER NOT NULL,
	`NEW_COLOR_G`	INTEGER NOT NULL,
	`NEW_COLOR_B`	INTEGER NOT NULL
);
INSERT INTO `CONFIG` VALUES (1,30,30,10,0.3,150,128,128,128,255,255,0,255,153,51);
COMMIT;