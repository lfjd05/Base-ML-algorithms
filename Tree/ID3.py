"""
    ID3决策树，ID3决策树还是比较弱智的，使用信息熵增益的方法决策树层数会较少
"""
# -*- coding: utf-8 -*-


class ID3Tree(object):
    def __init__(self):
        self.tree = {}
        self.dataSet = []
        self.labels = []  # 变量名字

    # 读取数据
    def load_Data(self, path, labels):
        recordlist = []
        fp = open(path, 'rb')
        content = fp.read()
        fp.close()
        # 'ab c\n\nde fg\rkl\r\n'可以分割为['ab c', '', 'de fg', 'kl']
        rowlist = content.splitlines()   # 按照行转一维


if __name__ == '__main__':
    dtree = ID3Tree()
    dtree.load_Data('data/dataset.dat', ['age', 'revenue', 'student', 'credit'])
    