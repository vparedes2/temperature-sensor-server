<?php
/*
 * temperature-sensor-server - http://github.com/blueskyfish/temperature-sensor-server.git
 *
 * The MIT License (MIT)
 * Copyright (c) 2015 BlueSkyFish
 *
 * Distributed on "<%= datetime %> @ <%= target %>" in version <%= version %>
 */

namespace sensor\config;

//
// Config the application on depend the application mode
//
class Config
{
    /**
     * Setup the configuration for the application
     *
     * @param \sensor\Application $app
     * @return \sensor\Application
     */
    public static function configure($app)
    {

        # Configuration for the mode "development"
        $app->configureMode('development', function () use ($app) {
            $app->config(array(
                'debug' => true,
                'database.dsn' => 'mysql:dbname=XXXX;host=localhost;port=3306',
                'database.user' => 'dbUser',
                'database.pass' => 'dbPassword'
            ));
        });

        # Configuration for the mode "production"
        $app->configureMode('production', function () use ($app) {
            $app->config(array(
                'debug' => true,
                'database.dsn' => 'mysql:dbname=XXXXXX;host=localhost;port=3306',
                'database.user' => 'dbUser',
                'database.pass' => 'dbPassword'
            ));
        });

        // need more configuration modes?
        // insert here

        return $app;
    }
}

?>
