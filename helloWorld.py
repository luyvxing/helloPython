print(100+200);
print('1024 * 768 = ',1024*768);
print('I \'m \"ok\"!');
#转义字符 
print('\\\n\\');
print(r'\\\n');
#多行输出时用'''  '''格式
#命令行模式时要使用''' ...line1
#				      ...line2
#					  ...line3'''的格式
print('''line1
line2
line3''');
#布尔值运算
print('True and False = ',True and False);
print('True and True = ',True and True);
print('True or False = ',True or False);
print('True or True =', True or True);
print('False or False =',False or False);
#条件判断中布尔值的应用
#age = input("please enter ur age : ")
#if int(age) > 18 :
#	print('adult')
#else:
#	print('teenager')
#精确除法
print('10 / 3 =',10 / 3);
#只取整数的地板除
print('10 // 3 = ',10//3);
#取余数
print('10 % 3 =',10%3)

#格式化数据
print('Hello,%s'%'world');
print('Hi,%s，u have $%d'%('micheal',100000));

#小明的成绩从去年的72分提升到了今年的85分，
#请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，
#只保留小数点后1位：
s1 = 72;
s2 = 85;
r = (s2 - s1) / s1 * 100;

print('小明的成绩提升了','%.1f%%' % r);



##python内置list
classmates = ['bob','john','mary'];
print(classmates);
print('len(classmates) = ',len(classmates));
#classmates[-1]代表直接取最后一个元素,同理也可用-2取倒数第二个元素
print('classmates[-1] =',classmates[-1]);

#往list的最后一位追加元素
classmates.append('ada');
print(classmates);
#在指定位置插入元素
classmates.insert(1,'amy');
print(classmates);
#删除末尾元素
classmates.pop();
print(classmates);
#删除指定位置元素,1是被删除元素的索引值
classmates.pop(1); 


#tuple与list相似，可以通过索引获取其中元素，但
#tuple一经定义，无法修改
classmates = ('tom','jack','rose'); 
print('here is a tuple :',classmates);
#只有一个元素的tuple需要在后面加个逗号与运算式型进行区分，如下
classmates = (1,);
print('only one element\'s tuple is like:',classmates )

#list练习题
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
];
print(L[0][0],L[1][1],L[2][-1]);

#条件判断
age = 3
if age >18:
	print('adult');
elif age == 18:
	print('just adult');
else :
	print('teenager');
	

##小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
height = 1.75;
weight = 80.5;

bmi = weight / height / height;

if bmi < 18.5 :
 	print('过轻');
elif bmi < 25 :
	print('正常');
elif bmi < 28 :
	print('过重');
elif bmi <32 :
	print ('肥胖');
else :
	print('严重肥胖');

#for-in循环
L = ['Bart', 'Lisa', 'Adam'];
for name in L:
	print('Hello,'+name+"!"+'\n')

#字典dict
d = {'mike':95,'bob':66,'kim':34};
print(d['mike']); 
#通过In来判断key是否存在
print('boby' in d)
#没找到key时指定返回的value
print(d.get('bob',-2));
#pop可以删除相应的key
d.pop('bob');
print(d);

#set，key的集合，不存储value
s = set ([1,2,23,4,4,5]);
print(s);
s.add(1);
print(s);
s.remove(23);
print(s);
#还可以对set进行交集和并集的操作（这个好棒哦~！）
anotherS = set([9,2,3,4,6,2]);
print(s & anotherS)
print (s | anotherS)

#abs()求绝对值，max()求最大值
print(abs(-22))
print(max(1,2,34,5))
#可以把函数名赋给一个变量，相当于给函数取了个别名
a = abs ;
print(a(-33))
print(hex(255))