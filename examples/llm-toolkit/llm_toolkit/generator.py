def generate_tool(func, framework):
    print(f"Генерация инструмента для {framework}:")
    if framework == "AI SDK":
        # AI SDK использует tool()
        print(f"  - tool()")
    elif framework == "MCP-сервер":
        # MCP-сервер использует registerTool()
        print(f"  - registerTool()")
    elif framework == "Genkit":
        # Genkit использует defineTool()
        print(f"  - defineTool()")
    else:
        raise ValueError(f"Неизвестный фреймворк: {framework}")