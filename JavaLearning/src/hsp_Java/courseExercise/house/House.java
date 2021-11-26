package hsp_Java.courseExercise.house;

enum Status{
    UNRENT("未出租"),RENTED("已出租");

    private String status;

    private Status(String status){
        this.status = status;
    }

    public String getStatus(){
        return this.status;
    }

}

public class House {
    private int no;
    private String houseOwner;
    private int phone;
    private String address;
    private int monthlyRent;
    private Status status;

    public House(){

        this.status = Status.UNRENT;
    }
    public House(int no, String houseOwner, int phone, String address, int monthlyRent, String status){
        this.setNo(no);
        this.setHouseOwner(houseOwner);
        this.setPhone(phone);
        this.setAddress(address);
        this.setMonthlyRent(monthlyRent);
        this.setStatus(status);
    }
    public void setAttributes(String houseOwner, int phone, String address, int monthlyRent, String status){
        this.setHouseOwner(houseOwner);
        this.setPhone(phone);
        this.setAddress(address);
        this.setMonthlyRent(monthlyRent);
        this.setStatus(status);
    }
    public void setNo(int no){
        this.no = no;
    }
    public void setHouseOwner(String houseOwner){
        this.houseOwner = houseOwner;
    }
    public void setPhone(int phone){
        this.phone = phone;
    }
    public void setAddress(String address){
        this.address = address;
    }
    public void setMonthlyRent(int monthlyRent){
        this.monthlyRent = monthlyRent;
    }
    public void setStatus(String value){
        String status;
        switch(value){
            case "未出租":
                status = "UNRENT";
                break;
            case "已出租":
                status = "RENTED";
                break;
            default:
                return;
        }

        this.status = Enum.valueOf(Status.class, status);
    }
    public Status getStatus(){
        return this.status;
    }

    public String getHouseOwner() {
        return houseOwner;
    }

    public int getPhone() {
        return phone;
    }

    public String getAddress() {
        return address;
    }

    public int getMonthlyRent() {
        return monthlyRent;
    }

    @Override
    public String toString(){
        return this.no + "\t"
                + this.houseOwner + "\t"
                + this.phone + "\t"
                + this.address + "\t"
                + this.monthlyRent + "\t"
                + this.status.getStatus();
    }
}
