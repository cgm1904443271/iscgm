# html


## 1. html工作原理

- 原理 

![html工作原理](html工作原理.png)



- html是hypertext markup lanaguage缩写 超文本标记语言，是一种解释性语言，不需要编译，由浏览器解释执行
- html组成
  - html 负责数据展示
  - css 负责美化页面
  - js  页面的动态效果
- 动态网页和静态网页的区别
  - 如果不修改页面源码，页面一成不变，就是静态页面
  - 动态页面，服务器从数据库提出数据临时生成的，会根据时间、是否登录不同，而页面内容也不同
- 开发工具
  - sublime  、vim、note pad++
  - chrome浏览器

##2. 认识标签

marquee标签的引入，学习标签应该：

- 记住功能

- 标签写法

  - 可分为：单标签和对标签

    ~~~html
    <!--单标签 -->
    <标签名 属性1='属性值'  属性2="属性值"  属性3=属性值>
      
    <!--对标签 -->
     <标签名   属性1='属性值'  属性2="属性值"  属性3=属性值>内容</标签名>
    ~~~

- 注意事项

  - 标签不能创造
  - 书写标签的时候应该用英文半角
  - 属性值可以单引号、双引号引起来，也可以不写引号，推荐使用单引号括起来
  - 属性必须写在开始标签里
  - 标签可以嵌套，一个标签要完全嵌套到另外一个标签里


##  3. 全局架构标签（重点）

~~~html
<!doctype html>   文档类型，html表名是html5的文档
<html>   根标签
<head>   头部
	<meta charset="UTF-8"> 告诉浏览器用utf-8编码格式解释文档
	<title>Document</title>  文档标题
</head>
<body>
	
</body>
</html>
~~~

### 3.1 title标签     

​    设置文档标题，显示窗口的标题栏   

### 3.2 设置字符集 

​    字符集是告诉浏览器用那种编码格式解读html文档，注意html文档本身有一个编码格式，这两个编码格式必须一致，不一致就乱码

### 3.3 body

内容显示区，有些常用属性：

-   topmargin 上外边距
-   leftmargin 左外边距
-   text 文字颜色
-   bgcolor 背景颜色
-   background 背景图片，和bgcolor冲突，设置了背景图片，背景颜色就是不显示

### 3.3 全局属性

​	每一个标签都有的属性，常用的有id、class、name、style

## 4 html常用标签

-   html文件显示特点：多个空格、换行、tab键用一个空格代替；如果英文字符间没有空格，会看成一个单词，不会自动折行

### 4.1 常用标签

-   h1~h6   标题，一般一个页面只设置一个h1标题
-   hr （单标签） 水平分割线
    -   width  可以使用绝对值，300，不带单位，也可以使用百分比 50%
    -   align 对齐方式：left  center（默认） right
-   p 段落标签，有段前间距和段后间距
-   br （单标签） 换行
-   nobr （双标签） 不换行，所修饰内容无论多长，不会自动换行，显示不下，会有滚动条
-   pre  保持原来的样式，无论空格还是换行都会正常显示
-   b（strong)  加粗
-   i（cite,em）  斜体
-   u  下划线
-   sub/sup  下标/上标，看圈在那边，在下边就是下标
-   font (face/color/size) 字体
    -   face  字体名称，到window目录下font子目录下查看
    -   color 字体颜色
    -   size  值取1~7,7最大
-   blockquote  引用，会从正常的文本中分离，留有左右边距

### 4.2 注释和实体引用

-   注释  

    ~~~
    <!--我是注释 -->
    <!--
    我是注释 

    -->
    注释的作用：
    1 提高代码的可读性，主要给其他团队成员看的，方便维护
    2 方便调试
    ~~~

-   实体引用  

    ~~~html
    空格    &nbsp;
    <       &lt;
    >       &gt;
    &       &amp;
    "       &quot;
    '       &apos;
    ~~~

## 5. 列表

### 5.1 有序列表（ol/li）

-   type: 数字，a ,A,I ,i
-   start 开始标号，默认从1开始

### 5.2 无序列表(ul/li)

-   type 项目符号：
    -    disc 默认  实心圆圈
    -    square  实心方块
    -    circle   空心圆圈

### 5.3 自定义列表（dl/dt/dd)



## 6. 超级连接（重点）

-   超链接的写法

    ~~~
    <a href="http://www.baidu.com/">百度</a>
    ~~~


-   url 统一资源定位符

    ~~~
    https://baike.baidu.com：80/item/%E6%9D%A8%E5%B9%82/149851?fr=aladdin#4
    第一部分： 协议   http   https  ftp  news  magnet（磁力链接）
    第二部分：主机，服务器地址   可以是域名或ip地址
    第三部分：冒号后面的数字，端口  http 80(默认)  https :443  ftp:21  mysql：3306
             端口编号从0~65535 其中0~1023归操作系统使用
    第四部分：从端口后的斜线到？，中间这部分叫路径，请求文件的路径
    第五部分：从？到#中间这部分，是请求参数，query string ；写法： 键=值&键2=值
    第六部分：锚点 也就是同一个页面内的跳转，必须用#开头
    ~~~

-   href  所请求的url，注意url必须写协议

-   title   鼠标放到超链接上时显示的提示

-   target  

    -   _blank  新窗口打开
    -   _self  当前窗口打开，默认

-   锚点 

    ~~~html
    定义锚点
    <a href='#锚点名'>跳转提示</a>
    ....
    <a name='锚点名'></a>

    本页面锚点
    <a href="#3">跳转到锚点</a>

    跨页面锚点
    <a href="https://baike.baidu.com/item/%E6%9D%A8%E5%B9%82/149851?fr=aladdin#4">杨幂</a>
    ~~~

## 7. img标签（单标签）

​	img是单标签，`<img src=''  title=''  alt='' border='' width='' height=''>`

-   绝对路径和相对路径

    ~~~
    本机绝对路径：file:///C:/python/web/1/ym.jpg
    网络绝对路径：https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=32ceb0ef04d79123f4ed9c26cc5d32e7/7c1ed21b0ef41bd55520081359da81cb38db3de2.jpg
    网站绝对路径（了解）：  /代表网站根目录

    相对路径：相对于html文档所在目录  ../上级目录 ./当前目录  ./3/index.html    ../1.html
    ~~~

-   src 图片来源，可以是相对路径也可以是绝对路径

-   title  图片提示文字

-   alt   图片不显示的时候的提示文字

-   border 图片边框大小，一般默认为0

-   width/height  一般只设置一个，另外一个等比例缩放



## 8. 视频和音频

这两个标签都是对标签

-   视频  

    -   src  视频来源，写法同img的src
    -   controls  控制面板
    -   loop   循环播放
    -   autoplay  自动播放
    -   width/height    宽高，只设置一个

-   音频

    -   src /controls/loop/autoplay

## 9. 表格

-   table  表
    -   border   表格线
    -   cellspacing：单元格的间距
    -   cellpadding：单元格到内容距离
    -   align：水平对齐  left、center、right
    -   height可以不用设置，自动撑开
-   tr 行
    -   align :水平对齐  left  center  right
    -   valign：垂直对齐 top middle  bottom
    -   注意：如果没有给该表格设置高度，那么设置valign无效,在以后布局页面的时候，一般不使用valign，只有一种情况使用到，就是图片和文字并排排放的时候，需要设置图片的valign为middle
-   td 单元格
    -   colspan   跨列  向右合并
    -   rowspan  跨行 向下合并
    -   width/height
-   th 
    -   就是表格的表头，内容会加粗，和td用法相同
-   caption 表格标题，跟随表格移动

## 10. 表单（重要）

- 用途：收集用户信息，提交给服务器

- 基本使用

    - 不是所有的标签都可以提交，能够向服务器提交信息的表单项，只有表单项：input、select、textarea才可以向服务器提交信息

    - 表单项必须放到form标签中才可以提交信息

    - action：提交地址，一般是服务器的页面

    - method：提交方式，最重要的两种为get方式和post方式，默认是get提交

      ~~~
      get和post的区别：
      1.get用于向服务器请求数据，post一般用于向服务器提交数据
      2. get请求通过url传递数据，数据会暴露在浏览器地址栏里，不安全；
         post请求数据在请求体中，不会在浏览器地址栏里出现，相对安全
      3. get传参，数据大小受url限制，一般几k大小
         post传参理论上无限制
      ~~~

    - enctype：用于文件上传，值为：multipart/form-data，现在了解

- input框

    - 公有属性：type、name、value、readonly、disabled、size
      -   type 类型：单行文本框（text）、密码框（password）、复选框（checkbox）、单选框（radio）、文件上传（file）、按钮（button）、重置按钮（reset）、提交（submit)
      -   name：  名称，要提交，必须设置name
      -   value    默认值
      -   readonly   只读
      -   disabled  不可用
      -   size

    - 单行文本框
      -   type： text
      -   placeholder：占位符，一般用于提示用户，当用户输入时，会自动消失
      -   maxlength： 最大字符数

    - 提交按钮
      -   type：submit
      -   value：提交按钮的标题

    - 重置按钮
      -   type：reset

    - 密码框
      -   type：password

    - 单选框

      一般用于多选一，name相同是一组，一组中只能选一个

      -   type：radio
      -   checked：是否选中
      -   value： 一般用0或1表示，必须设置，否则服务器无法区别选中是哪一个

    - 复选框

      一般name值相同

      -   type：checkbox
      -   value：必须设置
      -   checked: 是否选中

    - 文件上传
      -   type：file

    - 隐藏按钮

      一般用于提交无需用户输入的数据

      -   type：hidden
      -   name和value值必须设置

    - button  一般配合js代码使用

- 下拉框（select）

    -   name 必须设置
    -   size：显示的行数，如果设置这个属性，下拉框会变成列表框
    -   multiple：是否可以选择多行
    -   下拉框选项（option）
        -   selected：是否选中
        -   value  需要设置，否则值就是option中间的文字

- 多行文本（textarea）

    -   cols：列数
    -   rows：行数
    -   注意textarea标签的内容不能有任何值，否则便会显示

- label标签

    -   配合radio、checkbox使用，方便用户选中

    ~~~
    <input type='radio' name='sex'  value='男' checked id='man'> <label for='man'>男</label>
    ~~~


## 11. iframe

内联框架，它的作用是在一页网页中间插入一个框窗以显示另一个文件。 

~~~
<iframe src="iframe.html" name="test"  width="300" height="100"  scrolling="Yes"></iframe>
~~~

- src="iframe.html" 

  欲显示於此框窗的文件来源除档案名称，必要加上相对或绝对路径。 

- name="test" 

  此框窗名称，这是连结标记的 target 参数所　要的， 

- width="300" height="100" 

  框窗的宽及长，以 pixels 为单位。 

- scrolling="Yes" 

  使用 Yes 表示容许卷动（内定）， No 则不容许卷动。

## 12. 头元素标签

-   链接外部的css样式

    ~~~
    <link rel="stylesheet" type="text/css" href="文件名" />	
    ~~~

-   堆积网站关键字，用来提高网站的排名

    ~~~
    <meta name="keywords" content="" />	
    ~~~

-   网站描述信息

    ~~~
    <meta name="description" content="" />
    ~~~

-   页面自动跳转

    ~~~
    <meta http-equiv="refresh" content="秒数;url=地址" >
    ~~~

## 13. 布局标签

- div
- span
- header、section、footer
- 标签分类
    - 块标签

        -   独占一行
        -   可以设置宽高

        ~~~
        h1~h6   ul ol dl li p table  tr  form  div  header section footer
        ~~~

    - 行内

        -   不独占一行
        -   不能设置宽高，宽高有内容决定

        ~~~
        a b i u strong  em cite  span
        ~~~

    - 行内块

        - 不独占一行
        - 有宽高

        ~~~
        input select textarea  
        ~~~

        


作业：
1）仿作大连民心网：<http://www.mxw.gov.cn/comp/jb_step2.html?tsly=pc&sqfl=1#pos_2&m=&openid=&id=5> 

2）编写表格

