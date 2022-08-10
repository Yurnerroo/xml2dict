def xml2dict(file: str) -> dict:
    """
    XML2DICT is a module, that parses XML file into Python dictionary.

    :param file: path to your XML file
    :return: file, parsed into python dictionary
    """
    dct = {}

    with open(file, "r") as f:
        f = f.read()
        formatted = f.split("\n")

        for row in formatted[1:-1]:
            row_stripped = row.lstrip()
            tag = ""

            for ch in row_stripped:
                if ch == ">":
                    tag += ch
                    break
                tag += ch

            closing_tag = tag[:1] + "/" + tag[1:]
            row_no_tags = row_stripped.replace(tag, "").replace(closing_tag, "")

            if closing_tag not in f and "//" not in closing_tag:
                raise AssertionError(f"{tag} tag is not closed.")

            if (closing_tag in row) and (tag[1:-1] not in dct.keys()):
                dct[tag[1:-1]] = row_no_tags
            elif (closing_tag in row) and (tag[1:-1] in dct.keys()):
                if isinstance(dct[tag[1:-1]], list):
                    dct[tag[1:-1]] = dct[tag[1:-1]] + [row_no_tags]
                elif not isinstance(dct[tag[1:-1]], list):
                    dct[tag[1:-1]] = [dct[tag[1:-1]]] + [row_no_tags]

    return dct


file_path = input("Please type path to your XML file: ")
print(xml2dict(file_path))
