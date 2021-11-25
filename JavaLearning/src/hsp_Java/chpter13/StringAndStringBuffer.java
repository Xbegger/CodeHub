package hsp_Java.chpter13;



public class StringAndStringBuffer {
    public static void main(String[] args) {
        String str = "hello tom";

        // String -> StringBuffer
        // 方式 1 使用构造器
        // 返回的是 StringBuffer对象，对 str 本身没有影响
        String t = null;
        StringBuffer stringBuffer = new StringBuffer(str);
        System.out.println(stringBuffer);
        // 方式 2 使用的是 append 方法
        StringBuffer stringBuffer1 = new StringBuffer();
        stringBuffer1 = stringBuffer1.append(str);

        // StringBuffer -> String
        // 方式 1 使用 StringBuffer 提供的 toString 方法
        StringBuffer stringBuffer2 = new StringBuffer("韩顺平教育");
        String s = stringBuffer2.toString();

        // 方式 2 使用构造器来确定
        String s1 = new String(stringBuffer2);
    }
}
