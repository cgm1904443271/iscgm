# bootstrap

## 1.响应式布局
- 利用header头技术，根据客户端类型跳转不同网站
  - 利用_SERVER['HTTP_USER_AGENT']获取
  - 在js中使用navigator.userAgent获取
```
    //获得请求头中userAgent，在userAgent中包含客户端信息
     var sUserAgent = navigator.userAgent.toLowerCase();  
     var bIsIpad = sUserAgent.match(/ipad/i) == "ipad";  
     var bIsIphoneOs = sUserAgent.match(/iphone os/i) == "iphone os"; 
     ...
     if (!(bIsIpad || bIsIphoneOs ) ){  
         window.location.href="http://localhost/1702/high/22/1.php";
     }   
```
- 媒体查询
- 参数
    - 媒体查询标识 @media
    - and 条件 并且
    - min-width  最小宽度
    - max-width  最大宽度
    - min-height
    - max-height
- 使用方式：
```
//方式一 @media
<style type="text/css">
	@media screen and (max-width:768px) {
		div{width: 480px;height: 600px;background: red;}
	}
	
</style>

//方式二  @import导入
<style type="text/css">
    @import url(mini.css) screen and (max-width: 768px);
</style>

//方式三  使用link标签导入外部文件
<link rel="stylesheet" type="text/css" href="superBig.css" media="screen and (min-width:768px) and (max-width:1200px)">
```
- 像素和分辨率
```
<meta name="viewport" content="width=device-width, initial-scale=1">
```
- 常见屏幕尺寸
    - 手机  <768px
    - 平板  >=768, <992px
    - 桌面  >=992px, <1200px
    - 超大屏幕  >=1200px;
## 2.bootstrap
目前最流行的前端框架，官网：www.bootcss.com
- 下载文档
- 起步，下载用于生产环境的版本
- 复制基本模板，修改引入文件
- 基本说明：
    - h5文档类型
    - 设置viewport
- 容器布局
    - 固定尺寸：<div class="container"></div>		
    - 100%宽度：<div class="container-fluid"></div>

## 3.栅格系统
- 将整个宽度平均分成12等份，书写时只需写份数
- 指定一行：class="row"
- 指定宽度：class="col-md-份数"
- 指定偏移：class="col-md-offset-份数"
- 指定排序：class="col-md-push/pull-份数"
- 可以嵌套使用，内部会重新按照栅格系统分配
- xs(超小)、sm(小屏)、md(中型)、lg(超大)

## 4 应用
- 全局样式
    - 标题、表格、按钮...
- 组件 
- js插件
    - 模态框 
- layout it

