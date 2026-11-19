class AgentSitemap:
    def generate_sitemap(self, sections, output_file):
        """
        Генерирует карту сайта из разделов и сохраняет в файл.
        """
        with open(output_file, 'w', encoding='utf-8') as file:
            for section in sections:
                file.write(f"- {section}\n")