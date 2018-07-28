# zc-cris

# 导入我们自己写的模块util：先从sys.modules 里查看是都模块都已经导入，如果没有导入，就依据sys.path 路径寻找模块，直到找到这个模块，然后创建这个模块的
# 命名空间，解释这个模块，将其中的内容加载到命名空间里

import util

util.func()
import time as t  # 给模块起别名：

print(t.time())
