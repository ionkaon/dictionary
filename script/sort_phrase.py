#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTHOR: Electric Sheep
VERSION : v2021.08.06

詞表排序
"""
#%%
import pandas as pd
#%%
sheet = pd.read_csv("../詞表.tsv", sep="\t",  encoding="utf-8", dtype=str)
sheet.fillna(value="",inplace=True)
sheet.sort_values(by=["兼容格式", "繁體"], inplace=True)
sheet.drop_duplicates(inplace=True)
sheet.to_csv(
    "../詞表.tsv", sep="\t", encoding="utf-8", index=False, line_terminator="\n"
)
