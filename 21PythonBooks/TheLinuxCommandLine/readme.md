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
