import codecs
import sys


b = "CODCOD".encode("utf8")
codecs.encode(b, encoding="bz2")


def compare_encodings(my_string, encoding_list):
    min_coding = sys.maxint
    min_coding_name = ''
    for code in encoding_list:
        my_bytes = my_string.encode('utf8')
        code_len = len(codecs.encode(my_bytes, encoding=code))
        if code_len < min_coding:
            min_coding = code_len
            min_coding_name = code
    print(min_coding_name)


compare_encodings("a", ["zlib", "bz2", "base64"])
compare_encodings("a" * 10, ["zlib", "bz2", "base64"])
compare_encodings("a" * 100, ["zlib", "bz2", "base64"])
compare_encodings("a" * 1000, ["zlib", "bz2", "base64"])
compare_encodings("a" * 10000, ["zlib", "bz2", "base64"])
compare_encodings("a" * 100000, ["zlib", "bz2", "base64"])
