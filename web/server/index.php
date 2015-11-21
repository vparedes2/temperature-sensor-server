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

set_include_path('.:../shares');

require('Slim/Slim.php');

require('config/config.php');

require('lib/DB.php');
require('lib/Define.php');

require('lib/Application.php');

require('lib/Storage_Sensor.php');

use sensor\Application;
use sensor\Define;
use sensor\config\Config;


// ----------------------------------------------------------------------------

/** @var \sensor\Application $app */
$app = Config::configure(new Application());

// Application Name
$app->setName('temperature-sensor-server');


//
// Rest Actor: GET /temo/server/hello
//
$app->get('/hello', function () use ($app) {
    $result = array(
        'status' => Define::RESULT_OKAY,
        'message' => 'Hello World, I am the server',
        'target' => '<%= target %>',
        'version' => '<%= version %>'
    );
    $app->sendResult($result);
});


//
// Rest Actor: POST /temo/server/upload
//
$app->post('/upload', function () use ($app) {
    $sensor = $app->getBodyJson();

    $storage = new Storage_Sensor($app);
    $storage->save($sensor);
});

//
// catch errors
//
$app->error(function (\Exception $e) use ($app) {
    $result = array(
        'status' => Define::RESULT_OKAY,
        'message' => $e->getMessage(),
        'code' => $e->getCode(),
        'file' => $e->getFile(),
        'line' => $e->getLine(),
        'trace' => $e->getTraceAsString()
    );
    $app->sendResult($result, 400);
});

//
// Execution
//
$app->run();

?>
