package hsp_Java.chapter4;

public class ArithmeticOperator {
    public static void main(String[] args) {
        System.out.println(10 / 4);
        System.out.println(10.0 / 4);
        double d = 10 / 4;
        System.out.println(d);


        // % 取模 取余
        // a % b = a - a/b * b
        System.out.println(10 % 3); // 1
        System.out.println(-10 % 3); // -1
        System.out.println(10 % -3); // 1
        System.out.println(-10 % -3);// -1
    }
}
