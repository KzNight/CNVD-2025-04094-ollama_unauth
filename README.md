>本脚本及生成结果仅用于技术交流与测试，使用者需自行承担所有风险。作者不保证数据的准确性、完整性，不对因使用此工具造成的任何直接或间接损失负责。请确保已获相关IP所有者授权后再进行检测。

脚本目前仅实现了未授权访问/api/tags获取ollama的列出本地模型，要使用请自行配合chatbox或其他应用。

## 漏洞简介

Ollama是一个本地私有化部署大语言模型（LLM，如DeepSeek等）的运行环境和平台，简化了大语言模型在本地的部署、运行和管理过程，具有简化部署、轻量级可扩展、API支持、跨平台等特点，在AI领域得到了较为广泛的应用。

Ollama存在未授权访问漏洞。由于Ollama默认未设置身份验证和访问控制功能，未经授权的攻击者可在远程条件下调用Ollama服务接口，执行包括但不限于敏感模型资产窃取、虚假信息投喂、模型计算资源滥用和拒绝服务、系统配置篡改和扩大利用等恶意操作。未设置身份验证和访问控制功能且暴露在公共互联网上的Ollama易受此漏洞攻击影响。

CNVD对该漏洞的综合评级为“高危”。

## 使用方法

- 使用**app.name=="Ollama Server"** 或者 **port=11434** 语法自行去资产探测网站搜索ollama应用
- 将获取的ip保存到本地 **ips.txt** 文档
- 运行以下命令：
```bash
python ollama_unauth CNVD-2025-04094.py
```
- 查看同目录的2.xlsx 获取结果。
