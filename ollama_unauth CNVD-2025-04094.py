import requests
import pandas as pd
from requests.exceptions import RequestException

# 读取IP列表
with open('ips.txt', 'r') as f:
    ips = [line.strip() for line in f if line.strip()]

results = []

for ip in ips:
    url = f'http://{ip}:11434/api/tags'
    try:
        # 发送请求，设置超时时间为5秒
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 检查HTTP错误
        
        # 解析JSON数据
        data = response.json()
        models = data.get('models', [])
        
        # 提取所有model的name
        model_names = [model.get('name', '') for model in models]
        model_names_str = ', '.join(filter(None, model_names))  # 过滤空名称并连接
        
        results.append((ip, model_names_str))
    
    except RequestException as e:
        results.append((ip, f'请求错误: {str(e)}'))
    except ValueError as e:
        results.append((ip, f'JSON解析错误: {str(e)}'))
    except Exception as e:
        results.append((ip, f'未知错误: {str(e)}'))

# 写入Excel文件
df = pd.DataFrame(results, columns=['IP', 'Models'])
df.to_excel('2.xlsx', index=False)

print('处理完成，结果已保存到2.xlsx')