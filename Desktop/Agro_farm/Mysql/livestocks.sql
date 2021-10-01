-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Oct 01, 2021 at 12:01 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `livestocks`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_profile`
--

CREATE TABLE `accounts_profile` (
  `id` bigint(20) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `profile_pic` varchar(100) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_profile`
--

INSERT INTO `accounts_profile` (`id`, `firstname`, `lastname`, `username`, `email`, `phone`, `profile_pic`, `created_date`, `user_id`) VALUES
(1, 'Chirag', 'Simkhada', 'chirag', '', '9876535790', 'static/profiles/Kadaknath_chicken_D3dxCaH.jpg', '2021-09-30 05:42:15.558232', 1),
(2, '', '', 'Manish', '', '', 'static/profiles/user1.jpg', '2021-09-30 05:43:01.157229', 2),
(3, '', '', 'Gautam', '', '', 'static/profiles/user1.jpg', '2021-09-30 06:46:15.976668', 3),
(4, 'Avishek', 'Khadka', 'Avishek', '', '9865457892', 'static/profiles/Local_goat.jpg', '2021-09-30 06:47:41.041384', 4),
(5, '', '', 'Saugat', '', '', 'static/profiles/user1.jpg', '2021-09-30 06:48:34.598329', 5);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add profile', 7, 'add_profile'),
(26, 'Can change profile', 7, 'change_profile'),
(27, 'Can delete profile', 7, 'delete_profile'),
(28, 'Can view profile', 7, 'view_profile'),
(29, 'Can add category', 8, 'add_category'),
(30, 'Can change category', 8, 'change_category'),
(31, 'Can delete category', 8, 'delete_category'),
(32, 'Can view category', 8, 'view_category'),
(33, 'Can add livestock', 9, 'add_livestock'),
(34, 'Can change livestock', 9, 'change_livestock'),
(35, 'Can delete livestock', 9, 'delete_livestock'),
(36, 'Can view livestock', 9, 'view_livestock'),
(37, 'Can add cart', 10, 'add_cart'),
(38, 'Can change cart', 10, 'change_cart'),
(39, 'Can delete cart', 10, 'delete_cart'),
(40, 'Can view cart', 10, 'view_cart'),
(41, 'Can add order', 11, 'add_order'),
(42, 'Can change order', 11, 'change_order'),
(43, 'Can delete order', 11, 'delete_order'),
(44, 'Can view order', 11, 'view_order');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$1cq10mspLxllgNcX07f5wG$8DaQut9tLOuEMZDH40BXx7JECGzFNC31YjFSRUb8v2E=', '2021-10-01 04:02:07.453994', 0, 'chirag', '', '', '', 0, 1, '2021-09-30 05:42:14.803971'),
(2, 'pbkdf2_sha256$260000$ksgJKzylKucOYLdBe3Ar3G$8AU29+mgi13TSmGCNPgWxfXueknnnTn+fzHq79VisgU=', '2021-10-01 04:03:56.597566', 1, 'Manish', '', '', '', 1, 1, '2021-09-30 05:43:00.586514'),
(3, 'pbkdf2_sha256$260000$FHHog887BXYzBLUjxQUQgc$IOpGkKstItGsLp2gv9qCG0dSn5Oz8dsKOvD/HRZ5+9s=', '2021-09-30 07:29:21.299210', 1, 'Gautam', '', '', '', 1, 1, '2021-09-30 06:46:15.421996'),
(4, 'pbkdf2_sha256$260000$XzZUfpG9Vq5ePCGI4zBUxS$wIsyl4TnOV1hiyy/aWXprHS8zrb7VF0Qk8/XqE+wHKA=', '2021-09-30 12:33:08.552484', 0, 'Avishek', '', '', '', 0, 1, '2021-09-30 06:47:40.517959'),
(5, 'pbkdf2_sha256$260000$r7wAbaC8Qi8GcmCuWIhAOz$mCO9SnvJP90s8MuwV+pjE6hePuDj4aMceCpB8790R+o=', '2021-09-30 06:48:49.509967', 0, 'Saugat', '', '', '', 0, 1, '2021-09-30 06:48:34.081785');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'profile'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'livestocks', 'cart'),
(8, 'livestocks', 'category'),
(9, 'livestocks', 'livestock'),
(11, 'livestocks', 'order'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-09-30 05:38:36.999054'),
(2, 'auth', '0001_initial', '2021-09-30 05:38:59.527377'),
(3, 'accounts', '0001_initial', '2021-09-30 05:39:03.616238'),
(4, 'admin', '0001_initial', '2021-09-30 05:39:10.306253'),
(5, 'admin', '0002_logentry_remove_auto_add', '2021-09-30 05:39:10.377540'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2021-09-30 05:39:10.655303'),
(7, 'contenttypes', '0002_remove_content_type_name', '2021-09-30 05:39:13.110080'),
(8, 'auth', '0002_alter_permission_name_max_length', '2021-09-30 05:39:15.739877'),
(9, 'auth', '0003_alter_user_email_max_length', '2021-09-30 05:39:16.841955'),
(10, 'auth', '0004_alter_user_username_opts', '2021-09-30 05:39:17.108941'),
(11, 'auth', '0005_alter_user_last_login_null', '2021-09-30 05:39:19.067616'),
(12, 'auth', '0006_require_contenttypes_0002', '2021-09-30 05:39:19.152344'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2021-09-30 05:39:19.265463'),
(14, 'auth', '0008_alter_user_username_max_length', '2021-09-30 05:39:19.669774'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2021-09-30 05:39:20.076749'),
(16, 'auth', '0010_alter_group_name_max_length', '2021-09-30 05:39:20.365886'),
(17, 'auth', '0011_update_proxy_permissions', '2021-09-30 05:39:20.480980'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2021-09-30 05:39:21.510143'),
(19, 'livestocks', '0001_initial', '2021-09-30 05:39:25.906277'),
(20, 'livestocks', '0002_category_category_image', '2021-09-30 05:39:26.805425'),
(21, 'livestocks', '0003_cart', '2021-09-30 05:39:33.931679'),
(22, 'livestocks', '0004_order', '2021-09-30 05:39:39.631790'),
(23, 'livestocks', '0005_auto_20210927_0843', '2021-09-30 05:39:41.406536'),
(24, 'sessions', '0001_initial', '2021-09-30 05:39:43.698970');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('afhvr7c331heopsf793n5i5tl4gw0at8', '.eJxVjEEOwiAQRe_C2hCcwkBcuvcMZGAYqRqalHZlvLtt0oVu33v_v1Wkdalx7WWOI6uLAnX6ZYnys7Rd8IPafdJ5ass8Jr0n-rBd3yYur-vR_h1U6nVbewSUYKyDYFPIwQ6WvHHGAToPYv3Z8MAomQTQFzAuSEnIkqFsENXnC6ujN30:1mW9m8:mnX5knQyJTxeZJLS5opchEtMcS_pJ0fB0wrnXvjfl3M', '2021-10-15 04:03:56.735837'),
('iieun311hdksj4cve0zwxwi72yk8ow0m', '.eJxVjEEOwiAQRe_C2pApIxRcuvcMZGBGqRpISrsy3l2bdKHb_977LxVpXUpcu8xxYnVSqA6_W6L8kLoBvlO9NZ1bXeYp6U3RO-360lie5939OyjUy7d2NguzyWCdJQM4Ggd-AEC0YRDvxCfPOFIwzosAHYNFL3DFFAAhJ_X-ALszNt0:1mVqVN:RHzjTz8clm0Dju_n4FvG_-Cgw23XSJGrWivKlZOk1ek', '2021-10-14 07:29:21.448822');

-- --------------------------------------------------------

--
-- Table structure for table `livestocks_cart`
--

CREATE TABLE `livestocks_cart` (
  `id` bigint(20) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `livestock_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `livestocks_cart`
--

INSERT INTO `livestocks_cart` (`id`, `created_date`, `livestock_id`, `user_id`) VALUES
(8, '2021-10-01 03:46:59.980122', 9, 1),
(9, '2021-10-01 03:47:08.153385', 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `livestocks_category`
--

CREATE TABLE `livestocks_category` (
  `id` bigint(20) NOT NULL,
  `category_name` varchar(200) DEFAULT NULL,
  `category_description` longtext DEFAULT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `category_image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `livestocks_category`
--

INSERT INTO `livestocks_category` (`id`, `category_name`, `category_description`, `created_date`, `category_image`) VALUES
(1, 'Goat', 'There are many kinds of goats found in Nepal. In our farm farm we are raising two breeds which are Boer and Local Goat. The Boer goat is a breed of goat that was developed in South Africa in the early 1900s and is a popular breed for meat production. and Local goat is raised locally in Nepal.', '2021-09-30 05:49:18.742252', 'static/uploads/Goat_c7oEvfm.jpeg'),
(2, 'Chicken', 'Chicken is the most common type of poultry in the world. In Nepal, Kadaknath, Broiler. and local type chickens are more famous. In our farm, we have raised all these breeds and also their eggs.', '2021-09-30 05:55:21.153440', 'static/uploads/Chicken_9IBd309.jpg'),
(3, 'Pig', 'Pig farming trend is changing gradually due to urbanization some commercial and modern pig farming practice recently started in Nepal. In our farm we have raise pigs in big volume and also selling baby pigs.', '2021-09-30 05:58:06.761983', 'static/uploads/Pigs_EohBqMg.jpg'),
(4, 'Quail', 'Quail farming in Nepal is going popular between farmers, raising quail for meat and eggs. Quails are smallest species of poultry bird. In our farm we have raise quail in small amount and also their eggs.abcad1223', '2021-09-30 06:00:13.172173', 'static/uploads/Quailem_or_f_ybHNrKL.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `livestocks_livestock`
--

CREATE TABLE `livestocks_livestock` (
  `id` bigint(20) NOT NULL,
  `livestock_name` varchar(200) NOT NULL,
  `livestock_price` double NOT NULL,
  `livestock_image` varchar(100) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `category_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `livestocks_livestock`
--

INSERT INTO `livestocks_livestock` (`id`, `livestock_name`, `livestock_price`, `livestock_image`, `created_date`, `category_id`) VALUES
(1, 'Baby Goat', 5000, 'static/uploads/baby_goat_W5SoZ6Q.jpg', '2021-09-30 06:01:12.887111', 1),
(2, 'Baby Pig', 2000, 'static/uploads/baby_pig_mOinWBU.jpg', '2021-09-30 06:01:52.426453', 3),
(3, 'Local Chicken', 1500, 'static/uploads/Local_chicken_c79wFwx.jpg', '2021-09-30 06:02:25.416518', 2),
(4, 'Kadaknath Chicken', 4000, 'static/uploads/Kadaknath_chicken_PPz1uHn.jpg', '2021-09-30 06:03:01.865772', 2),
(5, 'Quail(male or female)', 200, 'static/uploads/Quailem_or_f_qrh1ufN.jpg', '2021-09-30 06:03:44.646371', 4),
(6, 'Quail Egg', 300, 'static/uploads/Quail_egg_jhSyEN0.jpg', '2021-09-30 06:04:34.730122', 4),
(7, 'Chicken Eggs', 350, 'static/uploads/Chicken_egg_Uk5SgCi.jpg', '2021-09-30 06:05:02.047082', 2),
(8, 'Local Goat', 25000, 'static/uploads/Local_goat_QQNkl8q.jpg', '2021-09-30 06:05:57.118107', 1),
(9, 'Pig(male or female)', 20000, 'static/uploads/Pigs_XoVALzk.jpg', '2021-09-30 06:06:37.908305', 3),
(10, 'Boer Goat', 150000, 'static/uploads/Boer_goat_fY4Opfk.jpg', '2021-09-30 06:07:12.847220', 1),
(11, 'Broiler Chicken', 350, 'static/uploads/Broiler_chicken_ZhzAdB9.jpg', '2021-09-30 06:08:19.420905', 2);

-- --------------------------------------------------------

--
-- Table structure for table `livestocks_order`
--

CREATE TABLE `livestocks_order` (
  `id` bigint(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `total_price` int(11) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `contact_no` varchar(10) DEFAULT NULL,
  `contact_address` varchar(200) DEFAULT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `livestock_id` bigint(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `payment_method` varchar(200) DEFAULT NULL,
  `payment_status` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `livestocks_order`
--

INSERT INTO `livestocks_order` (`id`, `quantity`, `total_price`, `status`, `contact_no`, `contact_address`, `created_date`, `livestock_id`, `user_id`, `payment_method`, `payment_status`) VALUES
(6, 1, 4000, 'Delivered', '987654321', 'Dillibazar', '2021-09-30 12:29:34.415279', 4, 4, 'Esewa', 0),
(7, 2, 8000, 'Pending', '9841567890', 'Balaju', '2021-10-01 04:02:26.915833', 4, 1, 'Esewa', 0),
(8, 1, 150000, 'Delivered', '987654321', 'Dillibazar', '2021-10-01 04:03:17.454815', 10, 1, 'Esewa', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `livestocks_cart`
--
ALTER TABLE `livestocks_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `livestocks_cart_livestock_id_dc4f0f00_fk_livestocks_livestock_id` (`livestock_id`),
  ADD KEY `livestocks_cart_user_id_b5629389_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `livestocks_category`
--
ALTER TABLE `livestocks_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `livestocks_livestock`
--
ALTER TABLE `livestocks_livestock`
  ADD PRIMARY KEY (`id`),
  ADD KEY `livestocks_livestock_category_id_280a5aa4_fk_livestock` (`category_id`);

--
-- Indexes for table `livestocks_order`
--
ALTER TABLE `livestocks_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `livestocks_order_livestock_id_a3ebc305_fk_livestock` (`livestock_id`),
  ADD KEY `livestocks_order_user_id_21bafd45_fk_auth_user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `livestocks_cart`
--
ALTER TABLE `livestocks_cart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `livestocks_category`
--
ALTER TABLE `livestocks_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `livestocks_livestock`
--
ALTER TABLE `livestocks_livestock`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `livestocks_order`
--
ALTER TABLE `livestocks_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD CONSTRAINT `accounts_profile_user_id_49a85d32_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `livestocks_cart`
--
ALTER TABLE `livestocks_cart`
  ADD CONSTRAINT `livestocks_cart_livestock_id_dc4f0f00_fk_livestocks_livestock_id` FOREIGN KEY (`livestock_id`) REFERENCES `livestocks_livestock` (`id`),
  ADD CONSTRAINT `livestocks_cart_user_id_b5629389_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `livestocks_livestock`
--
ALTER TABLE `livestocks_livestock`
  ADD CONSTRAINT `livestocks_livestock_category_id_280a5aa4_fk_livestock` FOREIGN KEY (`category_id`) REFERENCES `livestocks_category` (`id`);

--
-- Constraints for table `livestocks_order`
--
ALTER TABLE `livestocks_order`
  ADD CONSTRAINT `livestocks_order_livestock_id_a3ebc305_fk_livestock` FOREIGN KEY (`livestock_id`) REFERENCES `livestocks_livestock` (`id`),
  ADD CONSTRAINT `livestocks_order_user_id_21bafd45_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
