<?php
/*
 * temperature-sensor-server - http://github.com/blueskyfish/temperature-sensor-server.git
 *
 * The MIT License (MIT)
 * Copyright (c) 2015 BlueSkyFish
 *
 * Distributed on "<%= datetime %> @ <%= target %>" in version <%= version %>
 */

namespace sensor\viewer;

require_once('lib/Hash_Service.php');

use sensor\DB;
use sensor\Define;
use sensor\HashService;

use Hashids\Hashids;

class SensorProvider
{
    /**
     * @var \sensor\Application
     */
    private $app;

    /**
     * SensorProvider constructor.
     * @param \sensor\Application $app
     */
    public function __construct($app)
    {
        $this->app = $app;
    }

    public function sendInfo()
    {
        // $hashKey = $this->app->getAuthToken();

        $sensorList = array();

        $sql = 'SELECT
            sn.group_id, sn.name_id, sn.title, sn.description, sn.icon,
            sc.temperature, sc.humidity, sc.date
          FROM `sensor-names` AS sn
            INNER JOIN `sensor-currents` AS sc ON sn.group_id = sc.group_id AND sn.name_id = sc.name_id';

        $pdo = DB::openDatabase($this->app);
        $stmt = $pdo->prepare($sql);
        $stmt->execute();
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            $id = HashService::encode($row['group_id'], $row['name_id']);
            $sensorList[] = array(
                'id' => $id,
                'title' => $row['title'],
                'description' => $row['description'],
                'icon' => $row['icon'],
                'temperature' => (int)$row['temperature'],
                'humidity' => (int)$row['humidity'],
                'date' => $row['date']
            );
        }

        // build the result object...
        $result = array(
            'status' => Define::RESULT_OKAY,
            'sensors' => $sensorList
        );

        $this->app->sendResult($result);
    }
}

?>
