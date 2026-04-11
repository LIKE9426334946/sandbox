import torch
import platform

def print_env_info():
    # Python版本
    print(f"Python版本: {platform.python_version()}")

    # PyTorch版本
    print(f"PyTorch版本: {torch.__version__}")

    # CUDA版本（PyTorch编译时使用的CUDA）
    print(f"CUDA版本: {torch.version.cuda}")

    # GPU信息
    if torch.cuda.is_available():
        print(f"GPU数量: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("未检测到GPU")

if __name__ == "__main__":
    print_env_info()
