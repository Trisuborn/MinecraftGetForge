import urllib.request as url_req
import requests
import os

class mgf_web_class(object):
    def __init__(self):
        self.html_content = ''

    def get_file_size(self, url, size_type = None):
        '''
            size_type: Byte/KiB/MiB
        '''
        req = requests.get(url, stream=True)
        headers = req.headers
        file_param = {'url':url, 'req':req, 'size':0, 'unit':''}
        try:
            filesize = int(headers['Content-Length'])
        except:
            print("No key: 'Content-Length'" )
            return None
        if ((filesize < 1024) or (size_type == 'Byte')):
            file_param['size'] = filesize
            file_param['unit'] = 'Byte'
        elif ((filesize > 1024 and filesize < 1024*1024) or (size_type == 'KiB')):
            file_param['size'] = (filesize/1024)
            file_param['unit'] = 'KiB'
        elif ((filesize > 1024*1024) or (size_type == 'MiB')):
            file_param['size'] = (filesize/1024/1024)
            file_param['unit'] = 'MiB'
        return (file_param)

    def save_file(self, resp, type, filename, save_path):
        '''
            type: html/file
            ~~~~~~~~~~~~~~~
        '''
        path = save_path + filename
        if (type == 'html'):
            size = 0
            html_content = resp.readlines()
            with open(path, 'wb+') as file:
                for cont in html_content:
                    file.write(cont)
                    size += len(cont)
                    print(size)
            return size
        # elif (type == 'file'):



    def get_html(self, url = '', filename = '', save_path = '', save = True):
        if (url == '' or save_path == ''):
            print("params error.")
            return None
        if (save == True and filename == ''):
            print("filename error.")
            return None
        url_resp = url_req.urlopen(url)
        if (save == True):
            return self.save_file(url_resp, 'html', filename, save_path)


