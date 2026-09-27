import os
import subprocess

def start_ssh_agent():
    """Запускает ssh-agent и добавляет ключи"""
    os.system("eval \"$(ssh-agent -s)\"")
    os.system("ssh-add ~/.ssh/id_rsa")

def run_container():
    """Запускает rootless Docker контейнер с ssh-agent"""
    user_id = "1000"  # Пример ID пользователя
    image_name = "your_image_name"
    subprocess.run([
        "docker", "run",
        "--user", user_id,
        "-e", "SSH_AUTH_SOCK=/tmp/ssh-agent.socket",
        "-v", "~/.ssh:/root/.ssh",
        image_name
    ])

def main():
    start_ssh_agent()
    run_container()

if __name__ == "__main__":
    main()