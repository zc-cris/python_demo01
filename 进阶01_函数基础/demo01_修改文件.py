# _Author: zc-cris

# 如何修改文件

# mode 不写默认是 r 模式
with open("test", encoding="utf-8") as file, open("test.bak", mode='w', encoding="utf-8") as filebak:
    for line in file:
        if 'cris' in line:
            line = line.replace('cris', '詹姆斯')
        filebak.write(line)

import os  # 导入os 包

os.remove('test')
os.rename('test.bak', 'test')
