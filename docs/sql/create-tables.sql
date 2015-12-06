--
-- temperature-sensor-server - http://github.com/blueskyfish/temperature-sensor-server.git
--
-- The MIT License (MIT)
-- Copyright (c) 2015 BlueSkyFish
--
-- CREATE DATABASE `temo-server` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
--

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor-currents`
--

DROP TABLE IF EXISTS `sensor-currents`;
CREATE TABLE IF NOT EXISTS `sensor-currents` (
  `group_id` int(11) NOT NULL,
  `name_id` int(11) NOT NULL,
  `temperature` int(11) NOT NULL DEFAULT '0' COMMENT 'current temperature from sensor',
  `humidity` int(11) NOT NULL DEFAULT '0' COMMENT 'current humidity from sensor',
  `date` datetime NOT NULL DEFAULT '1970-01-01 00:00:00' COMMENT 'the last timestamp'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='(temperature monitoring) the current temperature and humidity';

--
-- Daten für Tabelle `sensor-currents`
--

INSERT INTO `sensor-currents` (`group_id`, `name_id`, `temperature`, `humidity`, `date`) VALUES
(1000, 0, 0, 0, '1970-01-01 00:00:00');


-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor-names`
--

DROP TABLE IF EXISTS `sensor-names`;
CREATE TABLE `sensor-names` (
  `group_id` int(11) NOT NULL,
  `name_id` int(11) NOT NULL COMMENT 'the id of the sensor (range: 0..7)',
  `title` varchar(120) NOT NULL COMMENT 'the name of the sensor',
  `description` varchar(400) NOT NULL COMMENT 'a short description of the sensor',
  `icon` varchar(240) NOT NULL COMMENT 'font awesome icon name'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='(temperature monitoring) the sensor names';


--
-- Daten für Tabelle `sensor-names`
--

INSERT INTO `sensor-names` (`group_id`, `name_id`, `title`, `description`, `icon`) VALUES
(1000, 0, 'Wohnzimmer', 'Test Sensor im Wohnzimmer', 'fa-user');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor-readers`
--

DROP TABLE IF EXISTS `sensor-readers`;
CREATE TABLE IF NOT EXISTS `sensor-readers` (
  `group_id` int(11) NOT NULL,
  `name` varchar(120) NOT NULL COMMENT 'the name of the sensor reader',
  `description` varchar(400) NOT NULL COMMENT 'a short description',
  `icon` varchar(240) NOT NULL COMMENT 'font awesome icon name'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='(temperature monitoring) the sensor group';

--
-- Daten für Tabelle `sensor-readers`
--

INSERT INTO `sensor-readers` (`group_id`, `name`, `description`, `icon`) VALUES
(1000, 'Sensor 1', 'Test Sensor Reader', 'fa-home');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensors`
--

DROP TABLE IF EXISTS `sensors`;
CREATE TABLE IF NOT EXISTS `sensors` (
  `sensor_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL COMMENT 'the group id of the sensor reader',
  `name_id` int(10) NOT NULL COMMENT 'the name id of the sensor',
  `temperature` int(11) NOT NULL COMMENT 'The temperature value is multiplied by 100',
  `humidity` int(11) NOT NULL COMMENT 'The humidity value is multiplied by 100',
  `date` datetime NOT NULL,
  `status` enum('SAVED','DELETED') NOT NULL DEFAULT 'SAVED'
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8 COMMENT='(temperature monitoring) uploaded sensor dates';


--
-- Indizes für die Tabelle `sensor-currents`
--
ALTER TABLE `sensor-currents`
  ADD PRIMARY KEY (`group_id`,`name_id`) USING BTREE;

--
-- Indizes für die Tabelle `sensor-names`
--
ALTER TABLE `sensor-names`
  ADD PRIMARY KEY (`group_id`,`name_id`) USING BTREE;

--
-- Indizes für die Tabelle `sensor-readers`
--
ALTER TABLE `sensor-readers`
  ADD PRIMARY KEY (`group_id`);

--
-- Indizes für die Tabelle `sensors`
--
ALTER TABLE `sensors`
  ADD PRIMARY KEY (`sensor_id`),
  ADD KEY `SENSOR` (`group_id`,`name_id`);

--
-- AUTO_INCREMENT für Tabelle `sensors`
--
ALTER TABLE `sensors`
  MODIFY `sensor_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=16;SET FOREIGN_KEY_CHECKS=1;

-- version 0.6.0 ------------------------------------------

--
-- Tabellenstruktur für Tabelle `sensor-hash`
--

DROP TABLE IF EXISTS `sensor-hash`;
CREATE TABLE IF NOT EXISTS `sensor-hash` (
  `hash_id` int(11) NOT NULL,
  `hash` varchar(120) NOT NULL COMMENT 'the unique hash',
  `name` varchar(120) NOT NULL COMMENT 'A short name or description',
  `enabled` enum('Y','N') NOT NULL DEFAULT 'Y'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='(temperature monitoring) The table contains the access hash for viewing the sensor data';

--
-- AUTO_INCREMENT für Tabelle `sensor-hash`
--
ALTER TABLE `sensor-hash`
ADD PRIMARY KEY (`hash_id`);

ALTER TABLE `sensor-hash`
MODIFY `hash_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;SET FOREIGN_KEY_CHECKS=1;

--
-- Tabellenstruktur für Tabelle `sensor-hash-rules`
--

DROP TABLE IF EXISTS `sensor-hash-rules`;
CREATE TABLE IF NOT EXISTS `sensor-hash-rules` (
  `group_id` int(11) NOT NULL COMMENT 'the group id of the sensor reader',
  `name_id` int(11) NOT NULL COMMENT 'the name id of the sensor',
  `hash_id` int(11) NOT NULL COMMENT 'the id of the hash'
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8 COMMENT='(temperature monitoring) The table contains the link between the table sensor-hash and sensor-names';

--
-- Indizes für die Tabelle `sensor-hash-rules`
--
ALTER TABLE `sensor-hash-rules`
ADD PRIMARY KEY `HASH_RULES` (`group_id`,`name_id`, `hash_id`) USING BTREE;

COMMIT;
