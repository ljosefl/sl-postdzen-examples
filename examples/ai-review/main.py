import os
import subprocess
from git import Repo

def review_code(repo_path, commit_hash):
    """
    Обзор кода, сгенерированного ИИ, в указанной ветке и коммите.
    """
    repo = Repo(repo_path)
    if not repo.is_repo:
        raise ValueError("Путь не является репозиторием Git")

    print(f"Обзор кода в ветке {repo.active_branch} на коммит {commit_hash}...")

    # Проверка статуса коммита
    status = repo.git.status()
    if "nothing to commit" in status:
        print("Коммит не содержит изменений.")
        return

    # Просмотр изменений
    changes = repo.git.diff(commit_hash)
    print("Изменения в коде:")
    print(changes)

    # Проверка тестов
    test_result = subprocess.run(["pytest"], cwd=repo_path, capture_output=True)
    if test_result.returncode == 0:
        print("Тесты прошли успешно.")
    else:
        print("Тесты не прошли:")
        print(test_result.stderr.decode())

def main():
    repo_path = "/path/to/your/repo"
    commit_hash = "your_commit_hash"

    try:
        review_code(repo_path, commit_hash)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()