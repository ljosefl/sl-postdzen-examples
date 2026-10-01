from llm_toolkit import tool
from llm_toolkit.generator import generate_tool

# Пример инструментов для разных фреймворков
@tool
def ai_sdk_tool():
    pass

@tool
def mcp_server_tool():
    pass

@tool
def genkit_tool():
    pass

if __name__ == "__main__":
    print("Генерация инструментов...")
    generate_tool(ai_sdk_tool, "AI SDK")
    generate_tool(mcp_server_tool, "MCP-сервер")
    generate_tool(genkit_tool, "Genkit")