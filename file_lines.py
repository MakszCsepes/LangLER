
DELIMITER = '-'


def get_specific_line_from_file(filename, line_number, lines_to_elude=[]):
    with open(filename) as file:
        lines_list = file.readlines()

        if line_number > len(lines_list):
            return

        if len(lines_to_elude) != 0:
            if line_number in lines_to_elude:
                return

        if line_number < 1:
            print(line_number)
            return

        # because of a list starts with "0" and
        # we're trying literally to take a line
        # there should be -1
        return lines_list[line_number - 1]


def write_into_file(filename, index, data):
    f = open(filename, "r", encoding="utf-8")
    contents = f.readlines()
    f.close()

    contents.insert(index - 1, data + "\n")

    f = open(filename, "w", encoding="utf-8")
    f.writelines(contents)
    f.close()
# write_into_file(filename, index, "hello")


# LINES

def get_word_from_line(line):
    return line.split(DELIMITER, 2)[0]


def get_translation_from_line(line, char_to_replace=[]):
    translation = line.split(DELIMITER, 2)[1]

    for i in char_to_replace:
        translation = translation.replace(i, ' ')
    return translation


get_translation_from_line("4-4;\n", ';')

def get_number_of_lines_in_file(filename):
    with open(filename, 'r') as f:
        lines = len(f.readlines())

    return lines


def get_word(cur_line):
    if len(cur_line) != 0:
        origin_word = get_word_from_line(cur_line)

        return origin_word