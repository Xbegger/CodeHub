package hsp_Java.chapter3;

public class FloatDetail {
    public static void main(String[] args) {
        float num1 = 1.1f;
        double num2 = 1.1;

        double num11 = 2.7;
        double num12 = 8.1 / 3;

        System.out.println(num11);
        System.out.println(num12);

        if(num11 == num12){
            System.out.println("相等");
        }

        if(Math.abs(num11 - num12) < 0.000001){
            System.out.println("差值非常小，到我规定精度，认为相等");
        }
        System.out.println(Math.abs(num11 -num12));
    }
}
