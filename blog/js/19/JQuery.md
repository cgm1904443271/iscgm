# JQuery
## 1.什么是JQuery
jQuery是一个快速、简洁的JavaScript框架，是继Prototype之后又一个优秀的JavaScript代码库（或JavaScript框架）。jQuery设计的宗旨是“write Less，Do More”，即倡导写更少的代码，做更多的事情。它封装JavaScript常用的功能代码，提供一种简便的JavaScript设计模式，优化HTML文档操作、事件处理、动画设计和Ajax交互。可以到http://www.bootcdn.cn/jquery/下载最新的jQuery。

	jQuery的核心特性可以总结为：具有独特的链式语法和短小清晰的多功能接口；具有高效灵活的css选择器，并且可对CSS选择器进行扩展；拥有便捷的插件扩展机制和丰富的插件。

## 2.引入方式
- 使用远程（cdn）
```js
<script src="//cdn.bootcss.com/jquery/1.11.3/jquery.js"></script>
```
- 使用本地的
```javascript
<script type="text/javascript" src="jquery-1.11.3/jquery.js"></script>
```
- 说明：
    - 远程引入方式，//表示自适应协议
    - min版是代码压缩后的，不带空格换行;是工作版;不压缩的是开发，研究版(常用的压缩工具：Grunt，gulp)
    - 使用jQuery一定要注明版本
    - 使用方式：
    ```javascript
    jQuery(document) .ready(function(){
    	alert(123);
    });

    //$ = jQuery
    $(document).ready(function(){
    	alert(456);
    });
    $(function(){
    	alert(456);
    });
    ```
     - $等于jQuery，代表jQuery对象
     - jQuery(document)是构造jQuery对象的方法
     - 大部分方法都返回jQuery对象，所以可以串联操作
     - ready方法在DOM加载后执行，不加载资源（图片，文件等）,可以绑定多个方法

## 3.选择器
- 标签选择器

- id选择器

- 类选择器

- 组合选择器

- 层级选择器
    - '>' 选中所有的儿子（不包括孙子）
    - '+' 选中紧邻的下一个指定类型的元素
    - '~'选中后面所有同辈的兄弟

- 基本选择器（伪类选择器）

- 内容选择器
    - has包含指定标签
    - contains包含给定文本
    - parent包含子元素或文本的元素

- 属性

    ~~~
    attr主要针对标签的自定义属性
    prop主要针对标签的固有属性
    ~~~

- 可见性

    - hidden   display是none，type的值是hidden
    - visible  元素的`visibility: hidden` 或 `opacity: 0`被认为是可见的

- 子元素

    - :first-child 第一个孩子必须是指定元素

- 表单 

## jQuery和js的转换
```javascript
//jQuery=>js对象
$('p')[0].style.color = 'red';

//js对象=>jQuery
var oBj = document.getElementById('bj');
$(oBj).css('font-size','50px');

//jQuer对象不能直接调用js中的属性和方法，只能掉jQuery的方法和属性

//
$('.nav input:eq(0)').click(function(){
	$('.d1 input').prop('checked',true);
	//在事件函数中,this代表的是js对象，$(this)是jQuery对象
	$(this).siblings().prop('checked',false);
})
```

## 样式添加
-   addClass    添加类名
  -removeClass 移除类名
  -toggleClass 切换类名
  -attr        获取属性和设置属性（一般针对自定义的特性）
  -prop        获取属性和设置属性(元素固有属性)
  -val         获取输入框的值
  -text        标签中的内容
  -html
  -css
  -width
  -height 
  -position
  -index
  -each 遍历
  ​
