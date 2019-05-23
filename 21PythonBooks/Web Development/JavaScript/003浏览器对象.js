// JavaScript 可以获取浏览器提供的很多对象, 并进行操作

// window对象不仅充当全局作用域, 而且表示浏览器窗口
console.log('window inner size:  ' + window.innerWidth + 'x' + window.innerHeight);

// navigator对象表示浏览器的信息,
console.log('appName = ' + navigator.appName);
console.log('appVersion = ' + navigator.appVersion);
console.log('language = ' + navigator.language);
console.log('platform = ' + navigator.platform);
console.log('userAgent = ' + navigator.userAgent);

// location对象表示当前页的URL信息
console.log(location);
console.log('url = ' + location.href);
console.log('pathname = ' + location.pathname);
console.log('search = ' + location.search);

// document对象表示当前页面, 由于HTML在浏览器中以DOM形式表示树形结构, document对象就是整个DOM树的根节点
document.title = 'JavaScript';
console.log(document.cookie);
// 要查找DOM树的某个节点, 需要从document对象开始查找
console.log(document.getElementsByName);
console.log(document.getElementsByClassName);
console.log(document.getElementById);

// 选中具体DOM 区分element element.children element.firstElementChild
// getElementById getElementByTagName  element array

var js = document.getElementById('test-p');
var arr = document.getElementById('test-div').children[1].children;
var haskell = document.getElementById('test-div').lastElementChild.lastElementChild;

// 更新DOM
// 修改innerHTML属性, 非常强大,
// 不但可以修改一个DOM节点的文本内容, 还可以直接通过HTML片段修改DOM节点内部的子数
var p = document.getElementById('p-id');
p.innerHTML = 'ABC';
p.innerHTML = 'ABC <span style="color: red">RED</span>';

// innerText属性, 只是文本
var pp = document.getElementById('pp-id');
pp.innerText = '<script>alert("Hi")</script>';

// DOM节点的style属性对应所有的CSS, 可以直接获取和设置
pp.style.color = 'green';
pp.style.fontWeight = 'bold';

// 插入DOM 获得了某个DOM, 想在这个DOM节点内插入新的DOM
// DOM节点是空的, 如<div></div>, 直接innerHTML = '<span>child</span>'
// DOM节点不是空的, element.appendChild
var
    js = document.getElementById('js');
    list = document.getElementById('list');
// js节点首先会从原先的位置删除, 再插入到新的位置
list.appendChild(js);
// 更多的是创建一个节点, 再附加到末尾
var haskell = document.createElement('p');
haskell.id = 'haskell';
haskell.innerText = 'Haskell';
list.appendChild(haskell);

// 把字节点插入到指定的位置, parentElement.insertBefore(newElement, referenceElement)
var newElement = document.createElement('p');
newElement.id = 'new';
newElement.innerText = 'newElement';
list.insertBefore(newElement, js);

// 删除一个节点 先获取该节点本身及它的父节点
var self = document.getElementById('to-be-removed');
var parent = self.parentElement;
var removed = parent.removeChild(self);

// 遍历节点 children
for (let i of list.children) {
    console.log(i);
}