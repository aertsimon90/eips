import requests, socket, random, json
from requests.auth import HTTPBasicAuth
session = requests.Session()
http_proxy = """159.65.230.46:8888
159.203.178.26:8080
23.95.164.200:80
142.93.202.130:3128
144.86.187.61:3129
80.67.8.6:80
185.101.16.52:80
147.75.202.36:10042
47.89.184.18:3128
51.254.78.223:80
159.253.4.219:80
46.101.168.118:8080
209.38.184.90:8080
186.96.95.205:999
37.110.130.223:8081
165.22.77.86:80
65.109.13.237:80
103.49.202.252:80
103.86.109.38:80
103.253.103.50:80""".split()
random.shuffle(http_proxy)
https_proxy = """46.202.89.54:8080
104.168.57.24:3128
139.178.66.228:10002
139.178.66.227:10002
208.115.249.83:3128
74.255.219.229:3129
162.240.154.26:3128
147.75.101.247:10003
144.86.187.60:3129
145.40.90.218:9443
5.196.119.174:3128
147.75.101.247:10000
192.3.153.65:3128
144.86.187.58:3129
185.247.185.19:3128
194.163.153.9:3128
185.221.152.148:3128
41.33.174.100:3128
54.37.207.54:3128
41.128.90.52:1981
188.130.240.136:8080
51.75.86.68:3128
165.225.72.38:11351
141.95.1.186:3128
145.40.68.148:10001
144.86.187.52:3129
145.40.73.109:10010
13.208.249.0:80
45.226.226.26:999
145.40.73.109:10005
45.119.114.203:3129
181.114.225.187:8080
181.114.225.186:8080
202.137.8.147:8080
43.134.118.223:3128""".split()
random.shuffle(https_proxy)
def client_request(method, url, ip="129.129.129.129", ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) AppleWebKit/537.36 (KHTML, like Gecko) EIPS/11.3.7 (SSP/IIS/ICANN-W3C Unified Global Network Management) Secure-Web/7.6.2 (Enterprise Cyber Defense) ICANN/Global-DNS-Management/9.4.1 (IPv6-Compliant) W3C/Standards-Protocol/5.2.3 (Web Architecture Enhancement) Secure-Access/12.8.0 (High-Level Encryption) DDoS-Protect/15.3.2 (Active Mitigation) Multi-Layer-Protection/6.5.9 (Advanced Threat Management) Protocol-Enhancer/10.0 (Enhanced EIPS Integration)", headers={}, data="", proxies={}, cookies={}, forwarded_protect_count=4, timeout=2, proxy_auth=("", "")):
	global session
	try:
		origin = "/".join(url.split("/")[:3])
	except:
		origin = url
	try:
		admin = "/".join(url.split("://")[1:]).split("/")[0]
		admin = socket.gethostbyname(admin)
	except:
		admin = "/".join(origin.split("://")[1:])
	forwarded = f"{ip}, {admin}"
	for _ in range(forwarded_protect_count):
		forwarded += ", "+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
	headerss = {"User-Agent": ua, "X-Forwarded-For": forwarded, "X-Real-IP": ip, "X-Real-Ip": ip, "X-Client-IP": ip, "Referer": url, "Origin": origin, "Authority": admin, "HTTP_CLIENT_IP": ip, "HTTP_USER_AGENT": ua, "HTTP_X_FORWARDED_FOR": forwarded, "HTTP_X_REALHOST": ip, "X-Real-Host": ip, "Accept": "*/*", "Accept-Encoding": "*", "Accept-Language": "en-US", "Cache-Control": "no-cache", "Connection": "keep-alive"}
	for h, v in headers.items():
		headerss[str(h)] = str(v)
	r = session.request(method=method, url=url, headers=headerss, cookies=cookies, proxies=proxies, data=data, timeout=timeout, auth=HTTPBasicAuth(proxy_auth[0], proxy_auth[1]))
	return {"content": r.text, "status_code": r.status_code, "headers": dict(r.headers), "cookies": r.cookies.items(), "url": r.url, "encoding": r.encoding}
def proxy_request(method, url, ip="129.129.129.129", ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) AppleWebKit/537.36 (KHTML, like Gecko) EIPS/11.3.7 (SSP/IIS/ICANN-W3C Unified Global Network Management) Secure-Web/7.6.2 (Enterprise Cyber Defense) ICANN/Global-DNS-Management/9.4.1 (IPv6-Compliant) W3C/Standards-Protocol/5.2.3 (Web Architecture Enhancement) Secure-Access/12.8.0 (High-Level Encryption) DDoS-Protect/15.3.2 (Active Mitigation) Multi-Layer-Protection/6.5.9 (Advanced Threat Management) Protocol-Enhancer/10.0 (Enhanced EIPS Integration)", headers={}, data="", proxies={}, cookies={}, forwarded_protect_count=4, timeout=8, proxy_auth=("", "")):
	if url.startswith("http://"):
		for proxy in http_proxy:
			try:
				recv = client_request(method, url, ip=ip, ua=ua, headers=headers, data=data, proxies={"http": f"http://{proxy}", "https": f"https://{proxy}"}, cookies=cookies, forwarded_protect_count=forwarded_protect_count, timeout=timeout, proxy_auth=proxy_auth)
				return recv
				break
			except:
				pass
		return {"content": "EIPS Error: HTTP Proxy not found.", "status_code": 0, "headers": {}, "cookies": [], "url": "", "encoding": ""}
	if url.startswith("https://"):
		for proxy in https_proxy:
			try:
				recv = client_request(method, url, ip=ip, ua=ua, headers=headers, data=data, proxies={"http": f"http://{proxy}", "https": f"https://{proxy}"}, cookies=cookies, forwarded_protect_count=forwarded_protect_count, timeout=timeout, proxy_auth=proxy_auth)
				return recv
				break
			except:
				pass
		return {"content": "EIPS Error: HTTPS Proxy not found.", "status_code": 0, "headers": {}, "cookies": [], "url": "", "encoding": ""}
	
def eipshost_request(method, url, ip="129.129.129.129", ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) AppleWebKit/537.36 (KHTML, like Gecko) EIPS/11.3.7 (SSP/IIS/ICANN-W3C Unified Global Network Management) Secure-Web/7.6.2 (Enterprise Cyber Defense) ICANN/Global-DNS-Management/9.4.1 (IPv6-Compliant) W3C/Standards-Protocol/5.2.3 (Web Architecture Enhancement) Secure-Access/12.8.0 (High-Level Encryption) DDoS-Protect/15.3.2 (Active Mitigation) Multi-Layer-Protection/6.5.9 (Advanced Threat Management) Protocol-Enhancer/10.0 (Enhanced EIPS Integration)", headers={}, data="", proxies={}, cookies={}, forwarded_protect_count=4, timeout=10, proxy_auth=("", "")):
	data = {"method": method, "url": url, "ip": ip, "ua": ua, "headers": headers, "data": data, "proxies": proxies, "cookies": cookies, "forwarded_protect_count": forwarded_protect_count, "timeout": timeout, "proxy_auth": proxy_auth}
	return requests.request(method="EIPS", url="https://eips.pythonanywhere.com/eips", json=data).json()