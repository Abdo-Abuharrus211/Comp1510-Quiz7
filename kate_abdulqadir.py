def replace_all(input_file, output_file, search, replace):
    """
    Parse a text file and replace all instances of specified word with replacement

    :param input_file: string representing the file user wishes to edit including extension
    :param output_file: string representing the name of the modified file
    :param search: string for the keyword to be replaced
    :param replace: string for the replacement word
    :return: print number of times search argument has been replaced by replacement word
    """
    original_count = 0
    modified_count = 0
    filename_input = input_file
    filename_output = output_file

    with open(filename_input, 'r') as file_object:
        file_content = file_object.read()
    original_count = file_content.count(replace)

    modified_content = file_content.replace(search, replace)
    modified_count = modified_content.count(replace)

    with open(filename_output, 'w') as output:
        output.write(modified_content)
    filename_output.count(replace)

    return modified_count - original_count


def main():
    input_file = input("What's the input file's name?")
    output_name = input("What's the output file's name?")
    search_word = input("What's the search word?")
    replacement_word = input("What's the replacement word?")

    print(replace_all(input_file, output_name, search_word, replacement_word))


if __name__ == "__main__":
    main()
