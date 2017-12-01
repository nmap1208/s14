#Auther nmap
import paramiko

transport = paramiko.Transport(('10.0.1.23', 22))
transport.connect(username='root', password='2012server')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
print (stdout.read().decode())

transport.close()