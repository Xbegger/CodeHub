package hsp_Java.chpter13;

public class WrapperVSString {
    public static void main(String[] args){
        Integer i = 100;

        // 包装类(Integer) -> String
        // 方式1
        String str1 = i + "";
        // 方式2
        String str2 = i.toString();
        // 方式3
        String str3 = String.valueOf(i);

        //String -> 包装类(Integer)
        String str4 = "12345";
        // 方式1  使用自动装箱
        Integer i1 = Integer.parseInt(str4);
        // 方式2  构造器
        Integer i2 = new Integer(str4);
    }
}
