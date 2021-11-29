package hsp_Java.chapter14;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

@SuppressWarnings({"all"})
public class SetMethod {

    public static void main(String[] args) {

        Set set = new HashSet();
        set.add("john");
        set.add("lucy");
        set.add("john");
        set.add("jack");
        set.add("hsp");
        set.add("mary");
        set.add(null);
        set.add(null);

        for(int i=0; i<10; i++){
            System.out.println("set=" + set);
        }

        //方式1: 使用迭代器
        System.out.println("============使用迭代器===========");
        Iterator iterator = set.iterator();
        while(iterator.hasNext()){
            Object obj = iterator.next();
            System.out.println("obj=" + obj);
        }
        set.remove(null);

        //方式2: 增强for
        System.out.println("==============增强 for===============");

        for(Object o:set){
            System.out.println("o=" + o);
        }
    }
}
