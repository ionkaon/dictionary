#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTHOR : Electric Sheep
VERSION : v2021.11.12
"""
import re, sys, getopt

def phin2ipa(s):
    """
    將定海吳拼轉換爲 IPA
    https://github.com/ionkaon/dictionary/blob/master/音系與拼音方案.md#定海
    """
    s = s.lower()
    # 轉換聲調
    tone = ["53", "22", "35", "24", "44", "13", "5", "12"]
    for j in range(8):
        s = re.sub(r"(?<=[a-z])"+str(j+1)+r"\b", tone[j], s)
    # 轉換聲母
    s = re.sub(r"\b([ptck]|ts)h", r"\1ʰ", s)
    s = re.sub(r"\bc", r"tɕ", s)
    s = re.sub(r"\bj", r"dʑ", s)
    s = re.sub(r"\bgn", r"ȵ", s)
    s = re.sub(r"\bsh", r"ɕ", s)
    s = re.sub(r"\bzh", r"ʑ", s)
    s = re.sub(r"\bng", r"ŋ", s)
    s = re.sub(r"\bnk", r"ʔŋ", s)
    s = re.sub(r"\b([mnl])h", r"ʔ\1", s)
    s = re.sub(r"\bgh", r"ɦ", s)
    s = re.sub(r"\bg", r"ɡ", s)
    s = re.sub(r"\byi|\by(?=a|e)", r"ɦi", s)
    s = re.sub(r"\bwu|\bw(?=a|e|o)", r"ɦu", s)
    s = re.sub(r"\byu|\by(?=o)", r"ɦy", s)
    # 轉換韻母
    s = re.sub(r"(s|z|sʰ)yu", r"\1ʮ", s)
    s = re.sub(r"(s|z|sʰ)y", r"\1ɿ", s)
    s = re.sub(r"iu(?=n|q|\d)|i(?=o|ao)", r"y", s)
    s = re.sub(r"a[ou]", r"ɔ", s)
    s = re.sub(r"ae", r"ɛ", s)
    s = re.sub(r"oe", r"ø", s)
    s = re.sub(r"ieu", r"iu", s)
    s = re.sub(r"ien", r"ĩ", s)
    s = re.sub(r"(?<=[aɔuyø])n(?=\b|\d)", "\u0303", s)
    s = re.sub(r"ei", r"ai", s)
    s = re.sub(r"ou", r"au", s)
    s = re.sub(r"e(?=n)", r"ɐ", s)
    s = re.sub(r"y(?=q)", r"ya", s)
    s = re.sub(r"a(?=q)", r"ɐ", s)
    s = re.sub(r"i(?=q)", r"iə", s)
    s = re.sub(r"(?<=[^ʔ])n(?=\b|\d)", r"ŋ", s)
    s = re.sub(r"q(?=\b|\d)", r"ʔ", s)
    s = re.sub(r"er", r"əl", s)
    s = re.sub(r"\b(ʔ)?(m|n)(?=\b|\d)", r"\1\2̩", s)
    s = re.sub(r"\b(ʔ)?ŋ(?=\b|\d)", r"\1ŋ̍", s)
    # 聲調上標
    s = re.sub(r"1", r"¹", s)
    s = re.sub(r"2", r"²", s)
    s = re.sub(r"3", r"³", s)
    s = re.sub(r"4", r"⁴", s)
    s = re.sub(r"5", r"⁵", s)
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
  ./dinhe.py -i <file> -o <file> -f <option>

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

s = [eval(function)(i) for i in s]

with open(output_file, "w", encoding="utf-8") as f_output:
    [f_output.write(i) for i in s]
f_output.closed
