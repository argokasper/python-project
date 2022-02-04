
# 1. liige tiimis
def read_file(file_name):
    file = open(file_name, 'r')
    file_lines = file.readlines()
    file.close()

    return file_lines


# 2. liige tiimis
def write_file(file_name, line):
    try:
        file = open(file_name, 'x') # x = uue faili loomine
    except:
        # except plokki minnakse vaid siis kui fail on juba olemas
        # ehk ei saa teist korda sama faili luua
        file = open(file_name, 'a') # a = faili lisamine

    file.write(line + "\n")
    file.close()


def write_to_csv(file_name, data, delimiter = ','):
    line = ''
    data_count = len(data)
    for index, (key, value) in enumerate(data.items()):
        line +=  "\"" + str(value) + "\""

        if index < data_count - 1:
            line += delimiter
            # line = line + delimiter

    write_file(file_name, line)

def read_csv(file_name, delimiter = ','):
    lines = read_file(file_name) # list, kus iga element on üks rida ja rida on komaga eraldatud data

    #dict koosneb: name, text, ......
    data_headers = ['name', 'text']

    parsed_lines = []
    for line in lines:
        open_quotes = False
        tmp_phrase = ''
        tmp_data = {'name': '', 'text': ''}
        data_counter = 0
        line_length = len(line)
        for index, letter in enumerate(line):
            # print(letter)
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
                    key = data_headers[data_counter] # Kui data_counter == 2
                except:
                    key = data_counter

                tmp_data[key] = tmp_phrase.strip() # võtame eest ja lõpust tühikud ära
                tmp_phrase = ''
                data_counter += 1
                continue


        parsed_lines.append(tmp_data)

    return parsed_lines


