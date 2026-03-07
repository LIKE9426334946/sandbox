# 读取yaml文件并打印值

# 以下注释代码放在notebook中，可以直接运行
"""
%cd /kaggle/working
!rm -rf /kaggle/working/sandbox
!git clone https://github.com/LIKE9426334946/sandbox.git
%cd /kaggle/working/sandbox/configuration_file
!python3 test_yaml.py
"""
import yaml


with open("./one.yaml","r",encoding='utf-8') as f:
    data=yaml.safe_load(f)
    
print("app.name = ", data["app"]["name"])

print("database.port = ", data["database"]["port"])
print("运行完毕")
