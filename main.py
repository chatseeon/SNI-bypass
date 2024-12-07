# 生成的命令包含 --ignore-certificate-errors 参数，该参数将绕过 SSL/TLS 证书验证。
# 可能导致通信失去加密保护，信息可能被中间人攻击者监控或篡改。建议仅在信任的网络环境中使用。
import json

def generate_host_rules(data):
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
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("JSON 数据必须是一个列表。")
    for entry in data:
        if not isinstance(entry, list) or len(entry) != 3:
            raise ValueError(f"数据格式错误: {entry}")
    return data

if __name__ == "__main__":
    # 使用相对路径
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

    # 拼接最终的命令
    final_command = f"{host_rules} {resolver_rules} --test-type --ignore-certificate-errors"

    # 输出结果
    print("生成的命令:")
    print(final_command)
