## 1. 结构说明

前端参考代码： 项目前端的参考代码，基于此前端开发

电子商务书记词典：数据库设计表

电子商务系统需求分析：项目的完成目标



## 2. 设计说明

本系统采用前后端分离的方式实现，前后端通过Restful接口进行通信。通信的数据格式严格按以下json数据实现：

```json
{
    "success": true,
    "message": "",
    "data": {}
}
```

必要的三个字段 success，message，data，其中各字段作用如下：

success： 执行成功或失败

message： 失败时不为空，填充失败原因

data： 所携带的前端需要的数据



## 3. 资料

前端教程网页地址： https://www.imooc.com/video/1452

后台教程网页地址：https://www.imooc.com/learn/148



## 4. 前后端交互

### 4.1 技术栈

前端： vue.js + axios    vue 模板渲染 axios网络请求

后台：flask（python） servlet（java）

数据存储：mysql



### 4.2 节点结构

一共是5个节点，假设每个服务器节点ip分别为

1.1.1.1 后端用户功能

2.2.2.2 前端用户功能

3.3.3.3 前端管理功能

4.4.4.4 后端管理功能

5.5.5.5 数据存储 mysql和图片所在服务器 身份认证服务器



### 4.3 可能遇到的问题及解决方案

1）后端应当返回怎样格式的数据，怎么返回？

2）前端如何去获取后端返回的数据，怎么解析？

3）如何解决浏览器禁止跨域访问的问题？

4）如何保存用户会话状态，进行身份认证？（单点登录）

5）图片传输问题，如何上传下载图片？



### 4.4 前后端分离参考资料

flask编写restful：https://blog.csdn.net/chenmozhe22/article/details/82347813

vue教程：https://www.runoob.com/vue2/vue-tutorial.html



### 4.5步骤

后台提供数据接口， 接口实现。

前台请求获取数据，并解析填充。