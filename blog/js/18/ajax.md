## 1. Ajax
AJAX即“Asynchronous Javascript And XML”（异步JavaScript和XML），AJAX 是一种用于创建快速动态网页的技术。
通过在后台与服务器进行少量数据交换，AJAX可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

**必须通过服务器运行页面才能使用ajax的功能**

![ajax](ajax.jpg)

## 2. Ajax使用
- 第一步，创建ajax对象
    - 高级浏览器，包括火狐、chrome、opera，ie7以上
    ```js
    var xhr = new XMLHttpRequest();
    ```
    - ie7及以下
    ```js
    var xhr = new ActiveXObject("Microsoft.XMLHTTP");   //垃圾浏览器的方式
    var xhr = ActiveXObject("Microsoft.XMLHTTP");
    var xhr = new ActiveXObject("Msxml2.XMLHTTP.3.0");  
    var xhr = new ActiveXObject("Msxml2.XMLHTTP.5.0");  
    var xhr = new ActiveXObject("Msxml2.XMLHTTP.6.0");  //IE维护的最高版本
    ```

- 第二步，创建HTTP请求
    - 使用XMLHttpRequest对象的open创建请求
    ```js
    /*参数说明：
    method：该参数用于指定HTTP的请求方法，一共有get、post、head、put、delete五种方法
            ，常用的方法为get和post。
    URL：该参数用于指定HTTP请求的URL地址，可以是绝对URL，也可以是相对URL。
         该文件可以是任何类型的文件，比如 .txt 和 .xml，或者服务器脚本文件，比如 .asp 和 .php（在传回响应之前，能够在服务器上执行任务）。
    flag：该参数为可选参数，参数值为布尔型。该参数用于指定是否使用异步方式。
          true表示异步方式、false表示同步方式，默认为true。
    name：该参数为可选参数，用于输入用户名。如果服务器需要验证，则必须使用该参数。
    password：该参数为可选参数，用于输入密码。
    XMLHttpRequest.open(method,URL,flag,name,password);
    */
    //例
    xhr.open('get','2.py?username=tom&pwd=123');
    ```

    - 如果是get请求，参数需要附加到url里

- 第三步，发送请求
    - 如果是get请求，send参数可以为空；
    - 如果为post请求，参数必须在send参数中传递，参数格式和url中设置的一样
    - 如果为post方式需要在send前，设置请求头信息：xmlHttp.setRequestHeader("Content-Type","application/x-www-form-urlencoded")
    ```js
    //get方式
    xhr.send(null);

    //post方式
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
    xhr.send('username=tom&pwd=123');
    ```
- 第四步，监听Ajax状态变化
  向服务器发送请求的目的是为了获得服务器端的数据，要获得服务器端返回的数据，需要监听XMLHttpRequest的状态，每当XMLHttpRequest状态发生改变时，会触发事件onreadystatechange，我们可以编写onreadystatechange事件处理函数，获取服务器返回的数据。
    - XMLHttpRequest对象的状态，可以通过属性readyState获取，公有以下5种状态：
        - 0: 请求未初始化
        - 1: 服务器连接已建立
        - 2: 请求已接收
        - 3: 请求处理中
        - 4: 请求已完成，且响应已就绪 
    - 当readyState值为4时，就可以获取返回数据了，但返回的数据是成功还是失败，需要根据http的状态码确定，XMLHttpRequest的status属性用于判断http的状态，200表示访问成功
    ```js
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
    		if (xhr.status == 200) {
    			alert(xhr.responseText);
    		}
    	}
    };
    ```
- 第五步，获取响应数据
    - 可以通过XMLHttpRequest对象的responseText获取数据，现在已经不再使用responseXML获取数据了
    - 客户端获取json数据
    ```js
    xhr.onreadystatechange = function () {
    	if (4 == this.readyState && 200 == this.status) {
    		//1.通过eval将json字符串转换为对象 
    	   // var obj = eval('('+xhr.responseText+')');
    	   // console.log(obj);

    	   //2 使用json.parse将json字符串转换为对象
    	   obj = JSON.parse(this.responseText);
    	   console.log(obj);
    	}
    };
    ```
    - JSON字符串和JSON对象的转换
        ```js
        //json字符串 ==> json对象
        var obj = JSON.parse(json字符串);

        //或者
        var obj = eval('(' + json字符串 + ')');

        //json对象转json串
        var str=obj.toJSONString();
        //或
        var str=JSON.stringify(obj); 
        ```


## 第六步，局部更新客户端页面
## 3. 同步异步
- 同步： ajax请求数据时，客户端js代码必须等服务器返回请求的结果后再继续执行
- 异步： ajax请求数据时，客户端js代码不必等候ajax请求的结果，可以继续执行，啥时候ajax请求返回数据在进行处理。
- 同步请求是onreadystatechange事件处理绑定必须在open前，否则错误。

## 4. 跨域

- 一个网站不能使用ajax来访问另一个网站的数据，这样的话会被浏览器给阻止，这个问题我们通常叫做跨域问题。

  哪怕是同一个域名下的二级域名也不行。

- ajax不允许跨域访问

  - 域名组成   http:// www . google : 8080 / script/jquery.js

    - http:// （协议号）
    - www  （子域名）
    - google （主域名）
    - 8080 （端口号）
    - script/jquery.js （请求的地址）

  - 当协议、子域名、主域名、端口号中任意一个不相同时，都算不同的“域”。

  - 不同的域之间相互请求资源，就叫“跨域”。

    ```
    跨域访问：
    Failed to load http://www.test.com/index.py?rand=0.000729056685777163&: No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://localhost' is therefore not allowed access.
    ```

- 解决跨域问题的方式：

  - jsonp方式 
    - 后端需要返回函数调用字符串，函数的参数就是json格式的字符串，在前端定义这个函数，然后通过`<script src='xxx'></script>`将其引入进来，然后就会直接执行定义好的那个函数
    - src属性本身没有跨域的限制



## 5. 自学json

http://www.runoob.com/json/json-intro.html



## 作业

写一个登陆验证页面，如果用户名和密码正确，跳转到首页，否则跳转到失败页。

接口：v2接口

​          参数：username  用户名，字符串

​                      password  密码，字符串

​         返回值：

​                   

      登陆成功返回json串:
    {
        code: 0 ,
     	message: '登录成功'
    }
    
    登陆失败：
    {
    	code: 1 ,
    	 message: '登录失败'
    
    }

​ 



