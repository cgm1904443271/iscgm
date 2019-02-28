## 1. 基础类库

- Date类
- String类
- Math类
- Array类

------

## 2. Dom

DOM（Document Object Model） 文档对象模型，**定义了访问和操作 HTML 文档的标准。**

 HTML DOM 定义了所有 HTML 元素的对象和属性，以及访问它们的*方法*。通过 HTML DOM，树中的所有节点均可通过 JavaScript 进行访问。所有 HTML 元素（节点）均可被修改，也可以创建或删除节点。

 ![ct_htmltree](image/ct_htmltree.gif)

**在 HTML DOM 中，所有事物都是节点。DOM 是被视为节点树的 HTML。**

- 整个文档是一个文档节点
- 每个 HTML 元素是元素节点
- HTML 元素内的文本是文本节点
- 每个 HTML 属性是属性节点
- 注释是注释节点

### 2.1 获取html元素

1. getElementById	

   - 通过标签的id属性获取单个元素，返回一个对象

   - 只能通过document获取

     ~~~
     var oDiv = document.getElementById('标签的id名');
     ~~~

2. getElementsByTagName

   - 通过标签名获取一组元素，返回一个元素伪数组

   - 它的父级可以不是document

     ~~~
     var oDiv = 父级.getElementsByTagName('标签名');
     ~~~

3. getElementsByClassName  

   - 通过标签的class属性获取多个元素，返回伪数组

   - 它的父级可以不是document

     ~~~
     var oDiv = 父级.getElementsByClassName  ('标签的类名');
     ~~~

4. getElementsByName  

   - 通过name获取，返回伪数组
   - 需要通过document调用


### 2.2  修改元素
- 获取到标签元素后可以修改标签的行内样式：

```
var oDiv = document.getElementById('div1');
oDiv.style.backgroundColor = 'red';
```
- 获取到标签后，可读取或修改标签的固有属性
- innerHTML  获取或设置标签中间html代码
- innerText 获取或设置标签中间的文本
- value 获取input的值
- display 控制对象是否显示和消失
- 修改类名使用className，实现换肤
  注意：
  - css中所有的属性在js中必须转换为小驼峰

| css中属性           | js中属性           |
| ---------------- | --------------- |
| background-color | backgroundColor |
| margin-left      | marginLeft      |
| padding-left     | paddingLeft     |
| font-size        | fontSize        |
| ....             | ......          |

## 3.查找元素

- parentNode  获得当前元素的父元素
- children 获得当前元素的所有子元素
- firstElementChild
- lastElementChild
- previousElementSibling
- nextElementSibling
- IE8
  - previousSibling 
  - nextSibling
  - firstChild
  - lastChild

## 4.增加删除元素

- 增加节点应遵循以下步骤：

  - 创建节点

    - createElement   创建节点，只属于document，参数必须是合法的标签名

    ```
    document.createElement('标签名');
    ```

  - cloneNode(boolean deep) 克隆当前节点，deep为true，则同时克隆当前节点的后代节点

  - 添加节点

    - appendChild     追加节点，在父节点的最后面追加一个节点
    - insertBefore    插入节点，插入到父对象下面的某个节点前面

    ```
    oUl.appendChild(oLi);//在父节点末尾追加一个节点
    oUl.insertBefore(oLi,jf);//第一个参数是要插入的节点，第二个是要在哪个节点前插入
    ```

- 删除节点

  - removeChild     删除节点，任何父节点象都可以删除子节点

  - 删除父节点所有的节点  

    ```
    父节点.removeChild(要删除的子节点)
    父节点.innerHTML = '';//全部删除
    ```

## 5.属性（property)和特性(attribute)

- 在标签里添加的自定义属性称之为**特性**，不能通过标签.属性名获取或设置

  - 获取特性可以使用getAttribute,设置可以使用setAttribute

- 使用js代码给标签动态添加的属性称之为**属性**，可以通过标签.属性名存取

- 只有标准属性(标签固有属性)才可同时使用标准方法和点号方法

- 对于自定义属性

  - 特性使用getAttribute,设置可以使用setAttribute
  - 代码内添加的属性用点号



## 6 事件

| 事件          | 触发时机                                         |
| ------------- | ------------------------------------------------ |
| window.onload | 当页面加载完成时自动执行（页面所有资源加载完毕） |
| onclick       | 点击的时候触发                                   |
| ondblclick    | 双击                                             |
| onmouseover   | 鼠标移到某元素之上                               |
| onmouseout    | 鼠标从某元素移出                                 |
| onmouseup     | 鼠标按键被松开                                   |
| onmousedown   | 鼠标按钮被按下                                   |
| onmousemove   | 鼠标被移动                                       |
| onfocus       | 元素获得焦点                                     |
| onblur        | 元素失去焦点                                     |

## 7.定时器

- 一次性定时器
  - 设置定时器：timer = setTimeout(函数,毫秒);
  - 清除定时器：clearTimeout(timer);
  - 只执行一次

- 周期性定时器
  - 设置定时器：timer = setInterval(函数,毫秒);
  - 清除定时器：clearInterval(timer);

效果：反选、联动全选、选项卡

## 作业

1. 实现如下图所示功能，点击上箭头，输入框数值增加，点击向下箭头数值减小，如果数值等于0，则不再减小

    ![num](image/num.png)

