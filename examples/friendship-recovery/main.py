import time

def open_conversation(partner):
    print(f"Начинаем открытый разговор с {partner}.")
    return True

def apologize(partner):
    print(f"Извиняемся перед {partner}.")
    return True

def set_common_goals(partner):
    print(f"Устанавливаем общие цели с {partner}.")
    return True

def discuss_feelings(partner):
    print(f"Обсуждаем чувства с {partner}.")
    return True

def regular_meetings(partner):
    print(f"Проводим регулярные встречи с {partner}.")
    return True

def test_project(partner):
    print(f"Запускаем тестовый проект с {partner}.")
    return True

def be_reliable(partner):
    print(f"Будем предсказуемыми и надежными для {partner}.")
    return True

def main():
    partner = "старый друг"
    print("Начинаем процесс восстановления отношений.")
    
    if not open_conversation(partner):
        print("Не удалось начать разговор.")
        return
    
    if not apologize(partner):
        print("Не удалось извиниться.")
        return
    
    if not set_common_goals(partner):
        print("Не удалось установить общие цели.")
        return
    
    if not discuss_feelings(partner):
        print("Не удалось обсудить чувства.")
        return
    
    if not regular_meetings(partner):
        print("Не удалось провести регулярные встречи.")
        return
    
    if not test_project(partner):
        print("Не удалось запустить тестовый проект.")
        return
    
    if not be_reliable(partner):
        print("Не удалось стать предсказуемыми и надежными.")
        return
    
    print("Отношения восстановлены!")

if __name__ == "__main__":
    main()