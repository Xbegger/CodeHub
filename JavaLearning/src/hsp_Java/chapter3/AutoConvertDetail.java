package hsp_Java.chapter3;

public class AutoConvertDetail {
    public static void main(String[] args) {
        // 多种数据类型混合运算
        int n1 = 10;
//        float f1 = n1 +1.1; // 错误的赋值类型
        double d1 = n1 + 1.1; // n1 + 1.1  ==>  double
        float f1 = n1 + 1.1F;
        System.out.println(d1);
        System.out.println(f1);


//        int n2 = 1.1; // 错误的赋值


        // 细节二 : (byte, short) 和 char 之间不能相互转换
        byte b1 = 10;
////        // 当把具体数 赋值给 byte 时，先判断该数是否在 byte范围内， 如果是就可以
////        int n2 = 1;
////        byte b2 = n2;
//        short s1 = 10;
//        char c1 = b1;
//        char c2 = s1;
//        char c3 = 'a';
//        byte b2 = c3;
//        short s2 = c3;

        //byte，short，char 他们三者可以计算，在计算时首先转换为int类型
        byte b2 = 1;
        byte b3 = 2;
        short s1 = 1;
//        short s2 = b2 + s1;// 错误的赋值
        int s2 = b2 + s1;
        System.out.println(s2);
        System.out.println(b2 + s1);
//        byte b4 = b2 + b3;// 错误的赋值

        // boolean 不参与类型的自动转换
        boolean pas = true;
//        int num100 = pass; // 错误的赋值

        byte b4 = 1;
        short s3 = 100;
        int num200 = 1;
        double num300 = 1.1;

        // float num500 = b4 + s3 + num200 + num300; //错误的赋值
        double num500 = b4 + s3 + num200 + num300;
        System.out.println(num500);
    }
}
