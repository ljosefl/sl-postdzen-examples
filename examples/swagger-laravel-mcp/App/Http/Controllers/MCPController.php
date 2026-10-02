<?php

namespace App\Http\Controllers;

use Laravel\MCP\MCP;

class MCPController extends Controller
{
    public function search(string $query)
    {
        return response()->json(MCP::search($query));
    }

    public function operationDetails(string $operationId)
    {
        return response()->json(MCP::operationDetails($operationId));
    }

    public function namedSchemas()
    {
        return response()->json(MCP::namedSchemas());
    }

    public function operationsByTag(string $tag)
    {
        return response()->json(MCP::operationsByTag($tag));
    }
}