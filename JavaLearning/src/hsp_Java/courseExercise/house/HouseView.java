package hsp_Java.courseExercise.house;

import java.util.Scanner;

public class HouseView {
    private HouseService houseService;

    public HouseView(){
        this.houseService = new HouseService();
    }

    public void mainApp(){
        Scanner scanner = new Scanner(System.in);
        int choice;
        do{
            this.mainMenu();
            System.out.println("请输入(1-6):");
            choice = scanner.nextInt();
            switch (choice){
                case 1:
                    this.addHouses(scanner);
                    break;
                case 2:
                    this.findHouse(scanner);
                    break;
                case 3:
                    this.delHouse(scanner);
                    break;
                case 4:
                    this.updateHouse(scanner);
                    break;
                case 5:
                    this.listHouse();
                    break;

                case 6:
                    System.out.println("你退出了程序~~");
                    return;
                default:
                    System.out.println("错误的选项！请重新输入选择！");
                    break;
            }

        }while(true);

    }

    public void mainMenu(){
        System.out.println("--------------------房屋出租系统---------------------");
        System.out.println("              1 新 增 房 源");
        System.out.println("              2 查 找 房 屋");
        System.out.println("              3 删 除 房 屋");
        System.out.println("              4 修 改 房 屋 信 息");
        System.out.println("              5 房 屋 列 表");
        System.out.println("              6 退    出");
    }
    public void addHouses(Scanner scanner){
        System.out.println("--------------------添加房屋-----------------------");
        System.out.print("姓名:");
        String houseOwner = scanner.next();
        System.out.print("电话:");
        int phone = scanner.nextInt();
        System.out.print("地址:");
        String address = scanner.next();
        System.out.print("月租:");
        int monthlyRent = scanner.nextInt();
        System.out.print("状态(未出租/已出租):");
        String status = scanner.next();
        this.houseService.create(houseOwner,phone,address,monthlyRent,status);
        System.out.println("--------------------添加完成-----------------------");
    }
    public void findHouse(Scanner scanner){
        System.out.println("--------------------查找房屋-----------------------");
        System.out.print("请输入你要找的id:");
        int no = scanner.nextInt();
        System.out.println(this.houseService.find(no));
    }
    public void delHouse(Scanner scanner){
        System.out.println("--------------------删除房屋-----------------------");
        System.out.print("请选择待删除房屋编号(-1退出):");
        int no = scanner.nextInt();
        if(no == -1){
            System.out.println("--------------------退出删除-----------------------");
            return;
        }
        System.out.println(this.houseService.find(no));
        System.out.println("确认是否删除(Y/N)，请小心选择:");
        System.out.println("请输入你的选择");
        String choice = scanner.next();
        if(choice.equals("Y")){
            this.houseService.delete(no);
            System.out.println("--------------------删除完成-----------------------");
        }else{
            System.out.println("--------------------取消删除-----------------------");
        }
    }

    public void listHouse(){
        System.out.println("--------------------房屋列表-----------------------");
        this.houseService.read();
        System.out.println("--------------------房屋列表完成--------------------");
    }
    public void updateHouse(Scanner scanner){
        System.out.println("--------------------修改房屋-----------------------");
        System.out.print("请选择待删除房屋编号(-1退出):");
        int no = scanner.nextInt();
        if(no == -1){
            System.out.println("--------------------退出修改-----------------------");
            return;
        }
        House house = this.houseService.find(no);
        System.out.format("姓名(%s):" , house.getHouseOwner());
        String houseOwner = scanner.next();
        System.out.format("电话(%d):", house.getPhone());
        int phone = scanner.nextInt();
        System.out.format("地址(%s):", house.getAddress());
        String address = scanner.next();
        System.out.format("月租(%d):", house.getMonthlyRent());
        int monthlyRent = scanner.nextInt();
        System.out.format("状态(%s):", house.getStatus().getStatus());
        String status = scanner.next();
        house.setAttributes(houseOwner, phone, address, monthlyRent, status);
        System.out.println("--------------------修改完成-----------------------");
    }

}
