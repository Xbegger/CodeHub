package hsp_Java.chapter17;

public class ThreadMethod02 {
    public static void main(String[] args)
        throws InterruptedException{
        T t1 = new T();
        t1.start();
//        t1.join();
        for(int i=1 ; i<=20 ; i++){
            Thread.sleep(50);
            System.out.println("张三丰" + i);
        }
    }
}

class T extends Thread{
    @Override
    public void run(){
        for(int i=1 ; i<=20 ; i++){
            try{
                Thread.sleep(50);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
            System.out.println("JoinThread ----------" + i);
        }
    }
}