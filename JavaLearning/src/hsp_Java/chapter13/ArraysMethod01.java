package hsp_Java.chapter13;

import java.util.Arrays;
import java.util.Comparator;

public class ArraysMethod01 {
    public static void main(String[] args) {
        Integer[] integers = {1, 20, 90};

        for(int i=0; i<integers.length; i++){
            System.out.println(integers[i]);
        }
        // Arrays.toString方法，显示数组
        System.out.println(Arrays.toString(integers));

        // sort方法
        Integer arr[] = {1, -1, 7, 0, 89};

        // 匿名内部类 实现接口重写
        Arrays.sort(arr, new Comparator() {
            @Override
            public int compare(Object o1, Object o2) {
                Integer i1 = (Integer) o1;
                Integer i2 = (Integer) o2;
                return i2 - i1;
            }
        });
        System.out.println("========排序后==========");
        System.out.println(Arrays.toString(arr));
    }
}
