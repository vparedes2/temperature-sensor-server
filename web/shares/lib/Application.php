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

require_once('Slim/Slim.php');
require_once('Exception_Middleware.php');

use \Slim\Slim;


# Auto load the Slim classes.
Slim::registerAutoloader();


/**
 * Calculate the mode!
 *
 * @return string "production" or "deployment"
 */
function getMode()
{
    $version = '<%= version %>';
    return strpos($version, 'version') === false ? 'production' : 'development';
}

/**
 *
 */
class Application extends Slim
{

    /**
     * Defines the request header for the auth token.
     */
    const MONITORING_AUTH = 'x-temperature-sensor';

    private static $_INSTANCE;

    /**
     * @return Application
     */
    public static function getApplication()
    {
        return self::$_INSTANCE;
    }

    public function __construct()
    {
        parent::__construct(array(
            'mode' => getMode()
        ));
        self::$_INSTANCE = $this;
        # add the exception middleware
        $this->add(new Exception_Middleware());
    }

    public function sendResult($result, $statusCode = Define::HTTP_OKAY)
    {
        // may set the auth token in the response header
        $token = $this->getAuthToken();
        if (is_string($token) && strlen($token) > 0 && $token != '0000') {
            $this->response->headers->set(self::MONITORING_AUTH, $token);
        }

        $res = $this->response;
        $res->headers->set('Content-Type', 'application/json');
        if ($statusCode != Define::HTTP_OKAY) {
            $res->setStatus($statusCode);
        }
        $res->setBody(json_encode(self::prepare_to_json($result)));
    }

    public function getBodyJson()
    {
        $body = $this->request->getBody();
        return json_decode($body, true);
    }

    /**
     * Returns the auth token from the request headers. The name of the header field
     * must be "x-monitoring-auth". If the field is not exist, then it return "nothing".
     *
     * @return string
     */
    public function getAuthToken()
    {
        $token = $this->request->headers->get(self::MONITORING_AUTH);
        if (is_null($token)) {
            return '0000';
        }
        return $token;
    }

    public function getContextPath()
    {
        $scriptName = $_SERVER['SCRIPT_NAME'];
        return dirname($scriptName);
    }

    private static function prepare_to_json($items)
    {
        if (is_array($items)) {
            $temp = array();
            foreach ($items as $key => $value) {
                if (is_string($value)) {
                    $value = utf8_encode($value);
                } else if (is_array($value)) {
                    $value = self::prepare_to_json($value);
                }
                $temp[$key] = $value;
            }
            return $temp;
        }

        if (is_string($items)) {
            $items = utf8_encode($items);
        }
        return $items;
    }
}

?>
