# SNI-bypass

该项目旨在通过操控 SNI 字段，并使用自定义的主机规则来重定向流量。它利用来自 SpaceTimee/Cealing-Host 项目的数据结构生成域名映射，帮助用户绕过基于域名过滤的限制。

A tool to bypass network restrictions by modifying SNI and using custom host rules based on data from the SpaceTimee/Cealing-Host project. It allows dynamic domain-to-alias and alias-to-IP mapping for circumventing censorship.

### 功能特点：

1. **动态域名映射**：将多个域名映射到一组别名和 IP 地址，从而绕过依赖于 SNI 的过滤系统。
2. **自定义主机规则**：生成自定义的主机规则和解析器规则，以实现无缝重定向和绕过。
3. **简易集成**：使用简单的 JSON 配置文件，便于修改和更新。
4. **一键启用**，使用方便简单，且修改是一次性的，不会影响浏览器的正常使用。

### 使用方法：

1. 克隆或下载本仓库。
2. 在 CMD 中运行 `Get-data.py`，或者自行创建 `data.json` 文件，添加你自定义的域名、别名和 IP 地址。
3. 运行 `main.py`，将会直接打开带参数的浏览器。

## 注意事项

`--ignore-certificate-errors` 参数会绕过 SSL/TLS 证书验证，从而允许中间代理替换掉目标网站的证书。这将导致连接失去加密保护，从而使得数据可能被中间人攻击者监控或篡改。

### 安全警告：

- 请谨慎使用，尤其是在处理敏感数据或个人隐私信息时。
- 仅在确保网络环境安全或进行调试时使用。
- 强烈建议仅在信任的网络环境中使用。

## 数据来源

该项目中的 `data.json` 数据来源于 [SpaceTimee/Cealing-Host](https://github.com/SpaceTimee/Cealing-Host) 项目。


### Features:

1. **Dynamic Domain Mapping**: Maps multiple domains to a set of aliases and IP addresses, bypassing SNI-based filtering systems.
2. **Custom Host Rules**: Generates custom host rules and resolver rules for seamless redirection and bypassing.
3. **Easy Integration**: Uses a simple JSON configuration file, making it easy to modify and update.
4. **One-click Enable**: Simple to use, with one-time changes that do not affect the normal functioning of the browser.

### Usage:

1. Clone or download this repository.
2. Run `Get-data.py` in CMD, or create your own `data.json` file to add your custom domains, aliases, and IP addresses.
3. Run `main.py`, which will directly open the browser with the necessary parameters.

## Notes

The `--ignore-certificate-errors` parameter bypasses SSL/TLS certificate validation, allowing a proxy to replace the target website's certificate. This results in the loss of encryption protection, potentially allowing data to be monitored or tampered with by a man-in-the-middle attacker.

### Security Warning:

- Please use with caution, especially when handling sensitive data or personal privacy information.
- Only use when you are sure the network environment is secure or during debugging.
- It is strongly recommended to use this only in trusted network environments.

## Data Source

The `data.json` file in this project is sourced from the [SpaceTimee/Cealing-Host](https://github.com/SpaceTimee/Cealing-Host) project.


