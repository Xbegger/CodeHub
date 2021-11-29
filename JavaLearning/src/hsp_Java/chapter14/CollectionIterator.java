package hsp_Java.chapter14;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class CollectionIterator {
    @SuppressWarnings({"all"})
    public static void main(String[] args) {

        Collection col = new ArrayList();

        col.add(new Book("三国演义", "罗贯中", 10.1));
        col.add(new Book("小李飞刀", "古龙", 5.1));
        col.add(new Book("红楼梦", "曹雪芹", 34.6));

        System.out.println("col = " + col);

        Iterator iterator = null;

        Object obj = iterator.toString();
        while(iterator.hasNext()){
            obj = iterator.next();
            System.out.println("obj=" + obj);


        }
        while(iterator.hasNext()) {
            Object next =  iterator.next();
            System.out.println("obj=" + obj);
        }
    }
}

class Book{
    private String name;
    private String author;
    private double price;

    public Book(String name, String author, double price){
        this.name = name;
        this.author = author;
        this.price = price;
    }

    @Override
    public String toString(){
        return "Book{" +
                "name=" + name + '\'' +
                ",author=" + author + '\'' +
                ",price=" + price + '}';
    }
}