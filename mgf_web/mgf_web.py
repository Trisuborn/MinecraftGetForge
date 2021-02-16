import urllib.request as url_req
import os

class mgf_web_class(object):
    def __init__(self):
        self.html_content = ''

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
