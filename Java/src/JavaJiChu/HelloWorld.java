package JavaJiChu;
public class HelloWorld{

	//主函数方法入口
	public static void main(String[] args) {

		//创建一个对象，对象名为hello
		HelloWorld hello = new HelloWorld();

		int maxscore = hello.getMaxAge();
		System.out.println("最大年龄为：" + maxscore);
	}

	//获取学生最大年龄函数，无参方法，返回值之为年龄最大值
	public int getMaxAge(){

		//定义一个整形数组，存贮学生年龄
		int ages[] = {18, 23, 21, 19, 25, 29,17};
		//假定学生初始最大值为数组里面第一个值
		int max = ages[0];
		//遍历数组中的元素
		for(int age:ages){
			if (age > max) {
				max = age;
			}
		}
		return max;
	}
}