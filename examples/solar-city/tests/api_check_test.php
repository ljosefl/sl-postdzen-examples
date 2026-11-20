<?php

use Illuminate\Foundation\Testing\WithoutMiddleware;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\DatabaseTransactions;

class ApiControllerTest extends TestCase
{
    use WithoutMiddleware;

    public function testAccessWithCorrectKey()
    {
        $_SERVER['HTTP_API_KEY'] = 'your_api_key';
        $response = Http::get('http://angamua.ru/api/check');

        $this->assertEquals(200, $response->status());
        $this->assertJson($response->body());
        $this->assertEquals(['response' => 'Вход разрешен'], json_decode($response->body(), true));
    }

    public function testAccessWithIncorrectKey()
    {
        $_SERVER['HTTP_API_KEY'] = 'wrong_api_key';
        $response = Http::get('http://angamua.ru/api/check');

        $this->assertEquals(403, $response->status());
        $this->assertJson($response->body());
        $this->assertEquals(['response' => 'Доступ запрещен'], json_decode($response->body(), true));
    }
}