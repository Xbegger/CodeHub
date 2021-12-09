package hsp_Java.chapter23;

import java.util.Objects;

public class Car{
    public String brand;
    public double price;

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }



    public Car(String brand, double price){
        this.brand = brand;
        this.price = price;
    }

    public Car(){
        this.brand = "宝马";
        this.price = 0.;
    }
    @Override
    public String toString(){
        return "\nCar{" +
                "brand=" + brand +
                ",price=" + price +
                "}";
    }

    @Override
    public boolean equals(Object o){
        if(this == o)
            return true;
        if(o == null || !(o instanceof Car))
            return false;
        Car car = (Car) o;
        return Double.compare(car.price, price) == 0 &&
                Objects.equals(brand, car.brand);
    }

    @Override
    public int hashCode(){
        return Objects.hash(brand, price);
    }

}
