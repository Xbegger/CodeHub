package hsp_Java.chapter14;

import java.util.ArrayList;
import java.util.HashMap;

public class Collection_ {

    @SuppressWarnings({"all"})
    public static void main(String[] args) {
        // 集合主要是两组(单列集合， 双列集合)
        // Collection 接口有两个重要的子接口 List、 Set，他们的实现子类都是单列集合
        ArrayList arrayList = new ArrayList();
        arrayList.add("jack");
        arrayList.add("tom");

        // Map 接口的实现子类，是双列集合，存放的K - V
        HashMap hashMap = new HashMap();
        hashMap.put("NO1", "北京");
        hashMap.put("NO2", "上海");
    }
}
