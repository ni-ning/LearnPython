// 函数定义
function abc(x) {
    // return 当返回语句段时 return {}
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}

var abs = function (x) {
    // JavaScript 免费赠送的关键字 arguments
    // 只在函数内部起作用, 并且永远指向当前函数的调用者传入的所有参数
    // arguments 类似Array, 但它不是一个Array
    for (var i=0; i<arguments.length; i++) {
        alert(arguments[i])
    }
    console.log(arguments);
    if (typeof x !== 'number') {
        throw 'Not a number'
    }
    if (x >= 0) {
      return x;
    } else {
      return -x;
    }
};

function foo(a, b, ...rest) {
    // ES6 多余的参数以数据形式交给变量rest
    console.log(arguments);
    console.log(rest);
}

// 函数调用
foo(1, 2, 3, 4, 5);
alert(abc(-10));
alert(abs('100'));

// JavaScript默认有一个全局对象 window, 全局作用域的变量实际上被绑定到window的一个属性
var course = 'Learn JavaScript';
alert(course);
alert(window.course);

function foo() {
    alert('foo')
}
foo();
window.foo();

// alert()函数其实也是window的一个变量
window.alert('调用window.alert');
var old_alert = window.alert;
window.alert = function () {};

alert('无法显示alert了');

// 全局变量会绑定到window上，不同的JavaScript文件如果使用了相同的全局变量，或者定义了相同名字的顶层函数，都会造成命名冲突, 并且很难被发现
var MYAPP = {};
MYAPP.name = 'myapp';
MYAPP.version = 1.0;
MYAPP.foo = function () {
    return 'foo';
};
// 许多著名的JavaScript库就是这么干的，jQuery, underscore等


// 局部作用域
// 为了解决块级作用域 ES6 let 代替 var
function foo() {
    var sum = 0;
    for (let i=0; i<100; i++) {
        sum += i;
    }
}

// 常量 ES6
const PI = 3.14;

// 解构赋值
var [x, y, z] = ['Hello', 'JavaScript', 'ES6'];
var [, , es] = ['Hello', 'JavaScript', 'ES6'];
var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school'
};
var {name, age, passport} = person;

// map 函数作用于数组的每个元素, 返回值组成新的数组, 函数只需一个参数即可
function pow(x) {
    return x * x;
}

var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
var results = arr.map(pow);
console.log(results);

// reduce 函数作用于数组上, 返回值和序列的下一个元素做累计计算, 函数需要两个参数
var arr1 = [1, 3, 5, 7, 9];
var ret1 = arr1.reduce(function (p1, p2) { return p1 + p2; });
console.log(ret1);

// filter 函数作用于数组的每个元素, 返回值true元素保留, false过滤, 剩下元素组成新的数组
var arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
var ret2 = arr2.filter(function (x) {
    return x % 2 !== 0;
});
console.log(ret2);
// filter接收的回调函数，参数可以多个 element, index, self
var arr3 = ['apple', 'strawberry', 'banana', 'pear', 'apple', 'orange', 'orange', 'strawberry'];
var ret3 = arr3.filter(function (element, index, self) {
    return self.indexOf(element) === index;
});
console.log(ret3);

// sort 默认把所有元素先转换为String再排序
var arr4 = [10, 20, 1, 2];
arr4.sort();
console.log(arr4);
// 通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
// 这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序
arr4.sort(function (x, y) {
    if (x < y) {
        return 1;
    }
    if (x > y) {
        return -1;
    }
    return 0;
});
console.log(arr4);

// every 判断数组的所有元素是否满足测试条件
var arr5 = ['Apple', 'pear', 'orange'];
console.log(arr5.every(function (t) {
    return t.length > 0;
}));

// forEach和map类似, 把每个函数依次作用于传入的函数, 但不会返回新的数组，无返回值, 常用于遍历
var arr6 = ['Apple', 'pear', 'orange'];
arr6.forEach(function (element, index, self) {
    console.log(element);
});

// 闭包 函数作为返回值
function sum(arr) {
    return arr.reduce(function (p1, p2) {
        return p1 + p2;
    })
}
console.log(sum([1, 2, 3, 4, 5]));

function lazy_sum(arr) {
    var sum = function () {
        return arr.reduce(function (x, y) {
            return x + y;
        });
    };
    return sum;
}
var f = lazy_sum([1, 2, 3, 4, 5]);
console.log(f);

// 箭头函数 相当于匿名函数, 简化了函数的定义。一种只包含一个表达式 {...} 和 return 都省略
var fn = x => x * x;
console.log(fn(10));

(x, y) => x * x + y * y;
() => 3.14;
// 放回一个对象
x => ({foo: 123})