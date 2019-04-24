import time


def log(*args, **kwargs):
    """
    日志打印函数, 输入任意数据, 将其按特定格式打印出来并保存的根目录的log文件中
    :param args:
    :param kwargs:
    :return: None
    """
    # time.time() 返回 unix time, 并将其转换为如下格式
    time_format = '[--%Y/%m/%d--%H:%M:%S--]'
    localtime = time.localtime(int(time.time()))
    formatted = time.strftime(time_format, localtime)

    with open('log.gua.txt', 'a', encoding='utf-8') as f:
        # 时间和log内容分开, 并且加上分隔符号
        print(f'\n{formatted}')
        print('-' * 25)
        print(*args, **kwargs)
        print('-' * 25)

        # 将log的内容写到文件里, 与之前的print分开是为了避免写文件太慢影响print
        print(f'\n{formatted}', file=f)
        print('-' * 25, file=f)
        print(*args, **kwargs, file=f)
        print('-' * 25, file=f)


def load_str(filename):
    fn = filename
    with open(fn, 'r', encoding='utf-8') as f:
        r = f.read()
    return r


def dump_str(filename, content):
    fn = filename
    c = content
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    return 0
