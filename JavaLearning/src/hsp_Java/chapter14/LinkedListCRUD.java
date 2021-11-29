package hsp_Java.chapter14;


import java.util.Iterator;
import java.util.LinkedList;

@SuppressWarnings({"all"})
public class LinkedListCRUD {

    public static void main(String[] args) {

        LinkedList linkedList = new LinkedList();

        //add
        linkedList.add(1);
        linkedList.add(2);
        linkedList.add(3);
        System.out.println("linkedList=" + linkedList);

        //演示一个删除结点的
        linkedList.remove();//这里默认删除的是第一个结点

        System.out.println("linkedList=" + linkedList);

        //修改某个结点对象
        linkedList.set(1, 999);
        System.out.println("linkedList=" + linkedList);

        //得到某个结点对象
        Object o = linkedList.get(1);
        System.out.println(o);

        //因为 LinkedList 是 实现了 List 接口，遍历方式
        System.out.println("============LinkedList 遍历迭代器=============");
        Iterator iterator = linkedList.iterator();
        while(iterator.hasNext()){
            Object next = iterator.next();
            System.out.println("next=" + next);
        }

        System.out.println("===============LinkedList 遍历增强 for============");
        for(int i=0; i<linkedList.size(); i++){
            System.out.println(linkedList.get(i));
        }
    }
}
