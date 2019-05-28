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


//JavaScript不区分类和实例的概念, 而是通过原型(prototype)来实现面向对象
var robot = {
    name: 'Robot',
    height: 1.6,
    run: function () {
        console.log(this.name + ' is running...');
    }
};

// robot有点像小明，有名称, 身高, 能跑
var Student = robot;

var xiaoming = {
    name: '小明'
};

// xiaoming的原型指向了Student, 看上去xiaoming仿佛是从Student继承下来
xiaoming.__proto__ = Student;
console.log(xiaoming.name);
xiaoming.run();

var Bird = {
    fly: function () {
        console.log(this.name + ' is flying...')
    }
};

// 在JavaScript代码运行时期, 可以把xiaoming从Student变成Bird, 或者变成任何对象
xiaoming.__proto__ = Bird;
console.log(xiaoming.name);
xiaoming.fly();

// Object.create(Student) 传入一个原型对象, 并创建一个基于该原型的新对象
// 但是该新对象什么属性都没有

function createStudent(name) {
    var s = Object.create(Student);
    s.name = name;
    return s;
}
var xiaohong = createStudent('小红');
xiaohong.run();
console.log(xiaohong.__proto__ === Student);
// 这是创建原型继承的一种方法，还有其他



// 构造函数: 除了用{...}创建对象外, JavaScript还可以用构造函数的方法来创建对象
function Student(name) {
    this.name = name;
    this.hello = function () {
        alert('Hello, ' + this.name + '!');
    }
}

// 如果不写new, 就是一个普通函数, 返回值 undefined
// 如果写了new, 它就变成一个构造函数, this指向新创建的对象, 并默认返回this
var xiaoxiao = new Student('小小');
console.log(xiaoxiao.name);
xiaoxiao.hello();

// 用new Student()创建的对象还从原型上获得了一个constructor属性, 它指向函数Student本身
console.log(xiaoxiao.constructor === Student.prototype.constructor);  // true
console.log(Student.prototype.constructor === Student);  // true

console.log(Object.getPrototypeOf(xiaoxiao) === Student.prototype);  // true

console.log(xiaoxiao instanceof Student);  // true

// 总结
// Student.prototype 表示 xiaoxiao, xiaoming, xiaohong的原型对象
// Student.prototype 有个constructor属性, 指向Student函数本身
// xiaoxiao, xiaoming, xiaohong是没有prototype这个属性
console.log(xiaoxiao.__proto__ === Student.prototype);  // 非标准用法

// function Student 和 Student = {} 一个表示函数, 一个表示对象

xiaoming = new Student('小明');
xiaohong = new Student('小红');
console.log(xiaoming.hello === xiaohong.hello);  // false
// xiaoming, xiaohong 各自的hello是一个函数, 但它们是两个不同的函数, 虽然函数名称和代码都相同, 如何共享呢?
// 根据属性的查找规则, 只要把hello函数移动到xiaoming, xiaohong这些对象共同的原型上就可以, 也就是Student.prototype
function Student(name) {
    this.name = name;
}
Student.prototype.hello = function () {
    console.log('Hello, ' + this.name + '.')
};

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
// 定义空构造函数F, new F()中间桥接对象
function inherits(Child, Parent) {
    var F = function () {};
    F.prototype = Parent.prototype;
    Child.prototype = new F();
    Child.prototype.constructor = Child;
}

// props.name || 'else'
function Student(props) {
    this.name = props.name || 'Unnamed';
}

// 原型对象 实现共享函数
Student.prototype.hello = function () {
    alert('Hello, ' + this.name + '!');
};

// Student.call(this, props) 只是构造函数的复用
function PrimaryStudent(props) {
    Student.call(this, props);
    this.grade = props.grade || 1;
}

// 绑定原型继承链
inherits(PrimaryStudent, Student);

// 实现自己的共享函数
PrimaryStudent.prototype.getGrade = function () {
    return this.grade;
};

// JavaScript的原型继承实现方式就是：
// 定义新的构造函数，并在内部用call()调用希望“继承”的构造函数，并绑定this；
// 借助中间函数F实现原型链继承，最好通过封装的inherits函数完成；
// 继续在新的构造函数的原型上定义新方法。


// class继承
class Student {
    constructor(name){
        this.name = name;
    }
    hello(){
        alert('Hello, ' + this.name + '!');
    }
}
// class 包含构造函数constructor和定义在原型对象上的函数hello()

class PrimaryStudent extends Student {
    constructor(name, grade) {
        super(name);  // super调用父类的构造方法
        this.grade = grade;
    }
    myGrade(){
        alert('I am at grade ' + this.grade);
    }
}

xiaoxiaoming = new PrimaryStudent('小小明', 100);
xiaoxiaoming.myGrade();