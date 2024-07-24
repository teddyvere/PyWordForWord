class FileProcessor:
    def __init__(self):
        testdata = '/Users/teddy/Documents/GitHub/Week4/PyWordForWord/testdata/testdata2.txt'
        self.testdata = testdata
    def print_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")

    def wc(self, filename):
        line_count = 0
        word_count = 0
        char_count = 0
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line_count += 1
                    words = line.strip().split()
                    char_count += len(line) + len(words) - 1  # subtracting 1 for spaces in between words
                    word_count += len(words)
        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
            return 0
        return (line_count, word_count, char_count)

    def word_frequency(self, filename):
        word_dict = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    words = line.strip().split()
                    for word in words:
                        word = word.lower()  # Optionally normalize to lower case
                        if word in word_dict:
                            word_dict[word] += 1
                        else:
                            word_dict[word] = 1
        except FileNotFoundError:
            print(f"\nThe file '{filename}' was not found.")
            return {}
        return word_dict

    def letter_frequency(self, filename):
        letter_dict = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    for char in line.strip():
                        if char.isalpha():
                            char = char.lower()  # Optionally normalize to lower case
                            if char in letter_dict:
                                letter_dict[char] += 1
                            else:
                                letter_dict[char] = 1
        except FileNotFoundError:
            print(f"\nThe file '{filename}' was not found.")
            return {}
        return letter_dict

    def frequency_word(self, word, testdata):
        word_dict = self.word_frequency(testdata)
        if word in word_dict:
            return word_dict[word]
        else:
            return 0

# Example usage of the class
if __name__ == "__main__":
    processor = FileProcessor()
    processor.print_file('testdata/testdata2.txt')
    print(processor.wc('testdata/testdata2.txt'))
    print(processor.word_frequency('testdata/testdata2.txt'))
    print(processor.letter_frequency('testdata/testdata2.txt'))
    print(processor.frequency_word('and', FileProcessor().testdata))
