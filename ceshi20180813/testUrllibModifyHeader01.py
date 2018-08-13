import urllib.request
import userAgents
'''userAgents.py是个自定义的模块，位置处于当前目录下'''
class UrllibModifyHeader(object):
    '''使用urllib模块修改header'''
    def __init__(self):
        PIUA = userAgents.pcUserAgent.get('IE 9.0')

        MUUA = userAgents.mobileUserAgent.get('UC standard')

        self.url = 'http://www.baidu.com'

        self.useUserAgent(PIUA,1)
        self.useUserAgent(MUUA,2)

    def useUserAgent(self,userAgent,name):
        request = urllib.request(self.url)
        request.add_header(userAgent.split(':')[0],userAgent.split(':')[1])
        response = urllib.urlopen(request)
        filename = str(name)+'.html'
        with open(filenam,'a') as fp:
            fp.write('%s\n\n'%userAgent)
            fp.write(response.read())

if __name__ == '__main__':
    unh = UrllibModifyHeader()

