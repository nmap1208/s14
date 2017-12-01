#Auther nmap
import paramiko

transport = paramiko.Transport(('10.0.1.23',22))
transport.connect(username='root',password='2012server')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('ssh.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('/tmp/1.txt', '3.txt')

transport.close()