## 一、发送AJAX请求
### 1. 简介
vue本身不支持发送AJAX请求, 需要时间vue-resource、axios等插件  
axios是一个基于Promise的HTTP请求客户端, 用来发送请求, 也是vue2.0官方推荐, 同时不再对vue-resouce进行更新维护

参考: [GitHub axios, 查看API](https://github.com/axios/axios)

### 2. 使用
#### 2.1 安装axios并引入
```
https://github.com/axios/axios.git
```
#### 2.2 基本用法
axios([options]);  

axios.get(url, [options]);   
传参方式
- url?key=value  
- 通过选项 {params: {key: "value"}} 

axios.post(url, data, [options]);  
传参方式  
- data
- 如果使用模块化开发, 可以使用qs模块进行转换