# 第5天  环境变量和shell编程

## 1. 环境变量

环境变量用来存储工作环境信息的变量，主要分为系统全局变量和用户级全局变量

- 全局变量

  ~~~shell
  常见的全局环境变量 ： 
    PATH    指令的搜索路径
    HOME     用户的工作目录
    LOGNAME  用户的登录名
    PS1      命令提示符：root用户是#，普通用户是$
    PS2      附属提示符默认是>
    SHELL    当前系统shell类型
  #使用全局变量
  echo $PATH  #显示单个全局变量,注意使用全局变量，必须加$
  export name='hello' #设置新的全局变量
  
  #系统级全局变量
  这类变量对系统内的所有用户都生效，所有用户都可以使用这类变量。
  这类变量在/etc/profile文件中设置，只有root用户才能设置
  vim /etc/profile
  export a=100
  :wq #存盘退出，这个时候a不会立即生效，应该是有
  source  /etc/profile
  
  #单用户级全局变量
  在用户主目录内有三个文件 ~/.bash_profile、~/.bashrc和~/.profile 在这个文件中定义变量只针对当前用户，添加方式同系统级全局变量
  ~~~

- 设置PATH环境变量

  ~~~
  echo $PATH  #x显示全局PATH环境变量
  #1 临时设置
  PATH=$PATH:/home/csl  #将/home/csl添加到系统环境变量，只针对当前登录有效
  #2 对所有用户永久有效
  vi /etc/profile
  export PATH=$PATH:/usr/local/sysbench/bin 
  source /etc/profile
  
  #3.对登录用户有效
  # vi ~/.bashrc 在里面加入：
  export PATH=$PATH:/usr/local/mysql/bin
  source ~/.bashrc
  ~~~

## 2. shell编程

### 2.1 什么是shell

shell是一个命令解释器，将用户输入的命令解释给操作系统内核。

Shell既是一种命令语言，又是一种程序设计语言。作为命令语言，它类似于Windows下的cmd.exe，可以交互式地解释和执行用户输入的命令；作为程序设计语言，它定义了各种变量和参数，并提供了许多在高级语言中才具有的控制结构，但是Shell是不需要进行编译的，它是从脚本程序中一行一行的读取并执行命令。

Shell有两种执行命令的方式：交互式（Interactive），用户输入一条命令，Shell就解释执行一条；批处理（Batch），用户事先写一个Shell脚本(Script)，其中有很多条命令，让Shell一次把这些命令执行完，而不必一条一条地敲命令。

### 2.2 常见的shell类型

Linux 的 Shell 种类众多，常见的有：

(1) **BourneShell(sh)**：是由AT&T Bell实验室的 Steven Bourne为AT&T的Unix开发的，它是Unix的默认Shell，也是其它Shell的开发基础。Bourne Shell在编程方面相当优秀，但在处理与用户的交互方面不如其它几种Shell。

(2) **BourneAgain Shell (即bash)**：是自由软件基金会(GNU)开发的一个Shell，它是Linux系统中一个**默认**的Shell。Bash不但与Bourne Shell兼容，还继承了C Shell、Korn Shell等优点。

(3) **ash**：ash Shell是由Kenneth Almquist编写的，是Linux 中占用系统资源最少的一个小Shell，它只包含24个内部命令，因而使用起来很不方便。

(4) **CShell(csh)**：是加州伯克利大学的Bill Joy为BSD Unix开发的，共有52个内部命令，与sh不同，它的语法与C语言很相似。它提供了Bourne Shell所不能处理的用户交互特征，如命令补全、命令别名、历史命令替换等。但是，C Shell与BourneShell并不兼容。该Shell其实是指向/bin/tcsh这样的一个Shell，也就是说，csh其实就是tcsh。

(5) **KornShell(ksh)**：是AT&T Bell实验室的David Korn开发的，共有42 条内部命令，它集合了C Shell和Bourne Shell的优点，并且与Bourne Shell向下完全兼容。Korn Shell的效率很高，其命令交互界面和编程交互界面都很好。

(6) **zch**：是Linux 最大的Shell之一，由Paul Falstad完成，共有84 个内部命令。如果只是一般的用途，没有必要安装这样的Shell。

- 可以使用系统变量SHELL查看当前使用的shell：echo $SHELL
- 也可以到/etc/shells文件里查看系统可以使用的shell

### 2.3 shell的交互方式

- 命令行

- 脚本执行

  - 编写脚本，文件后缀名一般为.sh
  - 文件必须以#!/bin/bash开头
  - 添加脚本的可执行权限`chmode +x 脚本名`
  - 执行脚本：
    - 在当前目录里执行：`./脚本名`
    - 在其他目录中执行：使用绝对路径

  ~~~
  #!/bin/bash
  #使用#注释，第一行是特殊存在
  cd /
  ls -al
  
  :wq #存退出盘
  chmod a+x 1.sh  #修改权限,添加可执行权限
  ./1.sh   #执行当前目录下的shell脚本
  ~~~

### 2.4 定义变量

  - 变量类型

    - 局部变量：只在本shell中使用
    - 环境变量 ： 整个系统使用，一般大写

  - 局部变量的使用

    ~~~
    #1 定义局部变量
    a=10 #注意等号两边不要留空格，否则会看成多个命令
    b=$a
    
    #2显示局部变量
    echo $b
    echo ${b}
    echo "a=$a"  #双引号中的变量解释
    
    #3.销毁变量
    unset a #干掉一个变量，不要带$符
    #注意反引号，反引号引起来的是命令，可以执行，将执行结果给变量
    d=`date`
    
    注意：等号两边不要留空格
    ~~~

    - 位置变量

      ~~~
      $0 表示脚本的名称
      $1-$9表示传递给脚本的的参数
      
      #test.sh脚本
      #!/bin/bash
      echo 'hello world'
      echo $0
      echo $1 $2
      
      执行输出：
      hello world
      ./test.sh
      1 2
      ~~~

    - 特殊变量

      ~~~
      $#表示传递给脚本的参数个数
      $*表示传递给脚本的所有参数
      $?表示命令的返回值，返回值为0表示成功执行，否则命令执行错误
      ~~~

    - 常量

    ~~~
    readonly a=10  #定义常量
    echo $a
    a='ll'  #-bash: name: 只读变量,不能修改
    ~~~

### 2.5 引号

- 双引号中解释变量，解释转义字符
- 单引号不解释变量、不解释转义字符
- 反引号会执行当中的内容
- 特殊字符要用反斜线转义：&  * ？| $  ^

### 2.6 字符串

- 计算字符串长度`${#字符串名}`
- 提取子串:`${字符串名:start:len}`从下标为start开始，提取len个字符

### 2.7 运算

- 数学运算

~~~
shell默认所有变量都是字符串，执行数学计算需要用[]括起来
a=100
echo $[$a+10]
echo $[$a / 2]
echo $[$a * 2]
echo $[$a - 80]
echo $[10 % 2]

echo $((3 + 5))
echo $((10/2))
echo $((10/3))  #3 整除
echo $((10*3))
echo $((10%3))

let a=5+6
echo $a
let a+=10
echo $a

echo `expr 3 + 5`  #也可以用expr进行计算
~~~

- 关系运算

  | 运算符 | 说明                        | 举例                          |
  | ------ | --------------------------- | ----------------------------- |
  | -eq    | ==，相等返回 true。         | [ `$a -eq $b` ] 返回 false。  |
  | -ne    | !=，不相等返回 true。       | [ ` $a -ne $b ` ] 返回 true。 |
  | -gt    | `>`，如果是，则返回 true。  | [ `$a -gt $b` ] 返回 false。  |
  | -lt    | <，如果是，则返回 true。    | [ `$a -lt $b` ] 返回 true。   |
  | -ge    | `>=`，如果是，则返回 true。 | [ `$a -ge $b` ] 返回 false。  |
  | -le    | `<=`，如果是，则返回 true。 | [ `$a -le $b` ] 返回 true。   |

- 逻辑运算

  | 运算符 | 说明       | 举例                                        |
  | ------ | ---------- | ------------------------------------------- |
  | &&     | 逻辑的 AND | [[ `$a -lt 100 && $b` -gt 100 ]] 返回 false |
  | \|\|   | 逻辑的 OR  | [[ $a -lt 100\| $b -gt 100 ]] 返回 true     |

- 字符串判断

  | 运算符 | 说明                                      | 举例                       |
  | ------ | ----------------------------------------- | -------------------------- |
  | =      | 检测两个字符串是否相等，相等返回 true。   | [` $a = $b` ] 返回 false。 |
  | !=     | 检测两个字符串是否相等，不相等返回 true。 | [ $a != $b ] 返回 true。   |
  | -z     | 检测字符串长度是否为0，为0返回 true。     | [ -z $a ] 返回 false。     |
  | -n     | 检测字符串长度是否为0，不为0返回 true。   | [ -n "$a" ] 返回 true。    |
  | str    | 检测字符串是否为空，不为空返回 true。     | [ $a ] 返回 true。         |

- 文件判断

  | 操作符  | 说明                                                         | 举例                      |
  | ------- | ------------------------------------------------------------ | ------------------------- |
  | -d file | 检测文件是否是目录，如果是，则返回 true。                    | [ -d $file ] 返回 false。 |
  | -f file | 检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 | [ -f $file ] 返回 true。  |
  | -r file | 检测文件是否可读，如果是，则返回 true。                      | [ -r $file ] 返回 true。  |
  | -w file | 检测文件是否可写，如果是，则返回 true。                      | [ -w $file ] 返回 true。  |
  | -x file | 检测文件是否可执行，如果是，则返回 true。                    | [ -x $file ] 返回 true。  |
  | -s file | 检测文件是否为空（文件大小是否大于0），不为空返回 true。     | [ -s $file ] 返回 true。  |
  | -e file | 检测文件（包括目录）是否存在，如果是，则返回 true。          | [ -e $file ] 返回 true。  |

### 2.8 分支语句

- if-else

  ~~~
  a=100
  if [ $a -gt 90 ];then
      echo "a>90"
  else
      echo "a<=90"
  fi
  ~~~


### 2.9 循环语句

```shell
for 变量 in 列表
do
    command1
    command2
    ...
    commandN
done

示例：
for i in 1 2 3 4 5;do
	echo $i
done

#从命令读取值
for line in `cat 1.txt`;do 
    echo $line
done

#读取目录列表
for file in ~/*;do 
	echo $file; 
done
```

- while

~~~
#当型循环
while condition
do
    command
done

sum=0
i=0
while [ $i -lt 10];do
   let sum+=$i
   let i+=1
done
~~~

### 2.10 函数

- 函数必须先定义后使用

~~~
#函数定义
test()
{
    echo "简单函数"
}
#函数调用
test
~~~

## 3 远程复制

- 建立主机间的信任关系

  ~~~
  1.生成密钥对
  ssh-keygen  #生成密钥对，按三次回车，在家目录下有一个隐藏目录.ssh，会有两个文件，id_rsa 私钥，id_rsa.pub 公钥

  2.到对方的主机上家目录里创建.ssh目录，并且在.ssh下生成一个authorized_keys一个文件(建议使用ssh-keygen声明.ssh)
  vi authorized_keys  

  把你机子上id_rsa.pub的内容复制过来
  chmod 600 authorized_keys

  3 再使用ssh -p 端口 用户名@x.x.x.x 就可以免密登录

  ~~~

- 远程复制

~~~
scp [-r] 原地址   目标地址

本地到远程
scp ~/1.txt root@10.11.59.76:/data  
scp -r /data/www  root@10.11.59.76:/data/tmp  #目录拷贝

远程到本地
scp -r root@10.11.59.76:/data/test /data/
~~~

## 4. samba服务器

samba服务器作可以windows和linux交互的媒介，可以让windows用户轻松地在电脑上使用图形界面访问linux文件系统。

```
# 1.安装
sudo apt-get install samba samba-common

# 2.建立共享目录
mkdir /home/python/share  
chmod 777 /home/python/share

#3 添加samba用户
sudo useradd sambuser
sudo smbpasswd  -a   sambuser # 输入两次密码

# 4.修改配置文件
sudo vim /etc/samba/smb.conf
在末尾添加：
[myshare ]   #共享目录名，不必和真实目录名同名
comment=This is samba dir    # 共享目录描述
path=/home/python/share      # 共享目录路径
writeable=yes                # 目录可写
valid users=sambuser         # 可登陆的用户
browseable=yes               # 可以浏览
# 5.重启服务
sudo service smbd restart   # start  stop

# 6.windows下访问
在开始运行输入：\\ip\myshare
然后输入用户名和密码就可以看到共享目录了
```



## 5. screen

在linux多窗口，多任务

```
sudo apt-get -y install screen
screen -S 窗口名字
screen -r  窗口名  进入指定窗口
screen -X -S 窗口名 quit 退出会话
常用快捷键:
   ctrl + a + d   #退出会话
   ctrl + a + c  #创建一个新窗口
   ctrl + a + n  #显示下一个窗口
   ctrl + a + p  #显示上一个窗口
   ctrl + a + w  #显示所有窗口
   ctrl + a + k  #关闭当前窗口,先按ctl+a,然后松开，1秒后按k
```

## 