import urllib3
import json

file_debug = open("Filter_debug.txt", mode='w', encoding='utf-8')
file_debug.close()

f1_name = "../phaetonbravo/phaetonbravo_data_month/link.json"
f1 = open(f1_name, mode='r', encoding='utf-8')
link_json_data = json.load(f1)
for user in link_json_data:
    link = user['link'][0]
# print(link)

http = urllib3.PoolManager()
r = http.request('GET', link)
s = r.data.split()
l = len(s)
y = s[l-1].decode("utf-8")
o = y.split(';')
l = len(o)
y = o[l-1]
# print(l)
# print(y)
file_name = "Kpm.txt"
Kpm_today_w = open(file_name, mode='w', encoding='utf-8')
Kpm_today_w.write(y)
Kpm_today_w.close()

file_debug = open("Filter_debug.txt", mode='w', encoding='utf-8')
file_debug.write("Working well")
file_debug.close()