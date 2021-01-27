CREATE TABLE `Journal_Entries` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept` VARCHAR,
    `entry` VARCHAR,
    `date` DATE,
    `mood_id` INTEGER
);
CREATE TABLE `Moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `mood` VARCHAR,
    FOREIGN KEY(`id`) REFERENCES `Journal_Entries`(`mood_id`)
);
-- making mood data
INSERT INTO `Moods` VALUES (NULL, 'Happy');
INSERT INTO `Moods` VALUES (NULL, 'Focused');
INSERT INTO `Moods` VALUES (NULL, 'Confused');
INSERT INTO `Moods` VALUES (NULL, 'Worried');
INSERT INTO `Moods` VALUES (NULL, 'Frustrated');
-- making journal data
INSERT INTO `Journal_Entries` VALUES (NULL,'React','React is alright and very versitile ','05/23/20',1);
INSERT INTO `Journal_Entries` VALUES (NULL,'Python','Python is amazing!','02/02/20',4);
INSERT INTO `Journal_Entries` VALUES (NULL,'SQL','Is hard to understand but practice makes perfect','08/19/27',2);
INSERT INTO `Journal_Entries` VALUES (NULL,'following the ball','helps you to understand the code!','01/30/45',1);
INSERT INTO `Journal_Entries` VALUES (NULL,'clients and servers','better understanding of how the internet works!','03/11/70',1);