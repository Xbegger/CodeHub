package hsp_Java.chapter3;

public class StringToBasic {
    public static void main(String[] args) {
        int n1 = 100;
        float f1 = 1.1f;
        double d1 = 4.5;
        boolean b1 = true;
        String s1 = "" + n1 + f1 + d1 + b1;
        System.out.println(s1);

        String s5 = "123";
        int num1 = Integer.parseInt(s5);
        double num2 = Double.parseDouble(s5);
        float num3 = Float.parseFloat(s5);
        long num4 = Long.parseLong(s5);
        byte num5 = Byte.parseByte(s5);
        boolean num6 = Boolean.parseBoolean("true");
        short num7 = Short.parseShort(s5);
        System.out.println(num1);
        System.out.println(num2);
        System.out.println(num3);
        System.out.println(num4);
        System.out.println(num5);
        System.out.println(num6);
        System.out.println(num7);
        System.out.println(s5.charAt(0));

    }
}
