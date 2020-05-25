# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import json


re_p = re.compile(r'OLD_ROW=\{(.*?)\} \|')
re_p_0 = re.compile(r'([0-9]+):\{(.*?)\}')
re_p_1 = re.compile(r', .*$')
re_p_2 = re.compile(r'".*?":(.*?)$')
row_lst = []
with open("1107208209222809.all.dump", 'r') as f:
    for i in f:
        row_lst.append(i.strip())
        
for line in row_lst:
    re_res = re_p.findall(line)
    for jj in re_res:
        if jj.strip() == '{}': continue
        r_str = jj.strip()
        re_jj = re_p_0.findall(r_str)
        is_one = True
        is_in = False
        for jjj in re_jj:
            if not is_one:
                print(", ", end="")
            else:
                print("(", end="")
                is_one = False
            data = re_p_1.sub("", jjj[1]).strip()
            data = re_p_2.search(data)
            data = data.group(1)
            print(data, end="")
            is_in = True
        if is_in:
            print(");")
