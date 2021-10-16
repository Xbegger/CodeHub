package basic;

public class TypeConversion {
    public static void main(String[] args) {
        int i = 128;
        byte b = (byte)i;

        System.out.println("byte b:" + b);

        System.out.println("(int)23.7 == 23:"+ ((int)23.7 == 23));
        System.out.println("(int)-45.89f == -45" + ((int)-45.89f == -45));


    }
}
