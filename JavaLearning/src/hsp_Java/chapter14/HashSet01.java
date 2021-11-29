package hsp_Java.chapter14;

import java.util.HashSet;

@SuppressWarnings({"all"})
public class HashSet01 {

    public static void main(String[] args) {

        HashSet set = new HashSet();

        System.out.println(set.add("john"));
        System.out.println(set.add("lucy"));
        System.out.println(set.add("john"));
        System.out.println(set.add("jack"));
        System.out.println(set.add("Rose"));

        set.remove("john");
        System.out.println("set=" + set);

        set = new HashSet();
        System.out.println("set=" + set);

        set.add("lucy");
        set.add("lucy");
        set.add(new Dog("tom"));
        set.add(new Dog("tom"));
        System.out.println("set=" + set);

        set.add(new String("hsp"));
        set.add(new String("hsp"));

        System.out.println("set=" + set);
    }
}
class Dog{
    private String name;

    public static int i = 0;
    public Dog(String name){
        this.name = name;
        Dog.i += 1;
    }

    public String getName(){
        return name;
    }
    @Override
    public String toString(){
        return "Dog{" +
                "name=" + name + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object obj){
        if(this == obj){
            return true;
        }
        if(obj instanceof  Dog){
            Dog dog = (Dog)obj;
            if(this.name.equals(dog.getName())){
                return true;
            }
        }
        return false;
    }
    @Override
    public int hashCode(){
//        return Dog.i;
        return 0;
    }

}
