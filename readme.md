
Temperature Sensor Server
=========================

> This is the rest server, written in PHP with the slim framework, collecting the sensor data.


Table of Content
----------------

* [Installation](#user-content-installation-on-server)
* [Database Schema](#user-content-database-schema)
* [License](#user-content-license)



Installation on Server
----------------------

There are some steps

### Configuration


* The application needs a config file.
* Under `app/config/` is the file `config.example.php`.
* Make a copy from the example config. The name of the config file must be the same as the target of the distribution.

```
$ cd app/config
$ cp config.example.php test.config.php
$ nano test.config.php
```


### Distribute

For the distribution on the server there is Gulp task. The first time, the dependencies of Gulp must be installed with `npm install`.

Open the terminal and enter:

```
$ gulp build --target=name
```

The parameter `target` is required. It is the name of the server.


### Setup the Rewrite rules

Change in the file `.htaccess` the **RewriteBase** value.

```
RewriteEngine On
RewriteBase /temo/

RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^ index.php [QSA,L]
```


### Copy on server

The destribution is in the folder `dist`. Copy this on the http server.


Database Schema
---------------

The sensor server application needs some MySQL database tables. Here is the database schema

![Sensor Server Database Schema](docs/database-schema.png)


License
-------

```
The MIT License (MIT)

Copyright (c) 2015 BlueSkyFish

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```