package hsp_Java.chapter15;

import org.junit.jupiter.api.Test;

public class JUnit_ {
    public static void main(String[] args) {
        new JUnit_().m1();
        new JUnit_().m2();
        new JUnit_().m3();
    }

    @Test
    public void m1(){
        System.out.println("m1 方法被调用");
    }
    @Test
    public void m2(){
        System.out.println("m2 方法被调用");
    }
    @Test
    public void m3(){
        System.out.println("m3 方法被调用");
    }
}
