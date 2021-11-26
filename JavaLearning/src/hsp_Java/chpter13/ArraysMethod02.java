package hsp_Java.chpter13;

import java.util.Arrays;
import java.util.List;

public class ArraysMethod02 {
    public static void main(String[] args) {
        Integer[] arr = {1, 2, 90, 123, 567};

        // binarySearch
        int index = Arrays.binarySearch(arr, 567);
        System.out.println("index=" + index);

        // copyOf
        Integer[] newArr = Arrays.copyOf(arr, arr.length);
        System.out.println("===拷贝执行完毕后===");

        System.out.println(Arrays.toString(newArr));

        Integer[] num = new Integer[]{9, 3, 2};

        // fill
        Arrays.fill(num, 99);
        System.out.println("==num 数组填充后==");
        System.out.println(Arrays.toString(num));

        // equals
        Integer[] arr2 = {1, 2, 90, 123};
        boolean equals = Arrays.equals(arr, arr2);
        System.out.println("equals=" + equals);

        // asList
        List asList = Arrays.asList(2, 3, 4, 5, 6, 1);
        System.out.println("asList=" + asList);
        System.out.println("asList的运行类型" + asList.getClass());
    }
}
