# Примеры кода к статьям

Рабочие примеры, которые сопровождают статьи каналов в Яндекс Дзене.
У каждой статьи с практической частью — своя папка: код можно склонировать,
запустить и потрогать руками, а не разглядывать скриншот.

---

## Как устроено

```
examples/
└── <название-статьи>/
    ├── main.py
    ├── requirements.txt
    └── README.md
```

Папка называется по теме материала, поэтому найти нужный пример просто: ссылка в
конце статьи ведёт прямо в неё.

## Как запустить пример

```bash
git clone https://github.com/ljosefl/sl-postdzen-examples.git
cd sl-postdzen-examples/examples/<папка-статьи>

pip install -r requirements.txt   # если файл есть
python main.py
```

Точка входа — первый файл в папке (обычно `main.py`). Если файлов несколько,
порядок запуска описан в `README.md` внутри папки.

## Что внутри примеров

- **законченный запускаемый пример** — а не фрагмент и не набор разрозненных команд;
- только реально существующие вызовы библиотек: ничего выдуманного, что «не заработает»;
- **без секретов, ключей и паролей** — такие примеры сюда не попадают;
- комментарии на русском, коротко и по делу;
- внешние зависимости перечислены отдельным файлом (`requirements.txt` или `package.json`);
- если для темы нужна внешняя служба, пример это явно оговаривает.

## Примеры

| Тема статьи | Файлы |
|---|---|
| [`ai-disrupt-pdlc-na-praktike-gde-ii-realn`](examples/ai-disrupt-pdlc-na-praktike-gde-ii-realn) | `README.md`, `example.py` |
| [`catboost-example`](examples/catboost-example) | `README.md`, `example.py` |
| [`example-agent`](examples/example-agent) | `README.md`, `example_agent.py`, `requirements.txt` |
| [`hotcold-mem-optimization`](examples/hotcold-mem-optimization) | `README.md`, `main.py` |
| [`idor-static-analyzer`](examples/idor-static-analyzer) | `README.md`, `example.py` |
| [`ii-agentu-zapretili-zapis-v-crm-crm-vse`](examples/ii-agentu-zapretili-zapis-v-crm-crm-vse) | `README.md`, `example.py` |
| [`kak-my-avtomatizirovali-kontrol-sborki-z`](examples/kak-my-avtomatizirovali-kontrol-sborki-z) | `README.md`, `accounting.py`, `camera.py`, `main.py`, `reporting.py` |
| [`kak-ya-sdelal-openclaw-ii-na-5000-sotrud`](examples/kak-ya-sdelal-openclaw-ii-na-5000-sotrud) | `README.md`, `example.py` |
| [`miga-cassandra-migration-example`](examples/miga-cassandra-migration-example) | `README.md`, `main.py`, `requirements.txt` |
| [`nativeaotrefactoring`](examples/nativeaotrefactoring) | `README.md`, `main.py` |
| [`pgvector-example`](examples/pgvector-example) | `README.md`, `example.py` |
| [`skrinshoty-zhgut-tokeny-headless-ne-zalo`](examples/skrinshoty-zhgut-tokeny-headless-ne-zalo) | `README.md`, `example.py` |
| [`vibcoding-firstcatastrophe`](examples/vibcoding-firstcatastrophe) | `README.md`, `example.py` |

## Обновления

Таблица примеров выше обновляется вместе с репозиторием: новая папка и строка в
списке появляются одновременно. Если нужного материала в списке нет — значит пример
к нему ещё не добавлен.

## Использование

Код можно свободно брать, менять и применять в своих проектах, в том числе
коммерческих — без указания источника. Если пример пригодился, будет приятно,
но это не требование.
