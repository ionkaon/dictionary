#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTHOR : Electric Sheep
VERSION : v2021.11.12
"""
import re, sys, getopt

def phin2ipa(s):
    """
    將鎮海吳拼轉換爲 IPA
    https://github.com/ionkaon/dictionary/blob/master/音系與拼音方案.md#鎮海
    """
    s = [i.lower() for i in s]
    # 轉換聲調
    tone = ["53", "221", "35", "13", "44", "13", "5", "2"]
    for j in range(8):
        s = [re.sub(r"(?<=[a-z])"+str(j+1)+r"\b", tone[j], i) for i in s]
    # 轉換聲母
    s = [re.sub(r"\b([ptck]|ts)h", r"\1ʰ", i) for i in s]
    s = [re.sub(r"\bc", r"tɕ", i) for i in s]
    s = [re.sub(r"\bj", r"dʑ", i) for i in s]
    s = [re.sub(r"\bgn", r"ȵ", i) for i in s]
    s = [re.sub(r"\bkn", r"ʔȵ", i) for i in s]
    s = [re.sub(r"\bsh", r"ɕ", i) for i in s]
    s = [re.sub(r"\bzh", r"ʑ", i) for i in s]
    s = [re.sub(r"\bng", r"ŋ", i) for i in s]
    s = [re.sub(r"\bnk", r"ʔŋ", i) for i in s]
    s = [re.sub(r"\b([mnl])h", r"ʔ\1", i) for i in s]
    s = [re.sub(r"\bgh", r"ɦ", i) for i in s]
    s = [re.sub(r"\bg", r"ɡ", i) for i in s]
    s = [re.sub(r"\byi|\by(?=a|e)", r"ɦi", i) for i in s]
    s = [re.sub(r"\bwu|\bw(?=a|e|o)", r"ɦu", i) for i in s]
    s = [re.sub(r"\byu|\by(?=o)", r"ɦy", i) for i in s]
    s = [re.sub(r"(t?)s(ʰ?)(?=o\b|on|oq|oe|yu|aon)", r"\1ʃ\2", i) for i in s]
    s = [re.sub(r"(d?)z(?=o\b|on|oq|oe|yu|aon)", r"\1ʒ", i) for i in s]
    # 轉換韻母
    s = [re.sub(r"(ʃ|ʒ|ʃʰ)yu", r"\1ʯ", i) for i in s]
    s = [re.sub(r"(s|z|sʰ)y", r"\1ɿ", i) for i in s]
    s = [re.sub(r"iu|i(?=o|ao)", r"y", i) for i in s]
    s = [re.sub(r"a[ou]", r"ɔ", i) for i in s]
    s = [re.sub(r"iɔ", r"io", i) for i in s]
    s = [re.sub(r"ae", r"ɛ", i) for i in s]
    s = [re.sub(r"oe", r"ø", i) for i in s]
    s = [re.sub(r"ieu", r"iu", i) for i in s]
    s = [re.sub(r"ii", r"iɪ", i) for i in s]
    s = [re.sub(r"ei", r"ᴇɪ", i) for i in s]
    s = [re.sub(r"ou", r"aʊ", i) for i in s]
    s = [re.sub(r"e(?=n)", r"ə", i) for i in s]
    s = [re.sub(r"ʯ(?=n|q)", r"ø", i) for i in s]
    s = [re.sub(r"(i|y)(?=q)", r"\1e", i) for i in s]
    s = [re.sub(r"(?<=[aɔ])n(?=\b|\d)", r"̃", i) for i in s]
    s = [re.sub(r"(?<=[^ʔ])n(?=\b|\d)", r"ŋ", i) for i in s]
    s = [re.sub(r"q(?=\b|\d)", r"ʔ", i) for i in s]
    s = [re.sub(r"er", r"l̩", i) for i in s]
    s = [re.sub(r"\b(ʔ)?(m|n)(?=\b|\d)", r"\1\2̩", i) for i in s]
    s = [re.sub(r"\b(ʔ)?ŋ(?=\b|\d)", r"\1ŋ̍", i) for i in s]
    s = [re.sub(r"e(?!ʔ)", r"ᴇ", i) for i in s]
    # 聲調上標
    s = [re.sub(r"1", r"¹", i) for i in s]
    s = [re.sub(r"2", r"²", i) for i in s]
    s = [re.sub(r"3", r"³", i) for i in s]
    s = [re.sub(r"4", r"⁴", i) for i in s]
    s = [re.sub(r"5", r"⁵", i) for i in s]
    return s

opts, args = getopt.getopt(sys.argv[1:], "hi:o:f:")
for opt, arg in opts:
    if opt == "-i":
        input_file = arg
    elif opt == "-o":
        output_file = arg
    elif opt == "-f":
        function = arg
    elif opt == "-h":
        print(
"""
Usage:
  ./tsyunhe.py -i <file> -o <file> -f <option>

Options:
  -i <file>            input file
  -o <file>            output file
  -f <option>          fuction dealing with the file
  -h                   Display this information

These fuctions are avalible:
  phin2ipa             將吳拼轉換爲IPA
"""
)
        sys.exit()

with open(input_file, "r", encoding="utf-8") as f_input:
    s = f_input.readlines()
f_input.closed

s = eval(function)(s)

with open(output_file, "w", encoding="utf-8") as f_output:
    [f_output.write(i) for i in s]
f_output.closed
