#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUTHOR : Shin Zoqchiuq
VERSION : v2021.11.12

從 `字表.tsv` 生成 `甬城（考證）.tsv`
"""
import pandas as pd
import numpy as np
from gninpou import compat2gninpou

sheet = pd.read_csv(
    open("../字表.tsv", encoding="utf-8"), sep="\t",
    usecols=["繁體", "简体", "兼容格式", "篩選", "備註"]
)
sheet.rename(columns={"兼容格式":"吳拼"}, inplace=True)

sheet.drop(
    (
        (sheet["繁體"] == "#") | (sheet["篩選"] == "#") |
        [type(i) != str for i in iter(sheet["吳拼"])]
    ).to_numpy().nonzero()[0]
    , inplace=True
)

sheet.reset_index(inplace=True, drop=True)
sheet["吳拼"] = [compat2gninpou(i) for i in iter(sheet["吳拼"])]
sheet["備註"] = [
    i if type(i) == float or "(" not in i else np.nan for i in iter(sheet["備註"])
]
sheet.drop_duplicates(inplace=True)
sheet.reset_index(drop=True, inplace=True)

sheet[["繁體", "简体", "吳拼", "備註"]].to_csv(
    "../各地字表/甬城（考證）.tsv", encoding="utf-8", index=False, sep="\t"
)
