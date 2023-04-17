# python3
# Danila Sinicins, 17. grupa, 221RDB323


def read_input():
    text_input = input()
    pattern = ""
    text = ""
    if "I" in text_input:
        pattern = input()
        text = input()
    elif "F" in text_input:
        f = open ("./tests/06","r")
        text_input = f.read()
        text_input = text_input.split("\n")
        pattern = text_input[0]
        text = text_input[1]
    pattern = pattern.strip()
    text = text.strip()
    return (pattern, text)


def print_occurrences(occs):
    print(' '.join(map(str, occs)))


def get_occurrences(pattern, text):
    ind = []

    for i in range(len(text)):
        if text[i] == pattern[0] and len(pattern)+i <= len(text):
            occurs = True
            for j in range(len(pattern)):
                if text[i+j] != pattern[j]:
                    occurs = False
            if occurs:
                ind.append(i)
    return ind

if __name__ == '__main__':
    pattern, text = read_input()
    occs = get_occurrences(pattern, text)
    print_occurrences(occs)
