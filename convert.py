""" Convert Chinese File Encoding To utf8
Returns:
    None
"""
import sys


def load_file(file_name: str, encoding="cp950") -> list:
    lines = []
    with open(file_name, 'r', encoding=encoding) as handler:
        for line in handler:
            lines.append(line)
    return lines


def write_file(file_name: str, text: str):
    save_name = f"new_{file_name}"
    with open(save_name, "w+", encoding="utf8") as handler:
        handler.write(text)


def main() -> None:
    file_names = sys.argv[1:]
    for file_name in file_names:
        lines = load_file(file_name, encoding="cp950")
        encoded_text = ''.join(lines)
        write_file(file_name, encoded_text)


if __name__ == '__main__':
    # fn_list = [ "BSR_35EXCD.zip"
    # ]

    # 如果 cp950無法的話可以試試看 "big5hkscs"
    # https://docs.python.org/2.4/lib/standard-encodings.html
    main()
