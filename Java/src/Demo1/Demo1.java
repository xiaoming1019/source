package Demo1;
import java.util.Scanner;
public class Demo1 {
    public static void main(String[] args){
        getChar tw = new getChar();
        System.out.println("请输入新星期的第一个大字母：");
        char ch = tw.getChar();
        switch(ch) {
            case 'M':
                System.out.println("Monday");
                break;
            case 'W':
                System.out.println("Wednesday");
                break;
            case 'F':
                System.out.println("Friday");
                break;
            case 'T': {
                System.out.println("请输入信息的第二个字母");
                char ch2 = tw.getChar();
                if (ch2 == 'U') {
                    System.out.println("Tuesday");
                }
                else if (ch2 == 'H') {
                    System.out.println("Tuesday");
                }
                else {
                    System.out.println("无此写法");
                }
                };
                break;
            case 'S':{
                System.out.println("请输入新奇的第二个字母：");
                char ch2 = tw.getChar();
                if (ch2 == 'U'){
                    System.out.println("Sunday");
                }
                else if (ch2 == 'A'){
                    System.out.print("Saturday");
                }
                else {
                    System.out.println("无此写法");
                }
            };
            break;
            default:System.out.print("无此写法");
        }
    }
}

class getChar{
    public char getChar(){
        Scanner s = new Scanner(System.in);
        String str = s.nextLine();
        char ch = str.charAt(0);
        if (ch < 'A' || ch > 'Z'){
            System.out.println("输入错误，请重新输入");
            ch = getChar();
        }
        return ch;
    }
}
