package basic;

public class TypeConversion {
    public static void main(String[] args) {

        // 自动类型转换
        int i = 128;
        byte b = (byte)i;

        System.out.println("byte b:" + b);

        System.out.println("(int)23.7 == 23:"+ ((int)23.7 == 23));
        System.out.println("(int)-45.89f == -45" + ((int)-45.89f == -45));

        char c1 = 'a';
        int i1 = c1;
        System.out.println("char自动类型转换为int后的值等于" + i1);

        char c2 = 'A';
        int i2 = c2 + 1;
        System.out.println("char 类型和int 计算后的值等于" + i2);


        // 强制类型转换
        int i3 = 123;
        byte b1 = (byte) i3;
        System.out.println("int 强制类型转换为byte 后的值等于" + b1);
    }
}
