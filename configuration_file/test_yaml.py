#读取yaml文件并打印值
import yaml


with open("./one.yaml","r",encoding='utf-8') as f:
    data=yaml.safe_load(f)
    
print("app.name = ", data["app"]["name"])

print("database.port = ", data["database"]["port"])
