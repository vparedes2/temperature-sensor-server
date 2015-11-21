<?php
/*
 * temperature-sensor-server - http://github.com/blueskyfish/temperature-sensor-server.git
 *
 * The MIT License (MIT)
 * Copyright (c) 2015 BlueSkyFish
 *
 * Distributed on "<%= datetime %> @ <%= target %>" in version <%= version %>
 */

namespace sensor\server;

use sensor\DB;
use sensor\Define;

/**
 * It stores the sensor data.
 */
class Storage_Sensor
{
    /**
     * @var \sensor\Application
     */
    private $app;

    /**
     * @param \sensor\Application $app
     */
    public function __construct($app)
    {
        $this->app = $app;
    }

    public function save($sensor)
    {
        $data = $this->prepareSensorData($sensor);

        /** @var \PDO $pdo */
        $pdo = DB::openDatabase($this->app);

        // update the current temperature and humidity
        $this->updateSensor($pdo, $data);

        // insert the sensor data
        $id = $this->insertSensor($pdo, $data);

        $result = array(
            'status' => Define::RESULT_OKAY,
            'id' => $id
        );
        $this->app->sendResult($result);
    }

    /**
     * @param \PDO $pdo
     * @param $sensor
     */
    private function updateSensor($pdo, $sensor)
    {
        $stmt = $pdo->prepare('UPDATE `sensor-currents` SET
            `temperature` = :temperature,
            `humidity` = :humidity,
            `date` = :date
            WHERE `group_id` = :groupId AND `name_id` = :nameId AND `date` < :date'
        );
        $stmt->execute($sensor);
    }

    /**
     * @param \PDO $pdo
     * @param $sensor
     * @return mixed
     */
    private function insertSensor($pdo, $sensor)
    {
        $stmt = $pdo->prepare('INSERT INTO `sensors` SET
            `group_id` = :groupId,
            `name_id` = :nameId,
            `temperature` = :temperature,
            `humidity` = :humidity,
            `date` = :date'
        );
        $stmt->execute($sensor);

        # prepare the result: the inserted id
        return $pdo->lastInsertId();
    }

    private function prepareSensorData($sensor)
    {
        $data = array();
        // copy all properties to the "data": except "group_id" and "name_id"!
        foreach ($sensor as $name => $value) {
            switch ($name) {
                case 'group_id':
                    $data['groupId'] = $value;
                    break;
                case 'name_id':
                    $data['nameId'] = $value;
                    break;
                default:
                    $data[$name] = $value;
            }
        }
        return $data;
    }
}

?>
