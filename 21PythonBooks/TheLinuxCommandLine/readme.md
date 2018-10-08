待续
Storage
Vi
Archiving And Bakcup



  ### Introduction

Many people speak of 'freedom' with regard to Linux, but I don't think most  
people know what this freedom really meams. Freedom is the power to decide what  
your computer does, and the only way to have this freedom is to know what your  
computer is doing. Freedom is a computer that is without secrets, one where  
everything can be known if you care enough to find out.

Linux is not just a piece of software, it's also a small part of the larger Unix
culture, which has its own language and history.

### Learning The Shell

terminal emulators
prompt
dash
slash
underscore
command -options arguments
ASCII(pronounced "As-Key")    
map keyboard characters to numbers
modify system settings and write our own scripts


"everything is a file"
less is more

While it is easy to perferm simple file manipulations with a graphical manager,
complicated tasks can be done easier with the command line programs.

special specify

alias name='string'
unalias name
alias

I/O redirection allows us to change where output goes and where input comes from.

The Difference Between > and |
command1 > file1      # 跟着一个文件，文件内容被重写; 如跟着一个命令，那命令就被重写了
command1 | command2   # command1的输出内容作为command2的输入

ls /bin /usr/bin | sort | uniq | grep zip
tail -f /var/log/messages  # 实时查看
ls /usr/bin | tee ls.txt | grep zip   # 既保存到文件ls.txt中，又输出给grep


Linux Is About Imagination
the person behind the counter

Expansion
Every time we type a command and press the enter key, BASH perform serveral
processes upon the text before it carries out our command.


Adanced Keyboard Tricks
many of
part of
some of
all of


Ctrl + A
Ctrl + E

Alt + f Move cursor forward one word
Alt + b Move cursor backward one word

Ctrl + k Kill text from the cursor location to the end of line
Ctrl + u Kill text form the cursor location the the beginnig of the line
Ctrl + y Yank text from the kill-ring and insert it at the cursor location

.bash_history

Ctrl + r  搜索命令
```
(reverse-i-search)`':
It is "reverse" because we are searching from "now" to some time in the past
```

Like so many things in Linux, from a couple of text files.
For each user account, the /etc/passwd file defines the user(login) name, uid, gid,
the account's real name, home directory, and login shell.


Symbolic notation does offer advantage of allowing you to set a single attribute
without disturbing any of the others.

区分一个概念，文件所属组与文件所有者所在组


chown
Superuser privileges are required to use this command.


Controlling processes
xlogo     # 前台执行
xlogo &   # 后台执行

ps
jobs    # 可查看在后台运行的进程

fg %1
bg %1
Ctrl + Z

The Environment
Knowing this, we can use the environment to cusotmize our shell experince.

printenv  
environment variables
set
environment variables and shell variables, as well as any defined shell functions
alias

Which Files Should We Modify?
As a general rule, to add directory to your PATH,
or define additional environmental variables, place those changes in .bash_profile
(or equivalent, according to your distribution.For example, Ubuntu uses .profile).
For everything else, place the changges in .bashrc

root /etc/profile   # root
common user
PATH        # 添加命令路径
.profile    # 添加环境变量
.bashrc     # 其他

Whenever we edit an important configuration file, it is always a good idea to create
a backup copy of the file first.
cp .bashrc .bashrc.bak

source .bashrc  to reload

echo $PS1  Prompt String one


Package management is a method of installing and maintaining software on the system.

apt-get update                  # 更新索引
apt-cache search search_name
apt-get install package_name
apt-cache show package_name
apt-get remove package_name
apt-get upgrade               # 更新软件


Networking
We will focus our attention on just a few of the most frequently used ones.
The commands chosen for examination include those used to monitor networks and
those used to transfer files.


ping linuxcommand.org
traceroute slashdot.com
ip a
netstat -ie
netstat -r
wget http://linuxcommand.org/index.php
ssh root@192.168.1.2


locate - Find Files The Easy Way   # 来源定时任务 updatedb 更新索引
locate bin/zip
locate zip | grep bin

find - Find Files The Hard Way
find ~ -type f -name ".php" -size +1M
find ~ \( -type -f -not -perm 0600 \) -or \( -type d -not -perm 0700\)

locate find 根据文件名和文件相关属性搜索文件
grep 根据文件内容搜索文件

Regular Expressions
grep: global regular expression print
grep [options] regex [file...]


literal charaters
metacharaters  ^ $ . [ ] { } - ? * + ( ) |  \

Note:As we can see, many of the regular expressions metacharaters are alse
characters that have meaning to the shell when expansion is perfermed.When we
pass regular expressions containing metacharaters on the command line, it is vital
that they be enclosed in quotes to prevent the shell from attemping to expand them


basic regular expressions  ^ $ . [ ] *
extended regualar expressions ( ) { } ? + |

echo 'AAA' | grep -E 'AAA|BBB|CCC'
grep -Eh '^(bz|gz|zip)' dirlist*.txt

? - Match An Element Zero Or One Time  "Make the preceding element optional"

[:upper:] [:lower:]  ---> gbm::预约  特殊含义  指定场景与含义解释
表示任意大小写与空格 [[:upper:][:lower:] ]
leading and trailing 开始的那个与结束的那个

* - Match An Element Zero Or More Times
used to denote an optional item, any number of times, not just once.

+ - Match An Element One Or More Times

{} - Match An Element A Specific Number of times
The { and } metacharaters are used to express minimum and maximum numbers of required matches.
{n} {n, m} {n,} {,m}

^\(?[0-9]{3}\)? [0-9]{3}-[0-9]{4}$
