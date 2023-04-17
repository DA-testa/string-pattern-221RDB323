# python3
# Danila Sinicins, 17. grupa, 221RDB323


def read_input():
    text_input = input("Input: ")
    pattern = ""
    text = ""
    if "I" in input:
        pattern = input("Pattern: ")
        text = input("Text: ")
    elif "F" in text_input:
        f = open ("./tests/06","r")
        text_input = f.read()
        input_array = text_input.split("\n")
        pattern = input_array[0]
        text = input_array[1]

    return (pattern.strip(), text.strip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    ind = []

    for i in range(text):
        if text[i] == pattern and len(pattern)+i <= len(text):
            occurs = True
            for j in range(len(pattern)):
                if text[i+j] != pattern[j]:
                    occurs = False
            if occurs:
                ind.append(i)

    return ind

if __name__ == '__main__':
    patern, text = read_input()
    output = get_occurrences(patern, text)
    print_occurrences(output)
