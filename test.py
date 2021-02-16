import urllib.request as ul_req

import mgf_web.mgf_web as mgf_web

# url = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.12.1.html'
# url = 'https://baidu.com'
url = 'https://baijiahao.baidu.com/s?id=1691774816108099834&wfr=spider&for=pc'

if __name__ == '__main__':
    mgf_web_obj = mgf_web.mgf_web_class()
    mgf_web_obj.get_html(url, 'test.html', './')
