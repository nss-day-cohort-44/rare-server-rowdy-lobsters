# rare-server-rowdy-lobsters

## Getting started

## Routes


## Setting Up Database

### Pulling down the Server-Side Repo. 
 
> Note: This project is meant to run simultaneously with the Client-Side Repo found here: https://github.com/nss-day-cohort-44/rare-rowdy-lobsters 
 
> Depending on which repo you start with, you may already have the following directories set up.  
> This project requires Python  
 
### To Begin installing the Server-Side Repo, complete the following steps: 
 
1. Create a directory from which to deploy the application. 
	
```mkdir RARE ```
 
2. Within RARE, create two sub-directories, CLIENT and SERVER 

```mkdir CLIENT ```
	
```mkdir SERVER ```
 
3. Navigate into the SERVER sub-directory. 
 
```cd CLIENT ```
 
4. Enter the following commands: 
	
```git clone git@github.com:nss-day-cohort-44/rare-rowdy-lobsters.git .``` <-- note the single 	
dot preceded by a single space.  
 
5. Create a virtual environment: 
```pipenv shell```

6. Once the virtual environment is created, install the 3rd-party software. 

```pipenv install autopep8 watchgod ```

7. Enter in the following command to start your new data server written in Python: 

```watchgod request_handler.main ```

> If there are no errors in the code, you will see the following, terse output:  
 
```watchgod request_handler.main [09:34:37] watching "/Users/.../workspace/python-server" and reloading "request_handler.main" on changes…``` 

## Create/Seed the Database

We have provided an SQL script for you to run to build the database. There some INSERT statements they provided. You may create as many INSERT statements as needed to seed the database.
```
DROP TABLE IF EXISTS `Categories`;
DROP TABLE IF EXISTS `Tags`;
DROP TABLE IF EXISTS `Reactions`;
DROP TABLE IF EXISTS `PostReactions`;
DROP TABLE IF EXISTS `Posts`;
DROP TABLE IF EXISTS `PostTags`;
DROP TABLE IF EXISTS `Comments`;
DROP TABLE IF EXISTS `Subscriptions`;
DROP TABLE IF EXISTS `DemotionQueue`;
DROP TABLE IF EXISTS `AccountTypes`;
DROP TABLE IF EXISTS `Users`;

CREATE TABLE `AccountTypes` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `label` varchar
);
CREATE TABLE `Users` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `first_name` varchar,
  `last_name` varchar,
  `email` varchar,
  `bio` varchar,
  `username` varchar,
  `password` varchar,
  `profile_image_url` varchar,
  `created_on` date,
  `active` bit,
  `account_type_id` INTEGER,
  FOREIGN KEY(`account_type_id`) REFERENCES `AccountTypes`(`id`)
);
CREATE TABLE `DemotionQueue` (
  `action` varchar,
  `admin_id` INTEGER,
  `approver_one_id` INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);
CREATE TABLE `Subscriptions` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `follower_id` INTEGER,
  `author_id` INTEGER,
  `created_on` date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE `Posts` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER,
  `category_id` INTEGER,
  `title` varchar,
  `publication_date` date,
  `image_url` varchar,
  `content` varchar,
  `approved` bit
);
CREATE TABLE `Comments` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `post_id` INTEGER,
  `author_id` INTEGER,
  `content` varchar,
  `created_on` INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE `Reactions` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `label` varchar,
  `image_url` varchar
);
CREATE TABLE `PostReactions` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER,
  `reaction_id` INTEGER,
  `post_id` INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
CREATE TABLE `Tags` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `label` varchar
);
CREATE TABLE `PostTags` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `post_id` INTEGER,
  `tag_id` INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);
CREATE TABLE `Categories` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `label` varchar
);
INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Categories ('label') VALUES ('Opinion');
INSERT INTO Categories ('label') VALUES ('How-To');
INSERT INTO Categories ('label') VALUES ('Editorial');
INSERT INTO Categories ('label') VALUES ("Here's something dumb");
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Tags ('label') VALUES ('React');
INSERT INTO Tags ('label') VALUES ('Angular');
INSERT INTO Tags ('label') VALUES ('Vue');
INSERT INTO Tags ('label') VALUES ('Node');
INSERT INTO Tags ('label') VALUES ('C#');
INSERT INTO Tags ('label') VALUES ('.NET');
INSERT INTO Tags ('label') VALUES ('Python');
INSERT INTO Tags ('label') VALUES ('Data Science');
INSERT INTO Tags ('label') VALUES ('Django');
INSERT INTO Tags ('label') VALUES ('Flask');
INSERT INTO Tags ('label') VALUES ('Open Source');
INSERT INTO Tags ('label') VALUES ('Check this out!');
INSERT INTO Tags ('label') VALUES ('Beginners');
INSERT INTO Tags ('label') VALUES ('Weird');
INSERT INTO Tags ('label') VALUES ('Ugh');
INSERT INTO Tags ('label') VALUES ('Cool!');
INSERT INTO Tags ('label') VALUES ('Why tho?');
INSERT INTO Tags ('label') VALUES ('C#');
INSERT INTO Tags ('label') VALUES ('.NET');
INSERT INTO Tags ('label') VALUES ('Rust');
INSERT INTO Tags ('label') VALUES ('Ruby');
INSERT INTO Tags ('label') VALUES ('Rails');
INSERT INTO Tags ('label') VALUES ('Go');
INSERT INTO Tags ('label') VALUES ('C++');
INSERT INTO Tags ('label') VALUES ('History Lesson');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO Reactions ('label', 'image_url') VALUES ('heart', 'https://lh3.googleusercontent.com/proxy/BlwtWdiO1ucoroiKKuJN5CpiAUFA4tdHYRT_yXzxWLpNVTJS7UEVp1JV-lYshjAPeS7wd1pqXk6mpxY6rrSAPXD5NbBoE9hTf-1PpzofQbzNyH__1miggtO2IQKktovnAyPzjCW6T9mQG6JvgdHklZUaMd-YnIxeBPuP1lBw2E7fp9d6AR68');
INSERT INTO AccountTypes ('label') VALUES ('Admin');
INSERT INTO AccountTypes ('label') VALUES ('Author');


INSERT INTO Users values (null,'jas', 'kaset',  'jk@jk.com', null, 'jk', 'yes', null, null, null, '1');

INSERT INTO Users values (null,'david', 'williams',  'david@david.com', null,'dwillz', 'yes', null, null, null, '1');


SELECT * FROM Users
INSERT INTO AccountTypes ('label') VALUES ('Author');



INSERT INTO Posts ('user_id','category_id','title','publication_date','image_url','content','approved') VALUES ('1','1','new post','1/28/21',null,'story',null);

INSERT INTO Posts ('user_id','category_id','title','publication_date','image_url','content','approved') VALUES ('2','2','new post','1/29/21',null,'story',null);

INSERT INTO Users ('first_name','last_name','email','bio','username','password','profile_image_url',"created_on","active","account_type_id") VALUES ('Coach', 'Steve', 'coach@aol.com', null, 'coach@aol.com', 'YES', null, 1611955074741, null, 1);
INSERT INTO Users ('first_name','last_name','email','bio','username','password','profile_image_url',"created_on","active","account_type_id") VALUES ('Coach', 'Mo', 'mo@aol.com', null, 'mo@aol.com', 'YES', null, 1611955074767, null, 1);
INSERT INTO Users ('first_name','last_name','email','bio','username','password','profile_image_url',"created_on","active","account_type_id") VALUES ('Coach', 'Madi', 'madi@aol.com', null, 'mo@aol.com', 'YES', null, 1611955074768, null, 1);
```
