
#### 分支管理

1. 创建与合并分支
```
git branch dev      # 创建分支dev
git checkout dev    # 切换到分支dev
git checkout -b dev # 创建并切换到分支 dev
git branch          # 查看当前分支，*号标识
git merge dev       # 在当前分支合并 dev
git branch -d dev   # 删除分支dev
```
因为创建、合并和删除分支非常快，所以Git鼓励使用分支完成某个任务，合并后再删掉分支，这和直接在master分支上工作效果是一样的，但过程更安全。

2. 解决冲突


```
git checkout -b feature1  # 创建新分支 feature1
echo  "Creating a new branch is quick AND simple." >> readme.txt
git add readme.txt 
git commit -m "AND simple"

git checkout master  # 切换到主分支 master
echo  "Creating a new branch is quick & simple." >> readme.txt
git add readme.txt 
git commit -m "& simple"


git merge feature1  # 在当前主分支master合并分支 feature1

```
出现冲突，需手动解决  Git用<<<<<<<，=======，>>>>>>>标记出不同分支的内容


```
git log --graph --pretty=oneline --abbrev-commit   # 看到分支的合并图
git branch -d feature1  # 删除分支 feature1
```

3. 分支策略

- master分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活
- 新建分支dev，在上面完成新功能，然后分支dev合并到master上
- 每个人都有自己的分支，时不时地往dev分支上合并就可以了

4. Bug分支

每个bug都可以通过一个新的临时分支来修复，修复后，合并分支，然后将临时分支删除

但是当前在dev上工作没完成？

```
git stash             # 当前dev工作现场“储藏”起来，等以后恢复现场后继续工作

git checkout master   # bug出现在master分支上，开始修复

git checkout -b issue-101
git add readme.txt 
git commit -m "fix bug 101"
 
git checkout master    # 修复完在主分支上合并
git merge --no-ff -m "merged bug fix 101" issue-101
git branch -d issue-101

git checkout dev       # 返回到原先工作分支 dev，进行恢复
git status
git stash list
git stash apply stash@{0} # 恢复后，stash内容并不删除
git stash drop            # 删除

git stash pop              # 恢复的同时把stash内容也删了
```

5. Feature 分支


```
 git checkout -b feature1
 git branch -D feature1  # 强制删除功能分支 feature1
```
 
#### 多人协作

当你从远程仓库克隆时，实际上Git自动把本地的master分支和远程的master分支对应起来了，并且，远程仓库的默认名称是origin


```
git remote -v  # 远程库的详情信息
```

1. 推送分支

推送分支，就是把该分支上的所有本地提交推送到远程库

```
git push origin master  
git push origin dev     

```
- master 主分支 要时刻与远程同步 
- dev 开发分支，团队所有成员都需要在上面工作，所以也需要与远程同步
- bug分支只用于在本地修复bug，就没必要推到远程了
- feature分支是否推到远程，取决于你是否和你的小伙伴合作在上面开发。


2. 抓取分支


```
git clone git@github.com:Jonathan1314/test.git  # 本地默认 master分支
git checkout -b dev origin/dev  ???

git push origin dev
# 如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并
git pull

# 如果git pull提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建
git branch --set-upstream dev origin/dev
```


#### 标签管理

标签也是版本库的一个快照，tag就是一个让人容易记住的有意义的名字，它跟某个commit绑在一起

1. 创建标签


```
git checkout master # 切换到相应分支上
git tag v1.0        # 创建tag
git tag             # 查看tag列表

# 如果忘了打标签，根据以往commit_id打标签
git log --pretty=oneline --abbrev-commit
git tag v0.9 6224937
git show v1.0      # 查看标签详情
```
标签不是按时间顺序列出，而是按字母排序的

2. 操作标签


```
git push origin v1.0    # 推送某个标签到远程
git push origin --tags  # 一次性推送全部尚未推送到远程的本地标签

git tag -d v0.7         # 删除本地标签
git push origin :refs/tags/v0.7   # 而后删除远程标签
```


#### 忽略配置文件

主目录下新增.gitignore 格式参考https://github.com/github/gitignore









