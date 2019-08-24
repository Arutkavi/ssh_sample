import paramiko
import sys

## EDIT SSH DETAILS ##

SSH_ADDRESS = "192.168.1.1"
SSH_USERNAME = "admin"
SSH_PASSWORD = "admin"

## CODE BELOW ##

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_stdin = ssh_stdout = ssh_stderr = None
ssh.connect(SSH_ADDRESS, username=SSH_USERNAME, password=SSH_PASSWORD)

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ifconfig")
sys.stdout.write(ssh_stdout.read())
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show buildinfo")
test = ssh_stdout.read()
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show buildinfo")
test1 = ssh_stdout.read()

if "SR900ac" in test:
   ssh_stdin, ssh_stdout, ssh_stderr =ssh.exec_command("show mfg")   
   sys.stdout.write(ssh_stdout.read())

if "SR400ac" in test1:
   ssh_stdin, ssh_stdout, ssh_stderr =ssh.exec_command("show hwrev")   
   sys.stdout.write(ssh_stdout.read())
