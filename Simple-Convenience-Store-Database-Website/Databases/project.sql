-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 03, 2025 at 01:10 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `coaches`
--

CREATE TABLE `coaches` (
  `CoachID` tinyint(4) NOT NULL,
  `LastName` varchar(9) DEFAULT NULL,
  `FirstName` varchar(8) DEFAULT NULL,
  `Sport` varchar(24) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `City` varchar(8) DEFAULT NULL,
  `PostalCode` varchar(7) DEFAULT NULL,
  `Country` varchar(3) DEFAULT NULL,
  `Email` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `coaches`
--

INSERT INTO `coaches` (`CoachID`, `LastName`, `FirstName`, `Sport`, `Address`, `City`, `PostalCode`, `Country`, `Email`) VALUES
(1, 'Davolio', 'Nancy', 'Soccer', '507 - 20th Ave. E.\r\nApt. 2A', 'Seattle', '98122', 'USA', 'nancy.davolio@gmail.com'),
(2, 'Fuller', 'Andrew', 'Tennis', '908 W. Capital Way', 'Tacoma', '98401', 'USA', 'afuller@yahoo.com'),
(3, 'Leverling', 'Janet', 'Basketball', '722 Moss Bay Blvd.', 'Kirkland', '98033', 'USA', 'janetl@gmail.com'),
(4, 'Peacock', 'Margaret', 'Tennis', '4110 Old Redmond Rd.', 'Redmond', '98052', 'USA', 'mpeacock08@gmail.com'),
(5, 'Buchanan', 'Steven', 'Soccer', '14 Garrett Hill', 'London', '89567', 'UK', 'steven.buchanan@gmail.com'),
(6, 'Suyama', 'Michael', 'Basketball', 'Coventry House\r\nMiner Rd.', 'London', 'EC2 7JR', 'UK', 'msuyama@hotmail.com'),
(7, 'King', 'Robert', 'Soccer', 'Edgeham Hollow\r\nWinchester Way', 'London', 'RG1 9SP', 'UK', 'Lauraking@gmail.com'),
(8, 'Callahan', 'Laura', 'Tennis', '4726 - 11th Ave. N.E.', 'Seattle', '98105', 'USA', 'lcallahan25@gmail.com'),
(9, 'Dodsworth', 'Anne', 'Soccer', '7 Houndstooth Rd.', 'London', '78154', 'UK', 'anne.dodsworth@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `doctors`
--

CREATE TABLE `doctors` (
  `DoctorID` varchar(5) NOT NULL,
  `DoctorName` varchar(30) DEFAULT NULL,
  `PostalCode` varchar(9) DEFAULT NULL,
  `Country` varchar(11) DEFAULT NULL,
  `Phone` varchar(17) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `doctors`
--

INSERT INTO `doctors` (`DoctorID`, `DoctorName`, `PostalCode`, `Country`, `Phone`) VALUES
('AFUTT', 'Adam Futterkiste', 'T5C 5P8', 'Canada', '(780) 123-4567'),
('AJAME', 'Aaron James', 'T6B 1R3', 'Canada', '(587) 886-0015'),
('BMCKE', 'Bernard McKenzie', 'T6J 4V7', 'Canada', '(780) 215-3551'),
('CHIGG', 'Carson Higgins', 'T5N 8M7', 'Canada', '(780) 885-7193'),
('DAARO', 'Demetry Aaron', 'T6V 5L6', 'Canada', '(780) 910-0840'),
('DCLOS', 'Donald Closterman', 'T6A 1A1', 'Canada', '(587) 353-9085'),
('JADAM', 'James Adams', 'T5P 8E4', 'Canada', '(780) 810-1008'),
('JEDWA', 'James Edwards', 'T6K 4R1', 'Canada', '(587) 660-0507');

-- --------------------------------------------------------

--
-- Table structure for table `hospitals`
--

CREATE TABLE `hospitals` (
  `HospitalID` varchar(5) NOT NULL,
  `HospitalName` varchar(60) DEFAULT NULL,
  `Address` varchar(80) DEFAULT NULL,
  `City` varchar(15) DEFAULT NULL,
  `PostalCode` varchar(9) DEFAULT NULL,
  `Country` varchar(11) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `hospitals`
--

INSERT INTO `hospitals` (`HospitalID`, `HospitalName`, `Address`, `City`, `PostalCode`, `Country`, `Email`) VALUES
('CALGH', 'Calgary General Hospital', '17205 - 79 Street SW', 'Calgary', 'T2P 2E4', 'Canada', 'info@cghospital.ab.ca'),
('GREYN', 'Grey Nuns Community Hospital', '1395 - 13 Street NW', 'Edmonton', 'T6J 4V7', 'Canada', 'info@greynuns.ab.ca'),
('MISCH', 'Misericordia Community Hospital', '10020 87 Avenue NW', 'Edmonton', 'T5N 8M7', 'Canada', 'info@mrch.ab.ca'),
('NALHC', 'Northern Alberta Health Center', '8997 Century Park NW', 'St Albert', 'T8P 1R3', 'Canada', 'info@nahc.ab.ca'),
('RALEX', 'Royal Alexandra', '11265 - 19 Avenue NW', 'Edmonton', 'T5C 5P8', 'Canada', 'info@ralex.ab.ca'),
('SHPCH', 'Sherwood Park Community Hospital', '3255 Sherwood Park NW', 'Sherwood Park', 'T8A 1A1', 'Canada', 'info@sphospital.ab.ca'),
('STALH', 'St Albert General Hospital', '8762 92 Avenue SW', 'St Albert', 'T8Y 5L6', 'Canada', 'info@sagh.ab.ca');

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `ItemID` tinyint(4) NOT NULL,
  `ItemName` varchar(32) DEFAULT NULL,
  `Price` decimal(7,4) DEFAULT NULL,
  `UnitsInStock` smallint(6) DEFAULT NULL,
  `Visible` int(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`ItemID`, `ItemName`, `Price`, `UnitsInStock`, `Visible`) VALUES
(1, 'Cereal', 18.0000, 39, 1),
(2, 'Tea', 19.0000, 17, 1),
(3, 'Corn Syrup', 10.0000, 13, 1),
(4, 'Seasoning Salt', 22.0000, 53, 1),
(5, 'Cumin Powder', 21.3500, 0, 1),
(6, 'Bread Slices', 25.0000, 120, 1),
(7, 'Feta Cheese', 30.0000, 15, 1),
(8, 'Chedder Cheese', 40.0000, 6, 1),
(9, 'Noodles', 97.0000, 29, 1),
(10, 'Beans', 31.0000, 31, 1),
(11, 'Milk', 21.0000, 22, 1),
(12, 'Eggs', 38.0000, 86, 1),
(13, 'Rice', 6.0000, 24, 1),
(14, 'Tofu', 23.2500, 35, 1),
(15, 'Pasta', 15.5000, 39, 1);

-- --------------------------------------------------------

--
-- Table structure for table `organizations`
--

CREATE TABLE `organizations` (
  `OrganizationID` tinyint(4) NOT NULL,
  `OrganizationName` varchar(60) DEFAULT NULL,
  `Address` varchar(80) DEFAULT NULL,
  `PostalCode` varchar(9) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `organizations`
--

INSERT INTO `organizations` (`OrganizationID`, `OrganizationName`, `Address`, `PostalCode`, `Email`) VALUES
(1, 'Royal Alexandra Org.', '11265 - 19 Avenue NW', 'T5C 5P8', 'info@ralex.com'),
(2, 'Grey Nuns Community Org.', '1395 - 13 Street NW', 'T6J 4V7', 'info@greynuns.com'),
(3, 'Harry Ainly Corporation', '3255 Sherwood Park NW', 'T8A 1A1', 'info@hainly.ca'),
(4, 'Mount Royal Org.', '10020 87 Avenue NW', 'T5N 8M7', 'info@mroyal.com'),
(5, 'Norquest Community Organization', '8762 92 Avenue SW', 'T8Y 5L6', 'info@norquest.ca'),
(6, 'NAIT Health Services', '8997 Century Park NW', 'T8P 1R3', 'info@nait.ca'),
(7, 'SAIT Health Services', '17205 - 79 Street SW', 'T2P 2E4', 'info@sait.ca');

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `PatientID` varchar(5) NOT NULL,
  `PatientName` varchar(30) DEFAULT NULL,
  `Address` varchar(80) DEFAULT NULL,
  `City` varchar(15) DEFAULT NULL,
  `PostalCode` varchar(9) DEFAULT NULL,
  `Country` varchar(11) DEFAULT NULL,
  `Phone` varchar(17) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`PatientID`, `PatientName`, `Address`, `City`, `PostalCode`, `Country`, `Phone`) VALUES
('ADAMJ', 'Adam James', '3229 Century Park NW', 'Edmonton', 'T6B 1R3', 'Canada', '(587) 886-0015'),
('ALFRF', 'Alfreds Futterkiste', '11265 - 101 Avenue NW', 'Edmonton', 'T5C 5P8', 'Canada', '(780) 123-4567'),
('BENJM', 'Benjamin McKenzie', '1355 - 16 Street NW', 'Edmonton', 'T6J 4V7', 'Canada', '(780) 215-3551'),
('CAROH', 'Carol Higgins', '10020 Jasper Avenue NW', 'Edmonton', 'T5N 8M7', 'Canada', '(780) 885-7193'),
('DAVIA', 'David Aaron', '8522 15 Avenue SW', 'Edmonton', 'T6V 5L6', 'Canada', '(780) 910-0840'),
('DAVIC', 'David Closterman', '215 Michener Park NW', 'Edmonton', 'T6A 1A1', 'Canada', '(587) 353-9085'),
('JERRA', 'Jerry Adams', '1815 - 89 Street NW', 'Edmonton', 'T5P 8E4', 'Canada', '(780) 810-1008'),
('JOHNE', 'John Edwards', '2856 - 54 Avenue NW', 'Edmonton', 'T6K 4R1', 'Canada', '(587) 660-0507');

-- --------------------------------------------------------

--
-- Table structure for table `players`
--

CREATE TABLE `players` (
  `PlayerID` tinyint(4) NOT NULL,
  `LastName` varchar(9) DEFAULT NULL,
  `FirstName` varchar(8) DEFAULT NULL,
  `Position` varchar(24) DEFAULT NULL,
  `BirthDate` varchar(19) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `City` varchar(8) DEFAULT NULL,
  `PostalCode` varchar(7) DEFAULT NULL,
  `Country` varchar(3) DEFAULT NULL,
  `Phone` varchar(14) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `players`
--

INSERT INTO `players` (`PlayerID`, `LastName`, `FirstName`, `Position`, `BirthDate`, `Address`, `City`, `PostalCode`, `Country`, `Phone`) VALUES
(1, 'Davolio', 'Nancy', 'Defense', '2000-12-08 00:00:00', '507 - 20th Ave. E.\r\nApt. 2A', 'Seattle', '98122', 'USA', '(206) 555-9857'),
(2, 'Fuller', 'Andrew', 'Midfielder', '2001-02-19 00:00:00', '908 W. Capital Way', 'Tacoma', '98401', 'USA', '(206) 555-9482'),
(3, 'Leverling', 'Janet', 'Attacker', '1998-08-30 00:00:00', '722 Moss Bay Blvd.', 'Kirkland', '98033', 'USA', '(206) 555-3412'),
(4, 'Peacock', 'Margaret', 'Defense', '1993-05-03 00:00:00', '4110 Old Redmond Rd.', 'Redmond', '98052', 'USA', '(206) 555-8122'),
(5, 'Buchanan', 'Steven', 'Midfielder', '1993-10-17 00:00:00', '14 Garrett Hill', 'London', '89567', 'UK', '(71) 555-4848'),
(6, 'Suyama', 'Michael', 'Attacker', '1997-10-17 00:00:00', 'Coventry House\r\nMiner Rd.', 'London', 'EC2 7JR', 'UK', '(71) 555-7773'),
(7, 'King', 'Robert', 'Midfielder', '1994-01-02 00:00:00', 'Edgeham Hollow\r\nWinchester Way', 'London', 'RG1 9SP', 'UK', '(71) 555-5598'),
(8, 'Callahan', 'Laura', 'Defense', '1995-03-05 00:00:00', '4726 - 11th Ave. N.E.', 'Seattle', '98105', 'USA', '(206) 555-1189'),
(9, 'Dodsworth', 'Anne', 'Defense', '1999-11-15 00:00:00', '7 Houndstooth Rd.', 'London', '78154', 'UK', '(71) 555-4444');

-- --------------------------------------------------------

--
-- Table structure for table `schools`
--

CREATE TABLE `schools` (
  `SchoolID` varchar(5) NOT NULL,
  `SchoolName` varchar(60) DEFAULT NULL,
  `Address` varchar(80) DEFAULT NULL,
  `PostalCode` varchar(9) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `schools`
--

INSERT INTO `schools` (`SchoolID`, `SchoolName`, `Address`, `PostalCode`, `Email`) VALUES
('AVLJH', 'Avalon Junior High School', '8997 Century Park NW', 'T8P 1R3', 'avalon@epsb.ca'),
('GRVES', 'Grand View Elementary School', '3255 Sherwood Park NW', 'T8A 1A1', 'grand.view@epsb.ca'),
('HANHS', 'Harry Ainly High School', '17205 - 79 Street SW', 'T2P 2E4', 'hainly@epsb.ca'),
('LDNES', 'Lansdowne Elementary School', '10020 87 Avenue NW', 'T5N 8M7', 'lansdowne@epsb.ca'),
('MALES', 'Malmo Elementary School', '11265 - 19 Avenue NW', 'T5C 5P8', 'malmo@epsb.ca'),
('MTPES', 'Mount Pleasant Elementary School', '1395 - 13 Street NW', 'T6J 4V7', 'mtpleasant@epsb.ca'),
('VBRJH', 'Vernon Barford Junior High School', '8762 92 Avenue SW', 'T8Y 5L6', 'vbarford@epsb.ca');

-- --------------------------------------------------------

--
-- Table structure for table `sports`
--

CREATE TABLE `sports` (
  `SportID` varchar(7) NOT NULL,
  `SportName` varchar(68) DEFAULT NULL,
  `TrainingHours` varchar(2) DEFAULT NULL,
  `MonthlyFee` decimal(8,4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `sports`
--

INSERT INTO `sports` (`SportID`, `SportName`, `TrainingHours`, `MonthlyFee`) VALUES
('BKBLL01', 'Jonir Basketball', '75', 600.0000),
('BKBLL02', 'Advanced Basketball', '80', 450.0000),
('BSBLL01', 'Baseball for Beginners', '80', 450.0000),
('BSBLL02', 'Baseball for Advanced', '75', 300.0000),
('FBALL01', 'Football for Beginners', '90', 450.0000),
('FBALL02', 'Football for Advanced', '90', 450.0000);

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

CREATE TABLE `teachers` (
  `TeacherNumber` int(11) NOT NULL,
  `FirstName` varchar(13) DEFAULT NULL,
  `LastName` varchar(15) DEFAULT NULL,
  `DisplayName` varchar(13) DEFAULT NULL,
  `CountryCode` varchar(2) DEFAULT NULL,
  `Gender` varchar(1) DEFAULT NULL,
  `BirthDate` varchar(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `teachers`
--

INSERT INTO `teachers` (`TeacherNumber`, `FirstName`, `LastName`, `DisplayName`, `CountryCode`, `Gender`, `BirthDate`) VALUES
(19770001, 'Bess', 'Woods', 'Bess', 'CA', 'F', '1979-11-04 00:00:00'),
(19790001, 'Emmy', 'Economos', 'Em', 'CA', 'F', '1976-10-14 00:00:00'),
(19800001, 'Aidan', 'Hendrickson', 'Aidan', 'CA', 'M', '1976-09-27 00:00:00'),
(19820003, 'Zane', 'Zilewski', 'Zane', 'PL', 'M', '1977-02-25 00:00:00'),
(19850003, 'Hayley', 'Anthony', 'Hayley', 'CA', 'F', '1977-04-30 00:00:00'),
(19870101, 'Kelsey', 'Parmalee', 'Kelsey', 'CA', 'F', '1983-11-09 00:00:00'),
(19880001, 'Warton', 'Keyes', 'Warton', 'CA', 'M', '1979-12-02 00:00:00'),
(19900001, 'Marcus', 'Taft', 'Marcus', 'CA', 'M', '1978-12-23 00:00:00'),
(19900002, 'Paolo', 'Sherwood', 'Paolo', 'CA', 'M', '1979-10-11 00:00:00'),
(19920001, 'K.D.', 'Moran', 'K.D.', 'CA', 'M', '1979-07-07 00:00:00'),
(19920002, 'Patrick', 'Jeffries', 'Pat', 'CA', 'M', '1979-07-26 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `coaches`
--
ALTER TABLE `coaches`
  ADD PRIMARY KEY (`CoachID`);

--
-- Indexes for table `doctors`
--
ALTER TABLE `doctors`
  ADD PRIMARY KEY (`DoctorID`);

--
-- Indexes for table `hospitals`
--
ALTER TABLE `hospitals`
  ADD PRIMARY KEY (`HospitalID`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`ItemID`);

--
-- Indexes for table `organizations`
--
ALTER TABLE `organizations`
  ADD PRIMARY KEY (`OrganizationID`);

--
-- Indexes for table `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`PatientID`);

--
-- Indexes for table `players`
--
ALTER TABLE `players`
  ADD PRIMARY KEY (`PlayerID`);

--
-- Indexes for table `schools`
--
ALTER TABLE `schools`
  ADD PRIMARY KEY (`SchoolID`);

--
-- Indexes for table `sports`
--
ALTER TABLE `sports`
  ADD PRIMARY KEY (`SportID`);

--
-- Indexes for table `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`TeacherNumber`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
