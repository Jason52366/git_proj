import sys

def load_file(_fn, encoding="cp950"):
  _msg_lst = list()
  with open(_fn, 'r', encoding=encoding) as _f:
    for l in _f:
      _msg_lst.append(l)
  return _msg_lst

if __name__ == '__main__':
  fn_list = sys.argv[1:]
  # fn_list = [ "BSR_35EXCD.zip"
  # ]

  # 如果 cp950無法的話可以試試看 "big5hkscs"
  # https://docs.python.org/2.4/lib/standard-encodings.html

  for fn in fn_list:
    msg_list = load_file(fn, encoding="cp950")
    with open("new_{}".format(fn), "w+") as new_f:
      new_f.write(''.join(msg_list))
