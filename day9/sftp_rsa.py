#Auther nmap
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('d:\id_rsa_2048')

transport = paramiko.Transport(('10.0.1.23', 22))
transport.connect(username='root', pkey=private_key )

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('id_rsa_2048', '/tmp/hehe.txt')
# 将remove_path 下载到本地 local_path
#sftp.get('remove_path', 'local_path')

transport.close()