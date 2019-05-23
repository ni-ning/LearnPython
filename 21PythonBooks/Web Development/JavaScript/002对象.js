// typeof 操作符获取对象的类型, 它总是返回一个字符串;
console.log(typeof 123);    // 'number'
console.log(typeof NaN);    // 'number'
console.log(typeof 'str');  // 'string'
console.log(typeof true);   // 'boolean'
console.log(typeof undefined);      // 'undefined'
console.log(typeof Math.abs);       // 'function'
console.log(typeof null);   // 'object'
console.log(typeof []);     // 'object'
console.log(typeof {});     // 'object'

// 包装对象, number boolean string 有对应包括对象，闲的蛋疼也不要使用包装对象
var n = new Number(123);
var b = new Boolean(true);
var s = new String('str');

typeof n;   // 'object'
typeof b;   // 'object'
typeof s;   // 'object'

// 总结一下，有这么几条规则需要遵守
// 不要使用new Number()、new Boolean()、new String()创建包装对象
// 用parseInt()或parseFloat()来转换任意类型到number
// 用String()来转换任意类型到string，或者直接调用某个对象的toString()方法
// 通常不必把任意类型转换为boolean再判断，因为可以直接写if (myVar) {...}
// typeof操作符可以判断出number、boolean、string、function和undefined
// 判断Array要使用Array.isArray(arr)
// 判断null请使用myVar === null
// 判断某个全局变量是否存在用typeof window.myVar === 'undefined'
// 函数内部判断某个变量是否存在用typeof myVar === 'undefined'
console.log(typeof parseInt('123'));
console.log(typeof String(123));
console.log(Array.isArray([1, 2, 3]));
console.log(Array.isArray({name: 'alex'}));
console.log(true===null);
console.log(null===null);
console.log(typeof window.myVar==='undefined');

// null 和 undefined 没toString()方法
console.log(123..toString());
console.log((123).toString());

// JavaScript中, Date对象用来表示日期和时间
var now = new Date();
now; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
now.getFullYear(); // 2015, 年份
now.getMonth(); // 5, 月份，注意月份范围是0~11，5表示六月
now.getDate(); // 24, 表示24号
now.getDay(); // 3, 表示星期三
now.getHours(); // 19, 24小时制
now.getMinutes(); // 49, 分钟
now.getSeconds(); // 22, 秒
now.getMilliseconds(); // 875, 毫秒数
now.getTime(); // 1435146562875, 以number形式表示的时间戳

// 创建日期
var d = new Date(2019, 5, 19, 20, 15, 30, 123);
console.log(d);

var d1 = Date.parse('2015-06-24T19:49:22.875+08:00');
console.log(d1);
console.log(new Date(d1));

// JavaScript 正则
var re1 = /ABC\-001/;
var re2 = new RegExp('ABC\\-001');

// obj.test() 检测给定的字符串是否符合条件
console.log(re1.test('ABC\-001'));
console.log(re2.test('ABC\-001'));

//切分字符串
console.log('a b   c'.split(' '));
console.log('a b   c'.split(/\s+/));
console.log('a;b, c  d'.split(/[\s,;]+/));

//分组 re.exec 提取分组
var re = /^(\d{3})-(\d{3,8})$/;
console.log(re.exec('010-12345'));
console.log(re.exec('010 12345'));

// 正则总结
// 单个匹配 \d \w \s
// 变长匹配 * + ? {n} {n, m}
// 精确匹配 [0-9a-zA-Z]
// 开头 ^ 结尾 $
// re.test re.exec /表达式/ 或 new RexExp(表达式)

// JSON是JavaScript Object Notation的缩写, 它是一种数据交换格式
// number：和JavaScript的number完全一致
// boolean：就是JavaScript的true或false
// string：就是JavaScript的string
// null：就是JavaScript的null
// array：就是JavaScript的Array表示方式——[]
// object：就是JavaScript的{ ... }表示方式

// JSON还定死了字符集必须是UTF-8, JSON的字符串规定必须用双引号"", Object的键也必须用双引号""

// JavaScript 内置JSON解析
// 如果我们收到一个JSON格式的字符串，只需要把它反序列化成一个JavaScript对象，就可以在JavaScript中直接使用这个对象了
var xiaoming = {
    name: '小明',
    age: 14,
    gender: true,
    height: 1.65,
    grade: null,
    'middle-school': '\"W3C\" Middle School',
    skills: ['JavaScript', 'Java', 'Python', 'Lisp'],
    // 精确控制序列化输出
    toJSON: function () {
        return {
            Name: this.name,
            Age: this.age
        }
    }
};
// 每个键值对预处理
function convert(key, value) {
    console.log(key, value);
    return value;
}
var s = JSON.stringify(xiaoming, convert);
console.log(s);
// JSON格式的字符串是一种通用格式，JSON对象与具体语言有关

console.log(JSON.parse('[1, 2, true]'));
console.log(JSON.parse('{"name":"小明","age":14}'));
console.log(JSON.parse('3.14'));
// 同样可以接收函数
var obj = JSON.parse('{"name":"小明","age":14}', function (key, value) {
    if (key === 'name') {
        return value + '同学';
    }
    return value;
});
console.log(JSON.stringify(obj)); // {name: '小明同学', age: 14}

// 构造函数来创建对象, new 才行
// this指向创建的对象, 并默认返回this
function Student(name) {
    this.name = name;
    this.hello = function () {
        alert('Hello, ' + this.name + '!');
    }
}

// 原型链 xiaoming ---> Student.prototype ---> Object.prototype ---> null
var xiaoming = new Student('小明');
console.log(xiaoming.name);
xiaoming.hello();


// 用 new Student()创建的对象还从原型上获得了一个constructor属性, 指向函数Student本身
console.log(xiaoming.constructor === Student.prototype.constructor);
console.log(Student.prototype.constructor === Student);
console.log(Object.getPrototypeOf(xiaoming) === Student.prototype);
console.log(xiaoming instanceof Student);

// 忘记写new怎么办
// 按照约定, 构造函数首字母应大写, 而普通函数字母应当小写
function Student1(props) {
    this.name = props.name || '匿名';
    this.grade = props.grade || 0;
}
// 共享函数 hello
Student1.prototype.hello = function () {
    alert('Hello, ' + this.name + '!')
};

//createStudent函数有几个巨大优点: 一是不需要new来调用, 二是参数非常灵活
function createStudent(props) {
    return new Student1(props || {})
}

var xiaohong = createStudent();
console.log(xiaohong.name);
console.log(xiaohong.grade);

// 原型继承


// class继承
class Student3 {
    constructor (name) {
        this.name = name;
    }
    hello () {
        alert('Hello, ' + this.name + '!');
    }
}
console.log(new Student3('小小').name);
