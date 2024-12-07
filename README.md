# SNI-bypass
A tool to bypass network restrictions by modifying SNI and using custom host rules based on data from the SpaceTimee/Cealing-Host project. It allows dynamic domain-to-alias and alias-to-IP mapping for circumventing censorship.

### Features:
1.Dynamic Domain Mapping: Maps multiple domains to a set of aliases and IP addresses to bypass filtering systems that rely on SNI.
2.Custom Host Rules: Generates custom host rules and resolver rules for seamless redirection and bypass.
3.Easy Integration: Uses simple JSON-based configuration for easy modifications and updates.
4.Support for SSL/TLS Encryption: Works over HTTPS to ensure secure and anonymous connections.
### How to Use:
1.Clone or download the repository.
2.Modify the data.json file with your custom domains, aliases, and IP addresses.
3.Run the script to generate the necessary command for bypassing network restrictions.
4.Use the output command in your proxy or tunneling tool to bypass censorship.

## Data Source

The `data.json` used in this project is sourced from the [SpaceTimee/Cealing-Host](https://github.com/SpaceTimee/Cealing-Host) project.

该项目旨在通过操控 SNI 字段，并使用自定义的主机规则来重定向流量，从而绕过网络审查。它利用来自 SpaceTimee/Cealing-Host 项目的数据结构生成域名映射，帮助用户绕过基于域名过滤的限制。

### 功能特点：
1.动态域名映射： 将多个域名映射到一组别名和 IP 地址，从而绕过依赖于 SNI 的过滤系统。
2.自定义主机规则： 生成自定义的主机规则和解析器规则，以实现无缝重定向和绕过。
3.简易集成： 使用简单的 JSON 配置文件，便于修改和更新。
4.支持 SSL/TLS 加密： 通过 HTTPS 工作，确保安全和匿名连接。
### 使用方法：
1.克隆或下载本仓库。
2.修改 data.json 文件，添加你自定义的域名、别名和 IP 地址。
3.运行脚本，生成绕过网络限制所需的命令。
4.在代理或隧道工具中使用输出的命令，来绕过审查。

## 数据来源

该项目中的 `data.json` 数据来源于 [SpaceTimee/Cealing-Host](https://github.com/SpaceTimee/Cealing-Host) 项目。
