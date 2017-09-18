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