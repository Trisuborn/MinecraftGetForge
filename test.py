import urllib.request as ul_req

url = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.12.2.html'
# url = 'https://github.com/Trisuborn'

if __name__ == '__main__':
    with open(file='./test.html', mode='wb+') as fs:
        resp = ul_req.urlopen(url)
        cont = resp.read()
        fs.write(cont);
