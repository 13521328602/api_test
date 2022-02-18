import yaml
import os


def readyaml(yamlPath):
    """读取yaml文件内容"""
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("未找到文件")
    f = open(yamlPath, 'r', encoding="utf-8")
    c = f.read()
    d = yaml.safe_load(c)
    print(d)
    return d


if __name__ == '__main__':
    yamlpath = "testdata.yml"
    readyaml(yamlpath)