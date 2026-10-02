<?php

use Illuminate\Support\Facades\Route;
use Laravel\MCP\MCP;

Route::get('/search/{query}', [App\Http\Controllers\MCPController::class, 'search']);
Route::get('/operation/{operationId}', [App\Http\Controllers\MCPController::class, 'operationDetails']);
Route::get('/schemas', [App\Http\Controllers\MCPController::class, 'namedSchemas']);
Route::get('/operations/{tag}', [App\Http\Controllers\MCPController::class, 'operationsByTag']);

MCP::routes();