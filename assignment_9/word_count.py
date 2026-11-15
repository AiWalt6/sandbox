import os


def main():
    filename = input('Enter the name of the input file: ').strip()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            words = input_file.read().split()
    except OSError as error:
        print(f'Error reading the input file: {error}')
        return
    except UnicodeError as error:
        print(f'Error: The input file must contain UTF-8 text. {error}')
        return

    # Preserve capitalization and punctuation, as in the assignment sample.
    word_counts = {}
    for word in set(words):
        word_counts[word] = 0
    for word in words:
        word_counts[word] += 1

    print(f'{"Word":<25}Occurrences')
    print('-' * 40)
    for word in sorted(word_counts.keys()):
        print(f'{word:<25}{word_counts[word]}')
    if not words:
        print('The input file contains no words.')


if __name__ == '__main__':
    main()
