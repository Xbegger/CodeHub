package hsp_Java.chapter17;

public class Thread01 {
    public static void main(String[] args) throws InterruptedException{

        // 创建 Cat 对象，当作线程使用
        Cat cat = new Cat();

        cat.start();
//        cat.run();//只是一个方法，不是一个线程
        System.out.println("主线程继续执行" + Thread.currentThread().getName());

        for(int i=0; i<60 ; i++){
            System.out.println("主线程 i=" + i);
            Thread.sleep(1000);
        }
    }
}
class Cat extends Thread{
    int times = 0;

    @Override
    public void run(){
        while(true){
            System.out.println("喵喵，我是小猫咪" + (++times) +
                    "线程名 = " + Thread.currentThread().getName());
            try{
                Thread.sleep(1000);
            }catch (InterruptedException e){
                e.printStackTrace();;
            }
            if(times == 80){
                break;
            }
        }
    }
}