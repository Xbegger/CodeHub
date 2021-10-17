package basic.VariableType;

public class Emplpyee {
    public String name;

    private double salary;

    public Emplpyee(String empName){
        name = empName;
    }

    public void setSalary(double empSal){
        salary = empSal;
    }
    public void printEmp(){
        System.out.println("名字 : " + name);
        System.out.println("薪水 : " + salary);

    }

    public static void main(String[] args) {
        Emplpyee emp = new Emplpyee("nowcoder");
        emp.setSalary(1000);
        emp.printEmp();
    }
}
