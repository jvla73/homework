class WordsFinder:
    def __init__(self, *files):
        self.file_names = files


    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with open(filename, encoding='utf-8') as file:
                words = []
                for line in file:
                    cleaned_line = line.lower().replace(',', '').replace('.', '').replace(
                        '=', '').replace('!','').replace(
                        '?', '').replace(';', '').replace(':', '').replace(' - ', '')
                    words += cleaned_line.split()
                all_words[filename] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            index = words.index(word.lower())
            result[filename] = index + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            count = words.count(word.lower())
            result[filename] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего