package hsp_Java.chpter13;

import java.util.Locale;

public class StringMethod02 {
    public static void main(String[] args) {
        // 1. toUpperCase
        String s = "heLLo";
        System.out.println(s.toUpperCase());

        // 2, toLowerCase
        System.out.println(s.toLowerCase());

        // 3. concat
        String s1 = "宝玉";
        s1 = s1.concat("林黛玉").concat("薛宝钗").concat("together");
        System.out.println(s1);

        // 4. replace
        s1 = "宝玉 and 林黛玉 林黛玉 林黛玉";
        String s11 = s1.replace("宝玉", "jack");
        System.out.println(s1);
        System.out.println(s11);

        // 5. split 分割字符串，对于某些分割字符，需要转义 比如\\等
        String poem = "锄禾日当午,汗滴禾下土,谁知盘中餐,粒粒皆辛苦";
        String[] split = poem.split(",");
        for(int i=0; i<split.length; i++){
            System.out.println(split[i]);
        }
        poem = "E:\\aaa\\bbb";
        split = poem.split("\\\\");
        for(int i=0; i<split.length; i++){
            System.out.println(split[i]);
        }

        // 6.toCharArray
        s = "happy";
        char[] chs = s.toCharArray();
        for(int i=0; i<chs.length; i++){
            System.out.println(chs[i]);
        }

        // 7.compareTo
        String a = "jcck";
        String b = "jack";
        System.out.println(a.compareTo(b));

        // 8.format 格式化字符串
        String name = "john";
        int age = 10;
        double score = 56.857;
        char gender = '男';
        String formatStr = "我的名字是%s 年龄是%d, 成绩是%.2f 性别是%c.希望大家喜欢我！";
        String info2 = String.format(formatStr, name, age, score, gender);
        System.out.println(info2);
    }
}
