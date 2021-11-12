package hsp_Java.chapter3;

public class CharDetail {
    public static void main(String[] args) {
        char c1 = 97;
        System.out.println(c1);

        char c2 = 'a';
        System.out.println((int)c2);
        char c3 = '韩';
        System.out.println((int)c3);
        char c4 = 38889;
        System.out.println(c4);

        // char 类型可以参与运算
        System.out.println('a' + 10);

        char c5 = 'b' + 1;
        System.out.println((int)c5);//99
        System.out.println(c5);//c
    }
}
