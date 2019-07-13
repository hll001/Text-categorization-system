# 读取出对应路径文本的内容
def readFile(path):
    with open(path, 'r', errors='ignore') as file:  # 文档中编码有些问题，所有用errors过滤错误
        # 返回读取文件的内容
        content = file.read()
        return content


if __name__ == '__main__':
    print(readFile('F:/test/133_教育.txt'))