<?php

require __DIR__ . '/vendor/autoload.php';

use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\App;

/**
 * Запуск Laravel приложения
 */
$kernel = require __DIR__ . '/bootstrap/app.php';
$kernel->bootstrap();