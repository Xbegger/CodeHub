package hsp_Java.chapter14;

import java.util.concurrent.atomic.AtomicLong;

public class LinkedList01 {

    public static void main(String[] args) {
        Node jack = new Node("jack");
        Node tom = new Node("tom");
        Node hsp = new Node("老韩");

        //连接三个结点，形成双向链表
        //jack -> tom -> hsp
        jack.next = tom;
        tom.next = hsp;

        //hsp -> tom -> jack
        hsp.pre = tom;
        tom.pre = jack;

        Node first = jack;//first 引用 指向 jack，就是双向链表的头结点
        Node last = hsp;//last 引用 指向 hsp，就是双向链表的尾结点

        //演示，从头到尾进行遍历
        System.out.println("==========从头到尾进行遍历=============");
        while(true){
            if(first == null){
                break;
            }
            //输出 last 信息
            System.out.println(first);
            first = first.next;
        }

        //演示，从尾到头的遍历
        System.out.println("=============从尾到头的遍历=============");
        while(true){
            if(last == null){
                break;
            }
            System.out.println(last);
            last = last.pre;
        }

        //1. 先创建一个 Node 结点，name 就是 smith
        Node smith = new Node("smith");
        //下面就把 smith 加入到双向链表
        smith.next = hsp;
        smith.pre = tom;
        hsp.pre = smith;
        tom.next = smith;

        first = jack;
        System.out.println("==========从头到尾遍历==========");
        while(true){
            if(first == null){
                break;
            }
            System.out.println(first);
            first = first.next;
        }

        last = hsp;//last 重新指向最后一个结点
        //演示，从尾到头的遍历
        System.out.println("=============从尾到头的遍历=============");
        while(true){
            if(last == null){
                break;
            }
            System.out.println(last);
            last = last.pre;
        }


    }
}

class Node{
    public Object item;
    public Node next;
    public Node pre;
    public Node(Object name){
        this.item = name;
    }

    public String toString(){
        return "Node name=" + item;
    }
}