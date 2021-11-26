package hsp_Java.chapter10;

public class AbstractClassDetail01 {
    public static void main(String[] args) {
        Template t = new A();
        t.done();
        A a = (A)t;
        System.out.println(a.getClass());
    }
}

abstract class Template{

    abstract public void done();
}
class A extends Template{

    @Override
    public void done(){
        System.out.println("A done");
    }
}
class B extends Template{

    @Override
    public void done(){
        System.out.println("B done");
    }
}