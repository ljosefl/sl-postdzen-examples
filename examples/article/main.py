import os
import subprocess

def install_required_tools():
    """
    安装必要的开发工具和软件。
    """
    tools = [
        "code",  # Visual Studio Code
        "git",   # Git
        "slack", # Slack
        "trello" # Trello
    ]
    for tool in tools:
        try:
            subprocess.run(["sudo", "apt-get", "install", "-y", tool], check=True)
            print(f"已安装 {tool}")
        except subprocess.CalledProcessError as e:
            print(f"安装 {tool} 失败: {e}")

def check_internet_connection():
    """
    检查网络连接。
    """
    try:
        result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("网络连接正常")
        else:
            print("网络连接失败")
    except Exception as e:
        print(f"检查网络连接失败: {e}")

def main():
    """
    主函数，用于设置开发环境。
    """
    print("开始设置开发环境...")
    install_required_tools()
    check_internet_connection()
    print("开发环境设置完成")

if __name__ == "__main__":
    main()