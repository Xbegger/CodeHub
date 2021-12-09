package hsp_Java.chapter14;

import java.util.*;

@SuppressWarnings({"all"})
public class MapFor {

    public static void main(String[] args) {
        Map map = new HashMap();
        map.put("A", "B");
        map.put("C", "D");
        map.put("E", "D");
        map.put("F", null);
        map.put(null, "G");
        map.put("H", "I");

        //第一种，先取出所有的 Key，通过Key 去除对应的 Value
        Set keyset = map.keySet();
        System.out.println("---------第一种方式--------------");
        //1， 增强 for
        for(Object key : keyset){
            System.out.println(key + "----" + map.get(key));
        }

        //2, 迭代器
        System.out.println("---------第二种方式--------------");
        Iterator iterator = keyset.iterator();

        while( iterator.hasNext() ){
            Object key = iterator.next();
            System.out.println(key + "----" + map.get(key));
        }

        //第二种， 把所有 values 取出
        Collection values = map.values();
        //1, 增强 for
        System.out.println("----取出所有的 value 增强for ----");
        for(Object value : values){
            System.out.println(value);
        }

        //2, 迭代器
        System.out.println("----取出所有的value 迭代器----");
        Iterator iterator1 = values.iterator();
        while(iterator1.hasNext()){
            Object value = iterator1.next();
            System.out.println(value);
        }

        //第三种，通过 EntrySet 来获取 k-v
        Set entrySet = map.entrySet();
        //1，增强for
        System.out.println("----------使用EntrySet 的 for 增强");
        for(Object entry : entrySet){
            Map.Entry m = (Map.Entry) entry;
            System.out.println(m.getKey() + "----" + m.getValue());
        }

        //2，迭代器
        System.out.println("----使用EntrySet 的迭代器(第 4 种)----");
        Iterator iterator2 = entrySet.iterator();
        while(iterator2.hasNext()){
            Object entry = iterator2.next();
            Map.Entry m = (Map.Entry) entry;
            System.out.println(m.getKey() + "----" + m.getValue());
        }
    }
}
