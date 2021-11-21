package hsp_Java.courseExercise.changes;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

enum Option{
    DETAIL, INCOME, COST, EXIT;

    public static Option valueOf(int value){
        switch (value){
            case 1:
                return DETAIL;
            case 2:
                return INCOME;
            case 3:
                return COST;
            case 4:
                return EXIT;
            default:
                return null;
        }
    }
}

public class SmallChangesSys {
    public static void main(String[] args) {

        int choice;
        Scanner input = new Scanner(System.in);
        ChangeDetail data = new ChangeDetail();

        Option option;

        do{
            menuView();
            choice = input.nextInt();
            option = Option.valueOf(choice);

            switch (option){
                case DETAIL:
                    changeDetail(data);
                    break;
                case INCOME:

            }

        }while(choice != 4);

    }


    static void menuView(){
        System.out.println("-----------零钱通-----------");
        System.out.println("       1 零钱通明细");
        System.out.println("       2 收益入账");
        System.out.println("       3 消费");
        System.out.println("       4 退     出");
        System.out.println("请选择(1-4):");
    }
    static void changeDetail(ChangeDetail head){
        changeDetailsView();
        traverseChangeDetails(head);
    }
    static void changeDetailsView(){
        System.out.println("-----------零钱通明细------------");
    }
    static void traverseChangeDetails(ChangeDetail head){
        if(head == null){
            return ;
        }
        System.out.println(head);
        traverseChangeDetails(head.next);
    }
}
class ChangeDetail{
    private int type;
    private String item;
    private double money;
    private Date time;
    private double balanceNow;
    public ChangeDetail next;

    static SimpleDateFormat ft = new SimpleDateFormat("yyyy-MM-dd hh:mm");
    static double  balance = 0.0;
    public ChangeDetail(int type, String item, double money){
        this.type = type;
        this.item = item;
        this.money = money;
        this.time = new Date();
        if(type == 2){
            balance = balance + money;
        }else{
            balance = balance - money;
        }
        this.balanceNow = balance;
    }
    public ChangeDetail(){

    }

    public void setNext(ChangeDetail next){
        this.next = next;
    }

    public ChangeDetail getNext() {
        return next;
    }
    @Override
    public String toString(){
        return item + "\t"
                + (type == 2? "+" : "-") + "\t"
                + money + "\t"
                + ft.format(time) + "\t"
                + "余额:" + balanceNow;


    }
}
