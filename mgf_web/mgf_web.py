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
        file_param = {'url':url, 'size':0, 'unit':''}

        req = requests.get(file_param['url'], stream=True)
        headers = req.headers
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

    def __save_file(self, filename, save_path):
        self.html_content = self.url_resp.read()
        path = save_path + filename
        # if (os.path.isfile(path) == True):
        #     size = os.path.getsize(path)
        #     if (size != 0):
        #         return True
        # else:
        with open(path, 'wb+') as file:
            file.write(self.html_content)

    def get_html(self, url = '', filename = '', save_path = '', save = True):
        if (url == '' or save_path == ''):
            print("params error.")
            return None
        if (save == True and filename == ''):
            print("filename error.")
            return None
        self.url_resp = url_req.urlopen(url)
        if (save == True):
            ret = self.__save_file(filename, save_path);
            if (ret):
                print("ok")
        return (len(self.html_content)/1024)





