PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user(
id TEXT PRIMARY KEY NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL
);
CREATE TABLE task(
task_id TEXT PRIMARY KEY NOT NULL,
userid TEXT NOT NULL,
keywords TEXT NOT NULL,
delay_sec INT NOT NULL,
status INT NOT NULL
);
CREATE TABLE datas(
data_id TEXT PRIMARY KEY NOT NULL,
task_id TEXT NOT NULL,
keyword TEXT NOT NULL,
page INT NOT NULL,
title TEXT NOT NULL,
desc TEXT NOT NULL,
url TEXT NOT NULL
);
COMMIT;
