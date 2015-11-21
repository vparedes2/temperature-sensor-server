/*
 * temperature-monitor - http://github.com/blueskyfish/temperature-monitor.git
 *
 * The MIT License (MIT)
 * Copyright (c) 2015 BlueSkyFish
 *
 * Purpose:
 * For distributing.
 */

'use strict';

var
  path = require('path');

var
  del = require('del'),
  dateformat = require('dateformat'),
  ejs = require('gulp-ejs'),
  gulp = require('gulp'),
  minimist = require('minimist'),
  rename = require('gulp-rename');

var
  pkg = require('./package.json'),
  params = minimist(process.argv.slice(2)),
  target = params.target || '',

// The name of the config file for the distribution
  configFile = 'shares/config/' + target + '.config.php';

var
  model = {
    target: target,
    datetime: dateformat(new Date(), 'yyyy-mm-dd HH:MM:ss'),
    version: pkg.version
  },
  settings = {
    ext: '.php'
  };


gulp.task('clean', function (done) {
  del(['dist'], function (err, paths) {
    done();
  });
});

gulp.task('check-target', ['clean'], function () {
  if (target === '') {
    console.log('');
    console.log('missing parameter "--target=name"');
    console.log('cancel!!');
    console.log('');
    process.exit(1);
  }
});

gulp.task('config-file', ['clean'], function () {
  return gulp.src(configFile)
    .pipe(ejs(model, settings))
    .pipe(rename('config.php'))
    .pipe(gulp.dest('dist/shares/config'));
});

function taskCopyHtAccess(rootPath) {
  return gulp.src(path.join(rootPath, '.htaccess'))
    .pipe(ejs(model, { ext: ''}))
    .pipe(gulp.dest(path.join('dist', rootPath)));
}

function taskCopyIndex(rootPath) {
  return gulp.src(path.join(rootPath, 'index.php'))
    .pipe(ejs(model, settings))
    .pipe(gulp.dest(path.join('dist', rootPath)));
}

function taskCopyLibrary(rootPath) {
  return gulp.src(path.join(rootPath, 'lib/*.php'))
    .pipe(ejs(model, settings))
    .pipe(gulp.dest(path.join('dist', rootPath, 'lib')));
}

gulp.task('copy-server-htaccess', ['clean'], function () {
  return taskCopyHtAccess('server');
});

gulp.task('copy-viewer-htaccess', ['clean'], function () {
  return taskCopyHtAccess('viewer');
});

gulp.task('copy-server-index', ['clean'], function () {
  return taskCopyIndex('server');
});

gulp.task('copy-viewer-index', ['clean'], function () {
  return taskCopyIndex('viewer');
});

gulp.task('copy-server-library', ['clean'], function () {
  return taskCopyLibrary('server');
});

gulp.task('copy-viewer-library', ['clean'], function () {
  return taskCopyLibrary('viewer');
});

gulp.task('copy-libraries', ['clean', 'copy-libaries-htaccess', 'copy-hasher'], function () {
  return gulp.src(['shares/lib/*.php'])
    .pipe(ejs(model, settings))
    .pipe(gulp.dest('dist/shares/lib'));
});

gulp.task('copy-libaries-htaccess', ['clean'], function () {
  return gulp.src(['shares/.htaccess'])
    .pipe(ejs(model, { ext: ''}))
    .pipe(gulp.dest('dist/shares'));
});

gulp.task('copy-hasher', ['clean'], function () {
  return gulp.src(['shares/Hashids/**/*.php'])
    .pipe(ejs(model, settings))
    .pipe(gulp.dest('dist/shares/Hashids'));
});

gulp.task('copy-slim', ['clean'], function () {
  return gulp.src('shares/Slim/**/**')
    .pipe(gulp.dest('dist/shares/Slim'));
});

gulp.task('copy-index', ['clean'], function () {
  return gulp.src('index.html')
    .pipe(ejs(model, { ext: '.html'}))
    .pipe(gulp.dest('dist'));
});

gulp.task('copy-all', [
  'config-file',
  'copy-server-index',
  'copy-server-htaccess',
  'copy-server-library',
  'copy-viewer-index',
  'copy-viewer-htaccess',
  'copy-viewer-library',
  'copy-libraries',
  'copy-slim',
  'copy-index'
]);

/**
 * Build a distribution
 */
gulp.task('build', [
  'check-target',
  'copy-all'
]);

/**
 * Default Task (help)
 */
gulp.task('default', function () {
  console.log('');
  console.log('Sensor Server');
  console.log('');
  console.log('Usage:');
  console.log('   gulp build --target=name   create a distribution with the config file of the target');
  console.log('   gulp clean                 delete the distribution folder');
});
