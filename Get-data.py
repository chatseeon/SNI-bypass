import requests
import os

url = "https://2git.xyz/SpaceTimee/Cealing-Host/raw/main/Cealing-Host.json"
#此镜像链接仅大陆用户可用
#非大陆ip请使用源地址
save_path = "./data.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    #"Referer": "https://2git.xyz",  # 添加 Referer 头部，模拟请求来源，若要使用请取消注释并可能需要修改
}

# 禁用 SSL 验证
response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as file:
        file.write(response.content)
    print(f"File saved as {save_path}")
else:
    print("Failed to download file:", response.status_code)
