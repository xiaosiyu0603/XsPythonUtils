# 用于Python模块化实用工具

每个模块都放在各自的文件夹里，工具放在根目录。

### 包含工具

| 工具                                            | 功能                                                 |
| ----------------------------------------------- | ---------------------------------------------------- |
| [batch_change_coding](batch_change_coding.py)   | 批量修改文件编码至指定编码，带过滤器                 |
| [gen_rnd_pswd](gen_rnd_pswd.py)                 | 生成随机密码，包括大小写字母、数字，可以指定密码长度 |
| [pyfiles_utf8bom2utf8](pyfiles_utf8bom2utf8.py) | 批量将Python源文件的编码从UTF-8-bom修改为UTF-8       |
| [urlclip](urlclip.py)                           | 将URL快捷方式裁剪到最简                              |

### 包含模块

| 模块                                      | 功能                               |
| ----------------------------------------- | ---------------------------------- |
| [dir_walker](./dir_walker/dir_walker.py)  | 产生一个递归遍历目录中文件的生成器 |
| [utils](./utils)                          | 一些零碎且被重复使用的实用工具     |
| [utils.argparse](./utils/argparse.py)     | argpasre扩展                       |
| [utils.pseudo_cpp](./utils/pseudo_cpp.py) | 模拟C++同名定义的功能的实用工具    |
| [utils.py](./utils/py.py)                 | Python语言相关实用工具             |
| [utils/type](./utils/type.py)             | 类型相关实用工具                   |

### 参考资料

1. [Python 3.x 文档](https://docs.python.org/zh-cn/3/index.html)；
