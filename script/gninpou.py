#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTHOR : Electric Sheep
VERSION : v2021.07.17
"""
import re, sys, getopt

def compat2gninpou(s):
    """
    將兼容格式轉爲寧波城區口音
    https://github.com/ionkaon/dictionary#兼容格式
    """
    s = re.sub(r"4", r"6", s)
    s = re.sub(r"(\w*)-(\w*)(\d)", r"\1\3", s)
    return s

def phin2ipa(s):
    "將學堂式的吳語拼音轉換爲 IPA"
    s = s.lower()
    # 轉換聲調
    tone = ["53", "24", "35", "213", "44", "213", "5", "12"]
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
    s = re.sub(r"\b([mnl])h", r"ʔ\1", s)
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
    s = re.sub(r"([btdnl]|tʰ)oe", r"\1ø", s)
    s = re.sub(r"oe", r"ʏ", s)
    s = re.sub(r"ieu", r"iʏ", s)
    s = re.sub(r"ei", r"ɐɪ", s)
    s = re.sub(r"ou", r"əu", s)
    s = re.sub(r"eu", r"œʏ", s)
    s = re.sub(r"e(?=n)", r"ə", s)
    s = re.sub(r"y(?=n|q)", r"yə", s)
    s = re.sub(r"ʮ(?=n)", r"ʮø", s)
    s = re.sub(r"a(?=q)", r"ɐ", s)
    s = re.sub(r"i(?=q)", r"iɪ", s)
    s = re.sub(r"ʮ(?=q)", r"ʮœ", s)
    s = re.sub(r"(?<=[aɔu])n(?=\b|\d)", "\u0303", s)
    s = re.sub(r"(?<=[^ʔ])n(?=\b|\d)", r"ŋ", s)
    s = re.sub(r"q(?=\b|\d)", r"ʔ", s)
    s = re.sub(r"er", r"əl", s)
    s = re.sub(r"\b(ʔ)?(m|n)(?=\b|\d)", r"\1\2"+"\u0329", s)
    s = re.sub(r"\b(ʔ)?ŋ(?=\b|\d)", r"\1ŋ"+"\u030d", s)
    # 聲調上標
    tonesymbol = ["¹", "²", "³", "⁴", "⁵"]
    for j in range(5):
        s = re.sub(str(j+1), tonesymbol[j], s)
    return s

def phinsplit(s):
    "將學堂式的吳語拼音分割爲聲母韻母和聲調"
    s = s.lower()
    s = re.sub(r"(?<=[a-z])([1-9])\b", r"\t\1", s)
    s = re.sub(r"\b(m|n|ng)\b", r"\1\t\1", s)
    s = re.sub(r"\ber\b", r"gh\ter", s)
    s = re.sub(r"\b(m|n)h\b", r"\1h\t\1", s)
    s = re.sub(r"\bnk\b", r"nk\tng", s)
    s = re.sub(r"\byi|\by(?=a|e)", r"ghi", s)
    s = re.sub(r"\bwu|\bw(?=a|e|o)", r"ghu", s)
    s = re.sub(r"\by(?=u)|\by(?=o)", r"ghi", s)
    s = re.sub(r"\b([yaeiou])(?!r)", r"∅\1", s)
    s = re.sub(r"(?<![aeiouy])([yaeiou])(?!r)", r"\t\1", s)
    return re.split(r"\t", s)

def ipa2phin(s):
    "將 IPA 轉換爲學堂式吳拼"
    # 聲調上標
    tonesymbol = ["¹", "²", "³", "⁴", "⁵"]
    for j in range(5):
        s = re.sub(tonesymbol[j], str(j+1), s)
    # 轉換聲調
    tone = ["53", "24", "35", "", "44", "213", "5", "12"]
    for j in [6, 0, 1, 2, 4, 5, 7]:
        s = re.sub(r"(?<!\d)"+tone[j]+r"\b", str(j+1), s)
    # 轉換韻母
    s = re.sub(r"əl", r"er", s)
    s = re.sub("[\u0329\u030d]", r"", s)
    s = re.sub(r"\bʔ([mn])(?=\b|\d)", r"\1h", s)
    s = re.sub(r"\bʔŋ(?=\b|\d)", r"nk", s)
    s = re.sub(r"ʔ(?=\b|\d)", r"q", s)
    s = re.sub(r"(?<!\b)ŋ(?=\b|\d)|"+"\u0303", r"n", s)
    s = re.sub(r"ʮ[œø](?=q|n)", r"ʮ", s)
    s = re.sub(r"iɪ(?=q)", r"i", s)
    s = re.sub(r"ɐ(?=q)", r"a", s)
    s = re.sub(r"yə(?=n|q)", r"y", s)
    s = re.sub(r"ə(?=n)", r"e", s)
    s = re.sub(r"ɐɪ", r"ei", s)
    s = re.sub(r"əu", r"ou", s)
    s = re.sub(r"œʏ", r"eu", s)
    s = re.sub(r"iʏ", r"ieu", s)
    s = re.sub(r"ʏ|ø", r"oe", s)
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
    s = re.sub(r"\bʔ([mnlŋȵ])", r"\1h", s)
    s = re.sub(r"\bȵ", r"gn", s)
    s = re.sub(r"\bgnh", r"kn", s)
    s = re.sub(r"\bɕ", r"sh", s)
    s = re.sub(r"\bʑ", r"zh", s)
    s = re.sub(r"\bŋ", r"ng", s)
    s = re.sub(r"\bngh", r"nk", s)
    s = re.sub(r"\bɦ", r"gh", s)
    s = re.sub(r"\bɡ", r"g", s)
    s = re.sub(r"\bghi(?=[aeo])", r"y", s)
    s = re.sub(r"\bghiu", r"yu", s)
    s = re.sub(r"\bghi", r"yi", s)
    s = re.sub(r"\bghu(?=a|e|o)", r"w", s)
    s = re.sub(r"\bghu", r"wu", s)
    return s

def ipasplit(s):
    "將 IPA 分割爲聲母韻母和聲調"
    # 聲調上標
    s = re.sub(r"¹", r"1", s)
    s = re.sub(r"²", r"2", s)
    s = re.sub(r"³", r"3", s)
    s = re.sub(r"⁴", r"4", s)
    s = re.sub(r"⁵", r"5", s)
    # 分割
    s = re.sub(r"\bəl", r"ɦəl", s)
    s = re.sub(
        r"(?<=[aoɔeɛøʏɐəœiuyɿʮɪŋʔl"+"\u0329\u0303\u030d"+r"])([12345]{1,3})\b", r"\t\1", s
    )
    s = re.sub(r"\b([aoɔeɛøʏɐəœiuyɿʮ])", r"∅\1", s)
    s = re.sub(r"(?<![iuyʮəœ])([aoɔeɛøʏɐəœiuyɿʮ])", r"\t\1", s)
    s = re.sub(r"\b(ʔ)?([mnŋ])"+"([\u0329\u030d])", r"\1\2\t\2\3", s)
    return re.split(r"\t", s)

def ghoqdaon2yihwei(s):
    "將學堂式吳拼轉爲協會式吳拼"
    s = s.lower()
    s = re.sub(r"\bgn", r"ny", s)
    s = re.sub(r"\bkn", r"'ny", s)
    s = re.sub(r"\bnk", r"'ng", s)
    s = re.sub(r"io(?=\b|\d)", r"iuo", s)
    s = re.sub(r"iau(?=\b|\d)", r"io", s)
    s = re.sub(r"iaon(?=\b|\d)", r"iuaon", s)
    s = re.sub(r"(s|z|tsh)yu(?=n|q)", r"\1oe", s)
    s = re.sub(r"er(?=\b|\d)", r"r", s)
    s = re.sub(r"q(?=\b|\d)", r"h", s)
    s = re.sub(r"\b(m|n|ng|l)h", r"'\1", s)
    s = re.sub(r"\b('?ny)i([aeou])", r"\1\2", s)
    for j in range(8):
        s = re.sub(r"(?<=[a-z])"+str(j+1)+r"\b", str(int(j/2)+1), s)
    return s

def yihwei2ghoqdaon(s):
    "將協會式吳拼轉爲學堂式吳拼"
    s = s.lower()
    s = re.sub(r"([aeiou])h(?=\b|\d)", r"\1q", s)
    s = re.sub(r"\bny", r"gni", s)
    s = re.sub(r"ii", r"i", s)
    s = re.sub(r"'ng", r"hng", s)
    s = re.sub(r"'(m|n|gn|l)", r"h\1", s)
    s = re.sub(r"\bhgn", r"kn", s)
    s = re.sub(r"io(?=\b|\d)", r"iau", s)
    s = re.sub(r"iuo(?=\b|\d)", r"io", s)
    s = re.sub(r"iuaon(?=\b|\d)", r"iaon", s)
    s = re.sub(r"(s|z|tsh)oe(?=n|q)", r"\1yu", s)
    for j in [4, 3, 2, 1]:
        s = re.sub(r"(?<=[a-z])"+str(j)+r"\b", str(int(j*2)-1), s)
    for j in [1, 3, 5, 7]:
        s = re.sub(r"(?<=\b[bmvdnlzjgywr])([^\b]*?)"+str(j)+r"\b", r"\g<1>"+str(j+1), s)
    s = re.sub(r"\bhng", r"nk", s)
    s = re.sub(r"\bh(m|n|l)", r"\1h", s)
    s = re.sub(r"r(?=\b|\d)", r"er", s)
    return s

def old2new(s):
    "將老派寧波話口音的學堂式吳拼轉爲新派"
    s = s.lower()
    s = re.sub(r"\b[^\b]*?(y|i)o\d?(?=\b|\d)", r"", s)
    s = re.sub(r"\bc(h)?ie(?=\b|\d)", r"ts\1e", s)
    s = re.sub(r"\bjie(?=\b|\d)", r"dze", s)
    s = re.sub(r"(?<=[sz])hie(?=\b|\d)", r"e", s)
    s = re.sub(r"ciaon", r"tsaon", s)
    s = re.sub(r"uo(?=\b|\d)", r"o", s)
    s = re.sub(r"wo(?=\b|\d)", r"gho", s)
    s = re.sub(r"(s|z|tsh)yu(?=n|q)", r"\1o", s)
    s = re.sub(r"(\by|i)u(?=n|q)", r"\1o", s)
    s = re.sub(r"un(?=\b|\d)", r"u", s)
    s = re.sub(r"ia(?=q)", r"i", s)
    s = re.sub(r"ya(?=q)", r"yi", s)
    s = re.sub(r"ya(?=q)", r"yi", s)
    s = re.sub(r"(?<!\d)([46])\b", r"2", s)
    return s

if __name__ == "__main__":
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
./gninpou.py -i <file> -o <file> -f <option>

Options:
-i <file>            input file
-o <file>            output file
-f <option>          fuction
-h                   Display this information

Fuctions:
compat2gninpou       將兼容格式轉爲寧波城區口音
phin2ipa             將吳拼轉換爲IPA
phinsplit            將吳拼分割爲聲母韻母和聲調
ipa2phin             將IPA轉換爲吳拼
ipasplit             將IPA分割爲聲母韻母和聲調
ghoqdaon2yihwei      將學堂式吳拼轉爲協會式吳拼
yihwei2ghoqdaon      將協會式吳拼轉爲學堂式吳拼
old2new              將老派轉爲新派
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
