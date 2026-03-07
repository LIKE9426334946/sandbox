# os 模块是 Python 标准库中用于 与操作系统交互 的模块，常见用途包括 文件与目录操作、路径处理、环境变量管理、执行系统命令等。
import os

# 获取当前工作目录
print(os.getcwd())

# 切换工作目录
os.chdir("/kaggle")

# 创建文件夹
os.mkdir("demo")
os.mkdir("demo1")

# 创建多级文件夹
os.makedirs("a/b/c")

# 删除文件夹
os.rmdir("demo1")

# 删除多级文件夹
os.removedirs("a/b/c")

files = os.listdir(".")
print(files)

path = "demo"

print(os.path.exists(path))   # 是否存在
print(os.path.isfile(path))   # 是否文件
print(os.path.isdir(path))    # 是否目录
print(os.path.abspath(path))  # 绝对路径

path = os.path.join("data", "train", "image.jpg")
print(path)

size = os.path.getsize("demo")
print("文件大小:", size)

print(os.environ.get("HOME"))
os.environ["MY_VAR"] = "hello"

os.system("ls")

for root, dirs, files in os.walk("dataset"):
    print("当前目录:", root)
    print("子目录:", dirs)
    print("文件:", files)

data_dir = "dataset"

for file in os.listdir(data_dir):
    path = os.path.join(data_dir, file)
    if os.path.isfile(path):
        print(path)
