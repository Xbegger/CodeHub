package hsp_Java.chapter14;

import java.util.ArrayList;

@SuppressWarnings({"all"})
public class ArrayListSource {

    public static void main(String[] args) {
        ArrayList list = new ArrayList();

        for(int i=1; i<=10; i++){
            list.add(i);
        }

        System.out.println(list);
        for(int i=11; i<=15; i++){
            list.add(i);
        }
        list.add(100);
        list.add(200);
        list.add(null);
        System.out.println(list);
    }
}
