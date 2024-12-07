# SNI-bypass
A tool to bypass network restrictions by modifying SNI and using custom host rules based on data from the SpaceTimee/Cealing-Host project. It allows dynamic domain-to-alias and alias-to-IP mapping for circumventing censorship.

This project is designed to bypass network censorship by manipulating the SNI (Server Name Indication) field and using custom host rules to redirect traffic. It leverages the data structure from the SpaceTimee/Cealing-Host project to generate domain mappings, allowing users to bypass restrictions based on domain filtering.

Features:
Dynamic Domain Mapping: Maps multiple domains to a set of aliases and IP addresses to bypass filtering systems that rely on SNI.
Custom Host Rules: Generates custom host rules and resolver rules for seamless redirection and bypass.
Easy Integration: Uses simple JSON-based configuration for easy modifications and updates.
Support for SSL/TLS Encryption: Works over HTTPS to ensure secure and anonymous connections.
How to Use:
Clone or download the repository.
Modify the data.json file with your custom domains, aliases, and IP addresses.
Run the script to generate the necessary command for bypassing network restrictions.
Use the output command in your proxy or tunneling tool to bypass censorship.
This tool is useful for those looking to bypass domain-based censorship on the network, especially for users in restrictive environments.
