package Demo;

public class DemoTest01 {
    public static void main(String[] args){
        /*
        String str1 = "ABC";
        String str2 = "ZXC";
        String str3 = str1 + str2;
        System.out.println(str3);
       */
        var Demo = new DemoTest01();
        int Sum;
        Sum = Demo.getSum();
        System.out.println(Sum);
        System.out.println(Sum == 5050 ? "测试通过" : "测试失败");
    }

    public int getSum(){
        int num = 0;
        for (int i = 0; i <= 100; i++){
            num = i + num;
        }
        return num;
    }
}
