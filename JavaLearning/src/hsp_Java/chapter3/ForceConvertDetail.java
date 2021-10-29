package hsp_Java.chapter3;

public class ForceConvertDetail {
    public static void main(String[] args) {

//        int x = (int) 10 * 3.5 + 6 * 1.5;// 错误的赋值
        int x = (int)(10 * 3.5 + 6 * 1.5);// 44.0 -> 44
        System.out.println(x);


        char c1 = 100;
        int m =100;
//        char c2 = m;// 错误的赋值
        char c3 = (char)m;
        System.out.println(c3);
    }
}
