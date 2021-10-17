package basic.VariableType;

public class Emplyee2 {
    private static double salary;
    public static final String DEPARTMENT = "高中部";

    public static void main(String[] args) {
        salary = 10000;
        System.out.println(DEPARTMENT + "平均工资：" + salary);
    }
}
