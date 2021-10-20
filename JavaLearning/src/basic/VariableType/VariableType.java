package basic.VariableType;

public class VariableType {
    public static void main(String[] args) {
        int a, b, c;
        int d = 3, e = 4, f = 5;
        byte z = 22;
        String s = "nowcoder";
        double pi = 3.14159;
        char x = 'x';


        // 局部变量
        VariableType test = new VariableType();
        test.setAge();
    }

    public void setAge(){
        int age = 0;
        age = age + 7;
        System.out.println("小狗的年龄是" + age);
    }
}

