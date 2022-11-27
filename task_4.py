import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=None, new_line=None):
    ...  # TODO реализовать конвертер из csv в json
    if delimiter is None:
        delimiter = ","
    if new_line is None:
        new_line = "\n"
    with open(filename) as f:
        matrix = []
        for i, l in enumerate(f):
            fields = l.strip(new_line).split(delimiter)
            if i == 0:
                heads = fields
                continue

            matrix.append({})

            for с, _ in enumerate(heads):
                matrix[-1][heads[с]] = fields[с]
    return matrix


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))