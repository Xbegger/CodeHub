package hsp_Java.chapter13;

public class WrapperMethod {
    public static void main(String[] args) {
        // Integer
        System.out.println(Integer.MIN_VALUE);
        System.out.println(Integer.MAX_VALUE);

        // Character
        System.out.println(Character.isDigit('a'));
        System.out.println(Character.isLetter('a'));
        System.out.println(Character.isUpperCase('a'));
        System.out.println(Character.isLowerCase('a'));

        System.out.println(Character.isWhitespace('a'));
        System.out.println(Character.toUpperCase('a'));
        System.out.println(Character.toLowerCase('A'));

    }
}
