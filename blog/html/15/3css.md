# css

## 5. 常用属性

- 单位

  - px  像素  绝对单位
  - em  相对单位，相对于父标签的大小
  - rem  相对于根标签（html)
  - %  相对于父标签的大小

- 颜色

  - 第一种方式：用单词表示  red、blue等

  - 第二种方式： #rrggbb（三原色）

    ```
    16进制表示 0-9 a-f(10-15)	  
    #ff0000 红
    #00ff00 绿
    #0000ff 蓝
    #c90  == #cc9900
    ```

  - 第三种方式：rgb(r,g,b)(r,g,b是10进制，0-255)  rgb(10%,20%,30%)  rgba(r,g,b,a(透明度))

- 宽高

  - width/height仅仅针对非行内元素

  - min-width max-width 用于响应式布局

    

## 6. 字体

```
font-style(normal,italic) 设置或去除斜体
font-weight(normal,bold)  字体加粗  也可以使用数值100~900
font-size(px,%，em rem) 设置字体
font-family 多种字体的话应该使用逗号隔开，如果第一种字体找不到，会使用第二种字体，以此类推。
	        font-family:黑体,仿宋,楷体,'Times New Roman'
color 字体颜色 颜色不能够简写
font简写(style || weight [size family]) 顺序不能错，但属性可以不出现
```

## 7. 文本属性

- text-indent  首行缩进  2em  20px（不推荐） -2em

- text-align  水平对齐  left center right，默认是left

- text-overflow（clip、ellipsis），这个属性需要配合overflow来使用，将overflow设置hidden

  ```
   p{
          text-indent: 2em;
          text-align: right;
          width: 300px;
          overflow: hidden;
          white-space: nowrap;  #不换行
  	   	   text-overflow: clip;
  }
  ```

- text-decoration（none、underline(下划线)、overline（上划线）、line-through（删除线） ）

- text-shadow   文本阴影

  ```
  text-shadow :水平偏移  垂直偏移  阴影模糊度  阴影颜色
  例如：text-shadow:5px 15px 10px blue;
  ```

- line-height:行高，一般把行高设置为容器高度，文本垂直居中

- vertical-align：由于很多浏览器不兼容这个属性，所以不推荐使用该属性。

  - 当碰见图片和文字水平布局的时候，使用这个属性。将文字行高设置和容器高度一样，将图片设置为垂直居中。

## 8. 背景

- background-color：背景色
- background-image :url("image/timg.jpg") 背景图片
- background-repeat：
  - repeat:重复背景（默认）
  - no-repeat：不重复背景图
  - repeat-x：水平方向重复背景图
  - repeat-y：垂直方向重复背景图
- background-position（top | center | bottom | left | center | right|x y）设置背景图像位置
  - x值：图片水平方向偏移的距离
  - y值：图片垂直方向偏移的距离
  - 坐标原点在图片左上角  向右是x正方向，下是y的正方向
- background-attachment
  - fixed设置图片不随窗口滚动而滚动
  - scroll：默认属性，背景图会随着内容的滚动而滚动
- background简写 :  background:url(1.jpg) no-repeat  20px 30px fixed red;

## 9. 列表

- list-style-type：none 去除项目符号

- list-style-image  设置项目符号图片

- list-style:none

  ```
  li{list-style: none;}
  ```

## 10. 布局(****)

- float(left,right,none)  漂浮，半脱离文档流 块里面的文字不会被覆盖，**重点掌握**

  - 在更高一层级来布局，不会影响原来的布局，但是会盖住父级上面的其他内容

- clear（left、right、both） 清除浮动 ，如果上面有浮动的元素，那么下面布局其他元素的时候会被浮动的元素盖住，这时候就需要清除浮动，从浮动元素的下面开始布局。

  ```
   1) 你在浮动额块后面的的块标签添加一个clear:both;
   2) 给需要清除浮动的标签添加一个父标签，父标签中添加一个类名：clear
   .clear:after{
  		display:block;
  		content:'';
  		zoom:1;
  		clear:both;
  }
  ```

- display（none、inline-block、block、inline）可以用于显示/隐藏，块、行内和行内块互相切换

  - inline-block：切换为行内块
  - block: 块
  - inline:行内◇
  - none: 隐藏，不显示，不占用位置

- visibility（visible、hidden）：让标签消失，但是位置依然存在

- overflow（visible、hidden、scroll、auto）当内容超出容器的宽度或者高度的时候：

  - visible：默认属性，显示出来
  - hidden：超出部分隐藏
  - scroll：显示滚动条，滚动显示
  - auto：自动显示滚动条

## 11 盒子模型

- 外边距

  ```
  margin-top
  margin-right
  margin-left
  margin-bottom
  margin简写 上右下左，没有的值可以用对边代替
  			-margin:200px 20px 100px 100px;
  			-margin:200px;/*上右下左都是200*/
  			-margin:200px 100px;/*上=下=200  右=左=100*/
  			margin:100px 30px 50px; 上=100 右=左=30 下=50 
  ```

- 内边距

  ```
  padding-top
  padding-right
  padding-bottom
  padding-left
  padding简写 上右下左
  ```

- 边框

  - border-width  宽度
  - border-style边框样式
    - none 无样式
    - dotted 点线
    - dashed 虚线
    - solid  实线
  - border-color 边框颜色
  - 简写：border:10px solid pink; 线宽  类型 颜色
  - border-radius 圆角半径
  - box-shadow 阴影
    - box-shadow: 水平偏移  垂直偏移  模糊度  颜色

## 12 定位

position(relative,absolute,static,fixed)

- 绝对定位：absolute

  - 1）完全脱离文档流
  - 2）相对于body 窗口定位
  - 3)行内元素会变成块

- 相对定位:relative

  - 1)不脱离文档流
  - 2）相对于自身原来的位置
  - 3）***如果父标签是相对定位，子标签是绝对定位，子标签是相对于父标签进行定位***

- fixed

  - 完全脱离文档流
  - 相对于当前可视区域

- z-index：这个属性的测试需要都为absolute或者fixed的才有效。数值越高，显示越靠前，针对浮动无效。默认值为0

- 如下属性只有当定位是relative、absolute、fixed时有效

  - top  right bottom   left

    ​

