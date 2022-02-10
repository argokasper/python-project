# 1. liige tiimis
def read_file(file_name: str):
    """Opens file and reads all lines

    Args:
        file_name (str): Path to a file

    Returns:
        list: Returns a list of lines in a file. if file does not exist,
        then returns an empty list.
    """
    try:
        file = open(file_name, 'r', encoding='utf-8')
        file_lines = file.readlines()
        file.close()

        return file_lines
    except FileNotFoundError:
        return []


# 2. liige tiimis
def write_file(file_name: str, line: str, headers = []):
    """Kirjutab midagi faili
    Args:
        file_name (str): Path to a file
        line (str): [description]
    """
    try:
        file = open(file_name, 'x', encoding='utf-8') # x = uue faili loomine
        if len(headers) > 0: # kui on header'id kaasa antud, siis loome esimeseks reaks pealkirjade rea
            tmp_headers = []
            for header in headers:
                tmp_headers.append(f'"{header}"')
            file.write(','.join(tmp_headers) + '\n')
    except:
        # except plokki minnakse vaid siis kui fail on juba olemas
        # ehk ei saa teist korda sama faili luua
        file = open(file_name, 'a') # a = faili lisamine

    file.write(line + '\n')
    file.close()


def write_to_csv(file_name: str, data: dict, headers = [], delimiter = ','):
    """Writes one line into a CSV file. Default delimiter is comma(,).
    Args:
        file_name (str): Path to a CSV file. It is created if it doesn't exist
        data (dict): Key-value data for inserting 1 row into a file
        headers (list): List of string containing header names for a CSV file
        delimiter (str, optional): CSV file data delimiter. Defaults to ','.
    """

    line = ''
    data_count = len(data)
    for index, (key, value) in enumerate(data.items()):
        line +=  "\"" + str(value) + "\""

        if index < data_count - 1:
            line += delimiter
            # line = line + delimiter

    write_file(file_name, line, headers)

def read_csv(file_name: str, has_headers = False, delimiter = ','):
    """Reads a CSV file and exports its data into a dictionary list.
    Args:
        file_name (str): Path to a CSV file
        has_headers (bool): Boolean for indicating file reader should also look for CSV headers. Headers are only on the first line of the file.
        delimiter (str, optional): CSV file data delimiter. Defaults to ','.
    Returns:
        list: List of dictionaries wher each dictionary represents a single line in a CSV
    """
    lines = read_file(file_name) # list, kus iga element on üks rida ja rida on komaga eraldatud data

    data_headers = []

    if has_headers:
        if len(lines) == 1:
            return []
        for line in lines:
            data_headers = parse_csv_line(line, delimiter, retrieve_headers = True)
            break

        lines = lines[1:]

    parsed_lines = []
    for line in lines:
        parsed_lines.append(parse_csv_line(line, delimiter, data_headers))

    return parsed_lines


def parse_csv_line(line: str, delimiter: str, headers = [], retrieve_headers = False):
    """Parses a single CSV document line

    Args:
        line (str): [description]
        delimiter (str): [description]
        headers (list, optional): [description]. Defaults to [].
        retrieve_headers (bool, optional): [description]. Defaults to False.

    Returns:
        list: [description]
    """
    open_quotes = False
    tmp_phrase = ''
    if retrieve_headers:
        tmp_data = []
    else:
        tmp_data = {}

    data_counter = 0

    for letter in line:
        if open_quotes == False and letter == '"': # if letter == "\"": /- ei tohi
            open_quotes = True
            continue

        if open_quotes == True:
            if letter == '"':
                open_quotes = False
                continue

            tmp_phrase += letter
        elif open_quotes == False and (letter == delimiter or letter == '\n'):
            # handlime tmp_phrase
            try:
                key = headers[data_counter] # Kui data_counter == 2
            except:
                key = data_counter

            if retrieve_headers:
                tmp_data.append(tmp_phrase.strip())
            else:
                tmp_data[key] = tmp_phrase.strip() # võtame eest ja lõpust tühikud ära

            tmp_phrase = ''
            data_counter += 1
            continue

    return tmp_data
