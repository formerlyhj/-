# GIT作业  
1、以容易理解的格式列出/home 目录中所有以”d”开头的文件目录的大小  
![avatar](https://gitee.com/forhejian/git_notetaking_test.git)  
2、列出/home 目录中所有以”s”开头的目录。  
![avatar](https://gitee.com/forhejian/git_notetaking_test.git)  
3、删除后缀名为.log 的所有，删除前逐一询问  
![avatar](https://gitee.com/forhejian/git_notetaking_test.git)  
5、找你的用户目录下面的所有py文件,ls -l 查看他们的属性,然后把这些结果输入到一个文件之中  
![avatar](https://gitee.com/forhejian/git_notetaking_test.git)  
6、使用ls查看根目录 并且每行显示3个信息  
![avatar](https://gitee.com/forhejian/git_notetaking_test.git)  
7、查看所有进程信息,只查看前3行  
![avatar](https://gitee.com/forhejian/git_notetaking_test.git)
8、分析以下问题,并给出解决方案
Mount is denied because the NTFS volume is already exclusively opened.
The volume may be already mounted, or another software may use it which could be identified for example by the help of the 'fuser' command.
有应用程序或者进程正在使用，可以ps –ef查到进程号，用kill杀掉
9、ssh 服务端口是多少,ssh免密登录方式的原理是什么
ssh服务端口是22，
-p 22 默认是有的
ssh免密登录：ssh-keygen生成公匙和私匙，然后本地端和远程端交换公匙和私匙，相当于互相信任，ssh-copy-id
10、权限755代表什么权限,如果我想把所有的w权限去除应该使用什么命令
权限755：rwxr-xr-x
chmod 555 file

