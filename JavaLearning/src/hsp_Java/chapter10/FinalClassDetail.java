package hsp_Java.chapter10;

public class FinalClassDetail {
    public static void main(String[] args) {
        test t = test.t1;
    }
}

final class test{
    public final int num;
    public static final test t1 = new test();
    public test(){
//        num = 10;
    }
    {
        num = 20;
    }
}