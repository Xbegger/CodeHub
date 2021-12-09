package hsp_Java.chapter14;

import java.util.HashMap;
import java.util.Map;

@SuppressWarnings({"all"})
public class MapMethod {
    public static void main(String[] args) {
        Map map = new HashMap();
        map.put("A", new Book1("", 100));
//        map.put("A", "B");
        map.put("C", "D");
        map.put("E", "D");
        map.put("F", null);
        map.put(null, "G");
        map.put("H", "I");

        System.out.println("map=" + map);

        // remove: 根据键删除映射关系
        map.remove(null);
        System.out.println("map" + map);

        //get: 根据键获取值
        Object val = map.get("H");
        System.out.println("val =" + val);

        // size: 获取元素个数
        System.out.println("k-v = " + map.size());

        // isEmpty: 判断个数是否为0
        System.out.println(map.isEmpty());

        // clear: 清除 k-v
//        map.clear();
        System.out.println("map=" + map);

        //containsKey: 查找键是否存在
        System.out.println("结果=" + map.containsKey("E"));

    }
}

 class Book1{
    private String name;
    private int num;

    public Book1(String name, int num){
        this.name = name;
        this.num = num;
    }
}
