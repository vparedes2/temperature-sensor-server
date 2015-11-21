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

require_once('Slim/Middleware.php');

use \Slim\Middleware;

/**
 * It catches an exception that thrown during the process.
 */
class Exception_Middleware extends Middleware
{
    public function call()
    {
        try {

            $this->next->call();

        } catch (\Exception $e) {
            $result = array(
                'status' => 'error',
                'message' => $e->getMessage(),
                'code' => $e->getCode(),
                'file' => $e->getFile(),
                'line' => $e->getLine(),
                'trace' => $e->getTraceAsString()
            );
            $this->getApplication()->sendResult($result, Define::HTTP_BAD_REQUEST);
        }
    }
}

?>
