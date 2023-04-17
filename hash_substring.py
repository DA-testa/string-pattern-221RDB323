# python3
# Danila Sinicins, 17. grupa, 221RDB323


def read_input():
    text_input = input()
    pattern = ""
    text = ""
    if "I" in input:
        pattern = input()
        text = input()
    elif "F" in text_input:
        f = open ("./tests/06","r")
        text_input = f.read()
        text_input = text_input.split("\n")
        pattern = text_input[0]
        text = text_input[1]

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
    pattern, text = read_input()
    output = get_occurrences(pattern, text)
    print_occurrences(output)
