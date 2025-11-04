/*
SQLyog Community v13.3.0 (64 bit)
MySQL - 10.4.32-MariaDB : Database - chatbot
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`chatbot` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `chatbot`;

/*Data for the table `auth_group` */

/*Data for the table `auth_group_permissions` */

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add course',7,'add_course'),
(26,'Can change course',7,'change_course'),
(27,'Can delete course',7,'delete_course'),
(28,'Can view course',7,'view_course'),
(29,'Can add department',8,'add_department'),
(30,'Can change department',8,'change_department'),
(31,'Can delete department',8,'delete_department'),
(32,'Can view department',8,'view_department'),
(33,'Can add facility',9,'add_facility'),
(34,'Can change facility',9,'change_facility'),
(35,'Can delete facility',9,'delete_facility'),
(36,'Can view facility',9,'view_facility'),
(37,'Can add login',10,'add_login'),
(38,'Can change login',10,'change_login'),
(39,'Can delete login',10,'delete_login'),
(40,'Can view login',10,'view_login'),
(41,'Can add schedule',11,'add_schedule'),
(42,'Can change schedule',11,'change_schedule'),
(43,'Can delete schedule',11,'delete_schedule'),
(44,'Can view schedule',11,'view_schedule'),
(45,'Can add support',12,'add_support'),
(46,'Can change support',12,'change_support'),
(47,'Can delete support',12,'delete_support'),
(48,'Can view support',12,'view_support'),
(49,'Can add timetable',13,'add_timetable'),
(50,'Can change timetable',13,'change_timetable'),
(51,'Can delete timetable',13,'delete_timetable'),
(52,'Can view timetable',13,'view_timetable'),
(53,'Can add subject',14,'add_subject'),
(54,'Can change subject',14,'change_subject'),
(55,'Can delete subject',14,'delete_subject'),
(56,'Can view subject',14,'view_subject'),
(57,'Can add student',15,'add_student'),
(58,'Can change student',15,'change_student'),
(59,'Can delete student',15,'delete_student'),
(60,'Can view student',15,'view_student'),
(61,'Can add staff',16,'add_staff'),
(62,'Can change staff',16,'change_staff'),
(63,'Can delete staff',16,'delete_staff'),
(64,'Can view staff',16,'view_staff'),
(65,'Can add gallary',17,'add_gallary'),
(66,'Can change gallary',17,'change_gallary'),
(67,'Can delete gallary',17,'delete_gallary'),
(68,'Can view gallary',17,'view_gallary'),
(69,'Can add feedback',18,'add_feedback'),
(70,'Can change feedback',18,'change_feedback'),
(71,'Can delete feedback',18,'delete_feedback'),
(72,'Can view feedback',18,'view_feedback'),
(73,'Can add events',19,'add_events'),
(74,'Can change events',19,'change_events'),
(75,'Can delete events',19,'delete_events'),
(76,'Can view events',19,'view_events'),
(77,'Can add complaints',20,'add_complaints'),
(78,'Can change complaints',20,'change_complaints'),
(79,'Can delete complaints',20,'delete_complaints'),
(80,'Can view complaints',20,'view_complaints'),
(81,'Can add allocate',21,'add_allocate'),
(82,'Can change allocate',21,'change_allocate'),
(83,'Can delete allocate',21,'delete_allocate'),
(84,'Can view allocate',21,'view_allocate'),
(85,'Can add feedbackpublic',22,'add_feedbackpublic'),
(86,'Can change feedbackpublic',22,'change_feedbackpublic'),
(87,'Can delete feedbackpublic',22,'delete_feedbackpublic'),
(88,'Can view feedbackpublic',22,'view_feedbackpublic');

/*Data for the table `auth_user` */

/*Data for the table `auth_user_groups` */

/*Data for the table `auth_user_user_permissions` */

/*Data for the table `django_admin_log` */

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(21,'myapp','allocate'),
(20,'myapp','complaints'),
(7,'myapp','course'),
(8,'myapp','department'),
(19,'myapp','events'),
(9,'myapp','facility'),
(18,'myapp','feedback'),
(22,'myapp','feedbackpublic'),
(17,'myapp','gallary'),
(10,'myapp','login'),
(11,'myapp','schedule'),
(16,'myapp','staff'),
(15,'myapp','student'),
(14,'myapp','subject'),
(12,'myapp','support'),
(13,'myapp','timetable'),
(6,'sessions','session');

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-10-04 22:30:01.069842'),
(2,'auth','0001_initial','2024-10-04 22:30:01.244794'),
(3,'admin','0001_initial','2024-10-04 22:30:01.593541'),
(4,'admin','0002_logentry_remove_auto_add','2024-10-04 22:30:01.685274'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-10-04 22:30:01.690009'),
(6,'contenttypes','0002_remove_content_type_name','2024-10-04 22:30:01.767988'),
(7,'auth','0002_alter_permission_name_max_length','2024-10-04 22:30:01.815313'),
(8,'auth','0003_alter_user_email_max_length','2024-10-04 22:30:01.836927'),
(9,'auth','0004_alter_user_username_opts','2024-10-04 22:30:01.846242'),
(10,'auth','0005_alter_user_last_login_null','2024-10-04 22:30:01.894427'),
(11,'auth','0006_require_contenttypes_0002','2024-10-04 22:30:01.899075'),
(12,'auth','0007_alter_validators_add_error_messages','2024-10-04 22:30:01.900198'),
(13,'auth','0008_alter_user_username_max_length','2024-10-04 22:30:01.922097'),
(14,'auth','0009_alter_user_last_name_max_length','2024-10-04 22:30:01.925105'),
(15,'auth','0010_alter_group_name_max_length','2024-10-04 22:30:01.941102'),
(16,'auth','0011_update_proxy_permissions','2024-10-04 22:30:01.956740'),
(17,'myapp','0001_initial','2024-10-04 22:30:02.211813'),
(18,'sessions','0001_initial','2024-10-04 22:30:02.558476'),
(19,'myapp','0002_support_discription','2024-11-13 02:09:11.666939'),
(20,'myapp','0003_feedback_email','2024-11-15 00:54:15.605463'),
(21,'myapp','0004_auto_20241115_0648','2024-11-15 01:18:52.846210');

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('91lb62uddwcg6ldd1j9me39gdw6zain3','ZDc0OGExZjUxNjlmOWIwYTdjZTBhNzU2ODA0NDViZTA3MjMwZWU3Njp7ImxpZCI6Mn0=','2024-11-08 23:51:19.124030'),
('jsw7jewg6pls7wtc5ykjn7yl3tn6p8bi','MGQzZGU3Mjk1ZjBhNGZjNjk5NTQ3NmFkNTNmN2IzNzJhMTRmMDQ4NDp7ImxpZCI6NH0=','2024-12-03 01:07:05.351336'),
('kx9h1cfg1sj3ua0s7fmhznnvz1ut6gf7','NTIxZWU2OTlmZTU0MmU4NTMyMjQ0NzcwZTg0ZTg5OGJmZjQ4YzFlMjp7ImxpZCI6M30=','2024-10-25 00:25:08.026943'),
('t622fdord2ug7vrys3i0wyftegndscun','MGQzZGU3Mjk1ZjBhNGZjNjk5NTQ3NmFkNTNmN2IzNzJhMTRmMDQ4NDp7ImxpZCI6NH0=','2025-01-07 05:53:08.418375'),
('xps2k6y2l2vtr11laixj5lda7t1w0g2p','MjE4YWZiZGExNGQwMmU5YmUyNThlNTIwZDkyNDBiODUyYzg5OWNhNTp7ImxpZCI6MX0=','2025-01-05 09:59:50.364806');

/*Data for the table `myapp_allocate` */

insert  into `myapp_allocate`(`id`,`status`,`date`,`STAFF_id`,`SUBJECT_id`) values 
(1,'','2024-11-13',3,3),
(4,'allocate','2024-11-18',3,4),
(5,'allocate','2024-11-19',1,3);

/*Data for the table `myapp_complaints` */

insert  into `myapp_complaints`(`id`,`date`,`complaint`,`reply`,`status`,`STAFF_id`) values 
(2,'2024-10-26','','bgvghcfc','replied',1),
(3,'2024-10-26','','','pending',1),
(4,'2024-10-26','iupoyutyty','','pending',1),
(5,'2024-11-19','retrtterwejyutlytryet','','pending',1);

/*Data for the table `myapp_course` */

insert  into `myapp_course`(`id`,`coursename`,`semester`,`DEPARTMENT_id`) values 
(3,'BACHELOR OF COMPUTER APPLICATION (BCA)','06',3),
(4,'','6',5),
(7,'BACHELOR OF COMPUTER APPLICATION','06',3),
(9,'34cvnnmngv','3',3);

/*Data for the table `myapp_department` */

insert  into `myapp_department`(`id`,`departmentname`) values 
(3,'COMPUTER SCIENCE'),
(4,'SOCIOLOGY'),
(5,'ENGLISH'),
(6,'COMMERCE AND MANAGEMENT STUDIES'),
(7,'PSYCOLOGY'),
(8,'LANGUAGE'),
(9,'PHYSICAL EDUCATION');

/*Data for the table `myapp_events` */

insert  into `myapp_events`(`id`,`date`,`type`,`venue`,`time`,`STAFF_id`) values 
(1,'2024-10-01','gfdr','xdcvbn','11:33',1),
(2,'2024-10-16','jjvkl, ','nbvcvbn','03:03',3),
(3,'2024-10-30','gfgkugj','bvjghfghj','03:03',1),
(4,'2024-11-20','urtyihuiit6yf','gfsfdhghv','17:55',1);

/*Data for the table `myapp_facility` */

insert  into `myapp_facility`(`id`,`name`,`image`) values 
(1,'washroom',''),
(3,'LAB','/media/20241115-045047.jpg'),
(4,'librsary','/media/20241115-045122.jpg'),
(5,'librsary','/media/20241115-045239.jpg'),
(6,'library','/media/20241115-045548.jpg'),
(7,'fdhgjyhj','/media/20241118-065225.jpg'),
(8,'lil','/media/20241119-060732.jpg');

/*Data for the table `myapp_feedback` */

insert  into `myapp_feedback`(`id`,`date`,`feedback`,`STAFF_id`) values 
(2,'2024-10-26','heghdiwuegfwefbqwjbf',1),
(3,'2024-10-26','guiudvvhjkh',1),
(4,'2024-10-26','ihfghuiou',1);

/*Data for the table `myapp_feedbackpublic` */

insert  into `myapp_feedbackpublic`(`id`,`date`,`feedback`,`Email`) values 
(1,'2024-11-15','6eyr35y35hhgfhgfdshts','shamna@gmail.com');

/*Data for the table `myapp_gallary` */

insert  into `myapp_gallary`(`id`,`image`,`date`,`STAFF_id`) values 
(2,'/media/20241113-042204.jpg','2024-11-13',3),
(3,'/media/20241113-042315.jpg','2024-11-13',3),
(4,'/media/20241119-061643.jpg','2024-11-19',1);

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin','1234','admin'),
(2,'abdullatheea@gmail.com','7249','staff'),
(4,'akhila@gmail.com','5114','staff'),
(5,'admin','1222','admin'),
(6,'admin','1222','admin'),
(7,'sakkeena.com','7976','staff'),
(8,'trfgyhunjk@gmailcom','6413','staff');

/*Data for the table `myapp_schedule` */

insert  into `myapp_schedule`(`id`,`programname`,`date`,`time`,`Venue`) values 
(3,'ONAM','2024-11-06','04:03','manjeri'),
(4,'union day','2024-10-08','04:04','ground');

/*Data for the table `myapp_staff` */

insert  into `myapp_staff`(`id`,`name`,`place`,`pin`,`district`,`email`,`photo`,`qualification`,`experience`,`gender`,`dob`,`DEPRTMENT_id`,`LOGIN_id`) values 
(1,'latheef','MANJERI','675498','MALAPPuram','abdullatheea@gmail.com','/media/20241005-084206.jpg','bsccs','1','male','1970-01-15',4,2),
(3,'AKHILA P','MANJERI','675498','MALAPPuram','akhila@gmail.com','/media/20241005-084206.jpg','set','5','female','2024-10-16',3,4),
(4,'sakeena','uiufdghj','345645','dfghjkhgfhjkhg','sakkeena.com','/media/20241212-083636.jpg','drkugjh','4','female','2024-12-10',3,7),
(5,'fgvx','dxs','2345678907','Kasaragod','trfgyhunjk@gmailcom','/media/20241222-113246.jpg','345','433','female','2024-12-24',3,8);

/*Data for the table `myapp_student` */

insert  into `myapp_student`(`id`,`admissionNo`,`name`,`dob`,`place`,`email`,`phone`,`pin`,`COURSE_id`) values 
(1,'6676','jhjfhdsg','2024-11-11','sdff','jhd@gamil.com','56565656','098754',3),
(3,'5656','GHUTYG','2025-01-01','DFYUIUGFCFGH','bhjgvhg@gmail.com','9865421','09865',3),
(4,'kjlvef','dknck','2024-11-19','kfvlkfo','ldkjvi@gmail.com','876543','098765',4),
(8,'9876','jhghnm','2024-11-20','jhghj','kjhgfy@gmail.com','987654','098765',3);

/*Data for the table `myapp_subject` */

insert  into `myapp_subject`(`id`,`subjectname`,`COURSE_id`) values 
(3,'COA',3),
(4,'TOC',3),
(5,'dgfdhfg',3);

/*Data for the table `myapp_support` */

insert  into `myapp_support`(`id`,`category`,`discription`) values 
(1,'Certificate','tfkhjiduyfwr'),
(3,'fyegfuio',''),
(4,'dgfdhgf',''),
(5,'dgfdhgf5767','');

/*Data for the table `myapp_timetable` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
