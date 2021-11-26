package hsp_Java.chapter10;

public class CodeBlockDetail01 {
    public static void main(String[] args) {
//        Father father = new Son();
        System.out.println(Son.num2);
        System.out.println("Main 代码");
    }
}

class Father{
    public static int num1 = 0;
    static {
        System.out.println("Father 静态代码块");
    }

    public Father(){
        System.out.println("Father 构造函数");
    }
    {
        System.out.println("Father 非静态代码块");
    }

}
class Son extends Father{
    public static int num2 = 0;
    {
        System.out.println("Son 非静态代码块");
    }
    static{
        System.out.println("Son 静态代码块");
    }
    public Son(){
        System.out.println("Son 构造函数");
    }
    public void test(){
        System.out.println("Son test函数");
    }
}