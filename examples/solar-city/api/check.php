<?php

header('Content-Type: application/json');
$apiKey = $_SERVER['HTTP_API_KEY'];

if ($apiKey == 'your_api_key') {
    echo json_encode(['response' => 'Вход разрешен']);
} else {
    echo json_encode(['response' => 'Доступ запрещен']);
}