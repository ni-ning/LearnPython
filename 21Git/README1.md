#### Git简介
1. Git是什么  

Git是最先进的分布式版本控制系统

2. Git诞生  

为了管理Linux源代码， Linus编写了分布式版本控制系统Git  

3. 集中式VS分布式  

集中式版本控制系统，版本库是集中存放在中央服务器，工作时需要用自己电脑从中央服务器取得最新的版本，工作完成后把代码推送给中央服务器。
特点：必须联网，安全性不高  

分布式版本控制系统，每个人的电脑上都是一个完整的版本库。工作的时候，就不需要联网，每个人都是完整的代码库。工作完之后，可以把代码推送到“交换”服务器。特点：安全性高，分支管理

#### 安装Git

1. CentOS

```
yum install git -y
```

2. Windows

从[https://git-for-windows.github.io](https://git-for-windows.github.io)下载，安装完成后，在项目文件下，右击 -> "Git Bash Here"，在命令行输入

```
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```
因为Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址

#### 创建版本库

版本库又名仓库，英文名repository，可以简单理解成一个目录，这个目录里面的所有文件都可以被Git管理起来，每个文件的修改、删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”


```
mkdir learngit
cd learngit
git init       # 初始化仓库
vim README     # 编辑文件
git add README # 添加文档到 Stage仓库，可以多次添加 
git commit -m 'first version'  # 把文档从Stage仓库，更新到分支
```

#### 版本回退

```
git status            # 查看仓库当前的状态
git diff readme.txt   # 查看文件变化

git log  # 显示从最近到最远的提交日志
git log --pretty=oneline
git reflog

git reset --hard HEAD^      # 回到上次版本，HEAD指向的版本就是当前版本
git reset --hard commit_id  # 回到特定版本
```

#### 工作区和暂存区

工作区（Working Directory）

版本库（Repository）  
Git版本库包括：Stage(暂存区)、Git自动创建的分支master以及指向master的一个指针HEAD

![image](http://images.cnblogs.com/cnblogs_com/jonathan1314/945576/o_0.jpg)

git add命令实际上就是把要提交的所有修改放到暂存区（Stage），然后，执行git commit就可以一次性把暂存区的所有修改提交到分支


#### 撤销修改


```
git checkout -- filename  # 用版本库里的版本替换工作区的版本，对应场景一
git reset HEAD filename   # 把文件从stage取撤回，对应场景二
```
场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令git checkout -- file，其中git checkout -- file命令中的--很重要，没有--，就变成了“切换到另一个分支”的命令

场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令git reset HEAD file，就回到了场景1，第二步按场景1操作。也就是说git reset HEAD file可以把暂存区的修改撤销掉（unstage），重新放回工作区

场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。


#### 删除文件

一是确实要从版本库中删除该文件

```
git rm test
git commit -m "remove test"
```

另一种情况是删错了，因为版本库里还有呢，所以可以很轻松地把误删的文件恢复到最新版本

```
git checkout -- test
```
git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。


#### 远程仓库

本地Git仓库和GitHub仓库之间的传输是通过SSH加密


```
ssh-keygen -t rsa
ls ~/.ssh/id_rsa  id_rsa.pub   # id_rsa.pub  拷贝到GitHub上
```


```
 git remote add origin git@github.com:Jonathan1314/test.git   # origin 表示远程
git push -u origin master  
```
注意：第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令  git push origin master


```
git clone git@github.com:Jonathan1314/test.git  # 从远程克隆一份
```
Git 支持多种协议，默认git://使用ssh

使用https除了速度慢以外，还有个最大的麻烦是每次推送都必须输入口令，但是在某些只开放http端口的公司内部就无法使用ssh协议而只能用https

