#Auther nmap
import configparser
conf=configparser.ConfigParser()
conf.read('example.ini')
print(conf.sections())
print(conf.defaults()) #打印defaults
for key in conf['bitbucket.org']:
    print(key)