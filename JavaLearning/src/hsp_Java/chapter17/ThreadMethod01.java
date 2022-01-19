package hsp_Java.chapter17;

public class ThreadMethod01 {
    public static void main(String[] args) throws InterruptedException{
        ThreadDemo1 td = new ThreadDemo1();
        td.setName("小笼包");
        td.setPriority(Thread.MIN_PRIORITY);
        td.start();
        System.out.println("默认优先级=" + Thread.currentThread().getPriority());
        Thread.sleep(3000);
        td.interrupt();
    }
}
class ThreadDemo1 extends Thread{
    @Override
    public void run(){
        for(int i=0 ; i<100 ; i++){
            System.out.println(Thread.currentThread().getName() + "吃包子-------" + i);

            try{
                System.out.println(Thread.currentThread().getName() + "休眠中-------");
                Thread.sleep(20000);
            }catch (InterruptedException e){
                System.out.println(Thread.currentThread().getName() + "被 Interrupt 了");
    //            e.printStackTrace();
            }
        }
    }
}