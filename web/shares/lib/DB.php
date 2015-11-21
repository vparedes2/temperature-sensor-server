<?php
/*
 * temperature-sensor-server - http://github.com/blueskyfish/temperature-sensor-server.git
 *
 * The MIT License (MIT)
 * Copyright (c) 2015 BlueSkyFish
 *
 * Distributed on "<%= datetime %> @ <%= target %>" in version <%= version %>
 */

namespace sensor;

class DB
{

    /**
     * Open a database connection
     *
     * @param \Slim\Slim $app
     * @return \PDO
     */
    public static function openDatabase($app)
    {
        $dsn = $app->config('database.dsn');
        $user = $app->config('database.user');
        $pass = $app->config('database.pass');
        return new \PDO($dsn, $user, $pass);
    }

}

?>
