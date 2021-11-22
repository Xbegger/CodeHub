package hsp_Java.courseExercise.house;

public class HouseService {
    private House[] houses;
    private int numOfHouses;
    static final int MAX_HOUSES = 40;

    public HouseService(){
        this.houses = new House[MAX_HOUSES];
        this.numOfHouses = 0;
    }

    public boolean create(String houseOwner, int phone, String address, int monthlyRent, String status){
        if(this.numOfHouses == MAX_HOUSES){
            return false;
        }

        this.houses[numOfHouses] = new House(numOfHouses + 1, houseOwner, phone,
                                            address, monthlyRent, status);
        this.numOfHouses += 1;
        return true;
    }
    public void read(){
        for(int i=0 ; i<this.numOfHouses ; i++){
            System.out.println(this.houses[i]);
        }
    }

    public House find(int no){
        if(no < 1 || no > this.numOfHouses){
            return null;
        }
        return this.houses[no -1];
    }
    public void update(int no, String houseOwner, int phone, String address, int monthlyRent, String status){
        this.houses[no - 1].setAttributes(houseOwner, phone, address, monthlyRent, status);
    }
    public void delete(int no){
        if(no == 0){
            no = 1;
        }
        for(int i=no ; i<this.numOfHouses ; i++){
            this.houses[i -1] = houses[i];
        }
        this.numOfHouses -= 1;
    }
}
