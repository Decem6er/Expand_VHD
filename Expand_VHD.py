import os

def change_vhdx_size():
    vhdx_path = input("请输入 vhdx 虚拟磁盘文件的地址：")
    if not os.path.exists(vhdx_path):
        print("文件不存在，请重新输入正确的地址！")
        return
    
    new_size = input("请输入新的虚拟磁盘大小（单位：GB）：")
    try:
        new_size = int(new_size) * 1024  # 转换为 MB
    except ValueError:
        print("输入的大小不合法，请重新输入！")
        return
    
    # 使用 Diskpart 命令更改虚拟磁盘大小
    diskpart_script = f"""
    select vdisk file="{vhdx_path}"
    expand vdisk size={new_size}
    """
    
    script_path = "diskpart_script.txt"
    with open(script_path, "w") as file:
        file.write(diskpart_script)
    
    # 执行 Diskpart 命令
    os.system(f"diskpart /s {script_path}")
    
    # 删除临时脚本文件
    os.remove(script_path)
    
    print("虚拟磁盘大小已成功更改！")

# 运行脚本
change_vhdx_size()
