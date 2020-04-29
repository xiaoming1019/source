package Demo;
import java.util.Scanner;

public class DemoTest02 {
    public static void main(String[] args){
        Scanner scaner = new Scanner(System.in);  //创建一个scanner对象
        System.out.print("Input your name: ");  //打印提示
        String name = scaner.nextLine();
        System.out.print("Input your age: ");
        int age = scaner.nextInt();
        System.out.printf("Hi, %s, you are %d\n", name,age);
    }
}
