## 一、Vue生命周期
Vue实例从创建到销毁的过程, 称为生命周期, 共有八个阶段  
统一作为new Vue(options)中options选项, 与el, data, methods, filters同级别
- beforeCreate()
- created()
- beforeMount()
- mounted()
- beforeUpdate()
- updated()
- beforeDestroy()
- destroyed()

## 二、计算属性

### 1. 基本用法
计算属性也是用来存储数据, 但具有以下几个特点:
- 数据可以进行逻辑处理操作
- 对计算属性中的数据进行监视

### 2. 计算属性 vs 方法
将计算属性的get函数定义为一个方法也可以类似的功能  
区别:
- 计算属性是基于它的依赖进行更新的, 只有在相关依赖发生改变时才能更新变化
- 计算属性是有缓存的, 只要相关依赖没有改变, 多次访问计算属性得到的值是之前缓存的计算效果, 不会多次执行

### 3. get和set
计算属性由两部分组成: get和set, 默认只有get, set需要添加


## 三、Vue实例的属性和方法
### 1. 属性
- vm.属性名
- vm.$el
- vm.$data
- vm.$options
- vm.$ref
### 2. 方法
- vm.$mount()
- vm.$destroy()
- vm.nextTrick()

- vm.$set()
- vm.$delete()
- vm.$watch()