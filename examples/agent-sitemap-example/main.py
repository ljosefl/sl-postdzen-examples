import os
from langchain.text_splitter import TextSplitter
from agent_sitemap import AgentSitemap

class CustomTextSplitter(TextSplitter):
    def split_text(self, text):
        # Простой текстовый разделитель для примера
        return text.split('\n')

def create_sitemap(input_file, output_file):
    """
    Создает карту сайта для ИИ-агента из входного файла Markdown.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    splitter = CustomTextSplitter()
    sections = splitter.split_text(content)

    sitemap = AgentSitemap()
    sitemap.generate_sitemap(sections, output_file)

if __name__ == "__main__":
    input_file = "test.md"
    output_file = "sitemap.txt"

    if not os.path.exists(input_file):
        print(f"Файл {input_file} не найден.")
    else:
        create_sitemap(input_file, output_file)
        print(f"Карта сайта сохранена в {output_file}")