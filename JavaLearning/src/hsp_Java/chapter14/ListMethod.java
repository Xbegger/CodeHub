package hsp_Java.chapter14;

import java.util.ArrayList;
import java.util.List;

public class ListMethod {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        List list = new ArrayList();
        list.add("张三丰");
        list.add("贾宝玉");

        list.add(1, "韩顺平");

        System.out.println("list=" + list);

        // addAll
        List list2 = new ArrayList();
        list2.add("jack");
        list2.add("tom");
        list.addAll(1, list2);
        System.out.println("list=" + list);

        //indexOf
        System.out.println(list.indexOf("tom"));

        list.add("韩顺平");
        System.out.println("list=" + list);
        System.out.println(list.lastIndexOf("韩顺平"));

        list.remove(0);
        System.out.println("list=" + list);

        list.set(1, "玛丽");
        System.out.println("list=" + list);

        List returnlist = list.subList(0, 2);
        System.out.println("returnList=" + returnlist);
    }
}
