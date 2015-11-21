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

require_once('Hashids/HashGenerator.php');
require_once('Hashids/Hashids.php');

use Hashids\Hashids;

class HashService
{
    private static $_HashIds = null;

    public static function getInstance()
    {
        if (is_null(self::$_HashIds)) {
            self::$_HashIds = new Hashids('temperature-sensor-server is cool :-)');
        }
        return self::$_HashIds;
    }

    public static function encode()
    {
        $args = func_get_args();
        $hashIds = self::getInstance();
        return call_user_func_array(array($hashIds, 'encode'), $args);
    }

    public static function decode()
    {
        $args = func_get_args();
        $hashIds = self::getInstance();
        return call_user_func_array(array($hashIds, 'decode'), $args);
    }

    public static function encodeHex($hex)
    {
        $hashIds = self::getInstance();
        return $hashIds->encode_hex($hex);
    }

    public static function decodeHex($hex)
    {
        $hashIds = self::getInstance();
        return $hashIds->decode_hex($hex);
    }
}

?>
