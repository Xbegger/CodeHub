package hsp_Java.chapter3;

public class String01 {

    public static void main(String[] args) {
        String str1 = "ABCD";
        String str2 = new String("ABCD");
        String str3 = new String("EFGH");
        System.out.println(str2 + str3);

        System.out.println("str1:" + str1);
        System.out.println("str2:" + str2);

        Test t1, t2;

        t2 = new Test("12345");
        t1 = t2;
        System.out.println(t1);

    }
}


class Test{
    public String s;

    public Test(String str){
        this.s = str;
    }

    @Override
    public String toString(){
        return "test1:" + this.s;
    }
}