# 生成的命令包含 --ignore-certificate-errors 参数，该参数将绕过 SSL/TLS 证书验证。
# 可能导致通信失去加密保护，信息可能被中间人攻击者监控或篡改。建议仅在信任的网络环境中使用。
import os
import json
import subprocess


def generate_host_rules(data):
    """生成 --host-rules 和 --host-resolver-rules 参数"""
    host_rules = []
    resolver_rules = []
    alias_map = {}

    # 为每个唯一 IP 地址分配别名
    alias_counter = 0
    for entry in data:
        domains, alias, ip = entry
        if ip and not alias:  # 没有别名但有 IP，生成唯一别名
            alias_key = f"CYFM{alias_counter}"
            alias_map[ip] = alias_key
            alias_counter += 1

    for entry in data:
        try:
            domains, alias, ip = entry
            if alias:  # 使用给定别名
                for domain in domains:
                    host_rules.append(f"MAP {domain} {alias}")
                if ip:
                    resolver_rules.append(f"MAP {alias} {ip}")
            elif ip:  # 使用自动生成的别名
                alias_key = alias_map[ip]
                for domain in domains:
                    host_rules.append(f"MAP {domain} {alias_key}")
                resolver_rules.append(f"MAP {alias_key} {ip}")
        except ValueError:
            print(f"数据格式错误: {entry}")
            continue

    return (
        ' --host-rules="' + ",".join(host_rules) + '"',
        ' --host-resolver-rules="' + ",".join(resolver_rules) + '"'
    )


def load_data_from_json(json_file):
    """从 JSON 文件加载数据"""
    with open(json_file, 'r', encoding='utf-8') as f:
import os
import json
import subprocess


def generate_host_rules(data):
    """生成 --host-rules 和 --host-resolver-rules 参数"""
    host_rules = []
    resolver_rules = []
    alias_map = {}

    # 为每个唯一 IP 地址分配别名
    alias_counter = 0
    for entry in data:
        domains, alias, ip = entry
        if ip and not alias:  # 没有别名但有 IP，生成唯一别名
            alias_key = f"CYFM{alias_counter}"
            alias_map[ip] = alias_key
            alias_counter += 1

    for entry in data:
        try:
            domains, alias, ip = entry
            if alias:  # 使用给定别名
                for domain in domains:
                    host_rules.append(f"MAP {domain} {alias}")
                if ip:
                    resolver_rules.append(f"MAP {alias} {ip}")
            elif ip:  # 使用自动生成的别名
                alias_key = alias_map[ip]
                for domain in domains:
                    host_rules.append(f"MAP {domain} {alias_key}")
                resolver_rules.append(f"MAP {alias_key} {ip}")
        except ValueError:
            print(f"数据格式错误: {entry}")
            continue

    return (
        ' --host-rules="' + ",".join(host_rules) + '"',
        ' --host-resolver-rules="' + ",".join(resolver_rules) + '"'
    )


def load_data_from_json(json_file):
    """从 JSON 文件加载数据"""
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("JSON 数据必须是一个列表。")
    for entry in data:
        if not isinstance(entry, list) or len(entry) != 3:
            raise ValueError(f"数据格式错误: {entry}")
    return data


def clean_path(input_path):
    """清理路径中的多余双引号"""
    # 如果路径被双引号包围，去除两端的双引号
    return input_path.strip().strip('"')


def get_browser_path():
    """提示用户输入浏览器路径"""
    while True:
        browser_path = input("请输入浏览器的完整路径（例如 C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe）：\n")
        browser_path = clean_path(browser_path)
        
        # 检查路径是否存在
        if not os.path.isfile(browser_path):
            print(f"路径无效或文件不存在：{browser_path}")
        else:
            return browser_path


def launch_browser(browser_path, params):
    """启动浏览器并传递参数"""
    try:
        # 使用 subprocess 启动浏览器
        subprocess.run([browser_path] + params, check=True)
        print("浏览器已成功启动。")
    except Exception as e:
        print(f"启动浏览器时出错：{e}")


def main():
    # 使用相对路径加载 JSON 数据
    json_file = 'data.json'

    # 加载 JSON 数据
    try:
        data = load_data_from_json(json_file)
    except FileNotFoundError:
        print(f"文件 {json_file} 未找到，请检查路径！")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"解析 JSON 文件失败: {e}")
        exit(1)
    except ValueError as e:
        print(f"数据验证失败: {e}")
        exit(1)

    # 生成规则
    host_rules, resolver_rules = generate_host_rules(data)

    # 拼接参数
    params = [
        host_rules,
        resolver_rules,
        "--test-type",
        "--ignore-certificate-errors"
    ]

    # 获取浏览器路径
    browser_path = get_browser_path()

    # 启动浏览器
    launch_browser(browser_path, params)


if __name__ == "__main__":
    main()
