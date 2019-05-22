### Vue.js

## 一、Vue.js 简介
### 1. Vue.js是什么
**Vue.js** 也称Vue, 读音/vju:/, 类似view, 错误读音v-u-
版本: v1.0 v2.0

+ 是一个构建用户界面的框架
+ 是一个轻量级MVVM(Model-View-ViewModel)框架, 和Angular, React类似, 其实就是所谓的数据双向绑定
+ 数据驱动+组件化的前端开发
+ 通过简单的API实现**响应式的数据绑定**和**组合的视图组件**
+ 更容易上手, 小巧

参考： [官网](https://cn.vuejs.org/)

### 2. Vue和Angular的区别

#### 2.1 Angular
+ 上手较难
+ 指令以ng-xxx开头
+ 所有属性和方法都存储在$scope中
+ 有Google维护

#### 2.2 Vue
+ 简单、易学、更轻量
+ 指令以v-xxx开头
+ HTML+JSON数据, 再创建一个Vue实例
+ 由个人维护: **尤雨溪**, 华人, 目前就职于阿里巴巴

共同点：都不兼容低版本IE


## 二、起步
### 1. 下载核心库 vue.js
```
git clone --branch v2.6.10 https://github.com/vuejs/vue.git
直接拷贝 dist/vue.js
```
vue2.0和v1.0相比, 最大的变化就是引入了Virtual DOM(虚拟DOM), 页面更新效率更高, 速度更快

### 2. Hello World

