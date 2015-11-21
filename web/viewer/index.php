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

set_include_path('.:../shares');

require('Slim/Slim.php');

require('config/config.php');

require('lib/DB.php');
require('lib/Define.php');

require('lib/Application.php');

require_once('lib/Sensor_Provider.php');

use sensor\Application;
use sensor\Define;
use sensor\config\Config;


// ----------------------------------------------------------------------------

$app = Config::configure(new Application());

// Application Name
$app->setName('sensor-viewer');


//
// Rest Action GET: /viewer/hello
//
$app->get('/hello', function () use ($app) {
    $result = array(
        'status' => Define::RESULT_OKAY,
        'message' => 'Hello World, I am the viewer',
        'target' => '<%= target %>',
        'version' => '<%= version %>'
    );
    $app->sendResult($result);
});

//
// Rest Action GET: /viewer/info
//
$app->get('/info', function () use ($app) {
    $provider = new SensorProvider($app);
    $provider->sendInfo();
});


//
// Rest Action GET: /viewer/sensor/:id
//
$app->get('/sensor/:id', function ($id) use ($app) {
    $provider = new SensorProvider($app);
    $provider->sendSensor($id);
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
