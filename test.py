import urllib.request as url_req
import urllib.parse as url_parse
import requests
import httplib2

import mgf_web.mgf_web as mgf_web

# url = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.12.1.html'
# url = 'https://baidu.com'
# url = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.12.1-14.22.1.2485/forge-1.12.1-14.22.1.2485-installer-win.exe'
url = 'https://down.qq.com/qqweb/PCQQ/PCQQ_EXE/PCQQ2021.exe'
# url = 'https://blog.csdn.net/shangxiaqiusuo1/article/details/81035046'

if __name__ == '__main__':
    mgf_web_obj = mgf_web.mgf_web_class()
    # size = mgf_web_obj.get_html(url, 'test.html', './')
    # print("html size : %.2f KiB" % size)
    file_param = mgf_web_obj.get_file_size(url)
    print("url : %s\nsize: %.2f %s \n" % (file_param['url'], file_param['size'], file_param['unit']))

    # with open('test.html', 'wb+') as f:
    #     f.write(req.text.encode('utf-8'))


