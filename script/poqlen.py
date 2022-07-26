#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTHOR : Shin Zoqchiuq
VERSION : v2021.11.12
"""
import re, sys, getopt

def phin2ipa(s):
    """
    將北侖吳拼轉換爲 IPA
    https://github.com/ionkaon/dictionary/blob/master/音系與拼音方案.md#北侖
    """
    s = s.lower()
    # 轉換聲調
    tone = ["51", "22", "34", "13", "44", "13", "5", "23"]
    for j in range(8):
        s = re.sub(r"(?<=[a-z])"+str(j+1)+r"\b", tone[j], s)
    # 轉換聲母
    s = re.sub(r"\b([ptck]|ts)h", r"\1ʰ", s)
    s = re.sub(r"\bc", r"tɕ", s)
    s = re.sub(r"\bj", r"dʑ", s)
    s = re.sub(r"\bgn", r"ȵ", s)
    s = re.sub(r"\bkn", r"ʔȵ", s)
    s = re.sub(r"\bsh", r"ɕ", s)
    s = re.sub(r"\bzh", r"ʑ", s)
    s = re.sub(r"\bng", r"ŋ", s)
    s = re.sub(r"\bnk", r"ʔŋ", s)
    s = re.sub(r"\b([mnlŋ])h", r"ʔ\1", s)
    s = re.sub(r"\bgh", r"ɦ", s)
    s = re.sub(r"\bg", r"ɡ", s)
    s = re.sub(r"\byi|\by(?=a|e)", r"ɦi", s)
    s = re.sub(r"\bwu|\bw(?=a|e|o)", r"ɦu", s)
    s = re.sub(r"\byu|\by(?=o)", r"ɦy", s)
    # 轉換韻母
    s = re.sub(r"(s|z|sʰ)yu", r"\1ʮ", s)
    s = re.sub(r"(s|z|sʰ)y", r"\1ɿ", s)
    s = re.sub(r"iu|i(?=o|ao)", r"y", s)
    s = re.sub(r"a[ou]", r"ɔ", s)
    s = re.sub(r"iɔ", r"io", s)
    s = re.sub(r"ae", r"ɛ", s)
    s = re.sub(r"ieu", r"iu", s)
    s = re.sub(r"ei", r"ai", s)
    s = re.sub(r"ou", r"au", s)
    s = re.sub(r"eu", r"øy", s)
    s = re.sub(r"e(?=n)", r"ə", s)
    s = re.sub(r"a(?=q)", r"a", s)
    s = re.sub(r"i(?=q)", r"ie", s)
    s = re.sub(r"(?<=[aɔ])n(?=\b|\d)", r"̃", s)
    s = re.sub(r"(?<=[^ʔ])n(?=\b|\d)", r"ŋ", s)
    s = re.sub(r"q(?=\b|\d)", r"ʔ", s)
    s = re.sub(r"er", r"l̩", s)
    s = re.sub(r"\b(ʔ)?(m|n)(?=\b|\d)", r"\1\2̩", s)
    s = re.sub(r"\b(ʔ)?ŋ(?=\b|\d)", r"\1ŋ̍", s)
    # 聲調上標
    s = re.sub(r"1", r"¹", s)
    s = re.sub(r"2", r"²", s)
    s = re.sub(r"3", r"³", s)
    s = re.sub(r"4", r"⁴", s)
    s = re.sub(r"5", r"⁵", s)
    return s

def ipa2phin(s):
    "將北侖話 IPA 轉換爲學堂式吳拼"
    # 聲調上標
    s = re.sub(r"¹", r"1", s)
    s = re.sub(r"²", r"2", s)
    s = re.sub(r"³", r"3", s)
    s = re.sub(r"⁴", r"4", s)
    s = re.sub(r"⁵", r"5", s)
    # 轉換聲調
    tone = ["51", "22", "34", "", "44", "13", "5", "23"]
    for j in [6, 0, 1, 2, 4, 5, 7]:
        s = re.sub(r"(?<!\d)"+tone[j]+r"\b", str(j+1), s)
    # 轉換韻母
    s = re.sub(r"\bl(?=\b|\d)", r"er", s)
    s = re.sub(r"[̩̍]", r"", s)
    s = re.sub(r"\b([mnŋ])(?=\b|\d)", r"\1", s)
    s = re.sub(r"ʔ(?=\b|\d)", r"q", s)
    s = re.sub(r"(?<!\b)ŋ(?=\b|\d)|̃", r"n", s)
    s = re.sub(r"(i|y)e(?=q)", r"\1", s)
    s = re.sub(r"ə(?=n)", r"e", s)
    s = re.sub(r"ai", r"ei", s)
    s = re.sub(r"au", r"ou", s)
    s = re.sub(r"øy", r"eu", s)
    s = re.sub(r"iu", r"ieu", s)
    s = re.sub(r"ɛ", r"ae", s)
    s = re.sub(r"io", r"iɔ", s)
    s = re.sub(r"ɔ", r"au", s)
    s = re.sub(r"aun", r"aon", s)
    s = re.sub(r"y(?=o|ao)", r"i", s)
    s = re.sub(r"y", r"iu", s)
    s = re.sub(r"ɿ", r"y", s)
    s = re.sub(r"ʮ", r"yu", s)
    # 轉換聲母
    s = re.sub(r"\btɕ", r"c", s)
    s = re.sub(r"\b([ptck]|ts)ʰ", r"\1h", s)
    s = re.sub(r"\bdʑ", r"j", s)
    s = re.sub(r"\bȵ", r"gn", s)
    s = re.sub(r"\bɕ", r"sh", s)
    s = re.sub(r"\bʑ", r"zh", s)
    s = re.sub(r"\bŋ", r"ng", s)
    s = re.sub(r"\bɦ", r"gh", s)
    s = re.sub(r"\bɡ", r"g", s)
    s = re.sub(r"\bghi(?=[aeo])", r"y", s)
    s = re.sub(r"\bghiu", r"yu", s)
    s = re.sub(r"\bghi", r"yi", s)
    s = re.sub(r"\bghu(?=a|e|o)", r"w", s)
    s = re.sub(r"\bghu", r"wu", s)
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
  ./poqlen.py -i <file> -o <file> -f <option>

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
