#!/usr/bin/env python
#-*- coding:utf-8 -*-
import subprocess
subprocess.Popen("git config --global user.name '你的github用户名'", shell=True)
subprocess.Popen("git config --global user.email 你的邮箱", shell=True)
subprocess.Popen("git config --global color.ui auto", shell=True)
subprocess.Popen("git config --global core.editor vim", shell=True)  #你想要的编辑器，我是用vim
subprocess.Popen("git config --global merge.tool vimdiff", shell=True) #设置你的合并工具
ls=subprocess.Popen("ls ~/.ssh/", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,shell=True)
ls_out=ls.stdout.read()
ls.stdout.close()

#生成rsa密钥对
set_ssh = subprocess.Popen("ssh-keygen -t rsa -C '你的邮箱'", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,shell=True)
set_ssh.stdin.write("\n")
#查看是否已存在rsa，如果以前电脑里存有rsa就需要输入‘y’确认覆盖
if 'id_rsa' in ls_out:
    set_ssh.stdin.write("y")
    set_ssh.stdin.write("\n")

set_ssh.stdin.close()
subprocess.Popen("echo 'git一键配置脚本'", shell=True)
subprocess.Popen("echo '作者：hijacklinux'", shell=True)
subprocess.Popen("echo '输入密码后，请复制下面公钥内容粘贴到github->settings->SSH keys,并按Ctrl+C退出配置'", shell=True)
subprocess.Popen("echo '\n'", shell=True)
cmd_out = set_ssh.stdout.read()
set_ssh.stdout.close()
subprocess.Popen("cat ~/.ssh/id_rsa.pub", shell=True)
