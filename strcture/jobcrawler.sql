-- phpMyAdmin SQL Dump
-- version 4.0.9
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 02, 2018 at 06:24 PM
-- Server version: 5.6.14
-- PHP Version: 5.5.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `jobcrawler`
--

-- --------------------------------------------------------

--
-- Table structure for table `company_list`
--

CREATE TABLE IF NOT EXISTS `company_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(100) NOT NULL,
  `address` text NOT NULL,
  `office_location` varchar(100) NOT NULL,
  `website` text NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `description` text NOT NULL,
  `domain` text NOT NULL,
  `company_url` varchar(255) NOT NULL,
  `company_id` int(11) NOT NULL,
  `current_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Unique_company` (`company_id`),
  UNIQUE KEY `company_name` (`company_name`,`company_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=102 ;

-- --------------------------------------------------------

--
-- Table structure for table `technopark`
--

CREATE TABLE IF NOT EXISTS `technopark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL,
  `apply_link` varchar(255) NOT NULL,
  `company_url` varchar(255) NOT NULL,
  `company_id` int(11) NOT NULL,
  `mail_id` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `skills` text NOT NULL,
  `walkin` varchar(20) NOT NULL DEFAULT 'False',
  `walkin_venu` text NOT NULL,
  `status` varchar(11) DEFAULT NULL,
  `closing_date` date NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `apply_link` (`apply_link`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=263 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
