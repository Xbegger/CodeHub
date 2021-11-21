package hsp_Java.courseExercise.chapter8;

public class Homework03 {
    /**
     * 1. 要求属性 姓名name， 年龄，age， 职称post，基本工资salary
     * 2. 编写业务方法，introduce()， 试下你输出一个教师信息
     * 3. 编写三个子类：教授类，副教授类，讲师类。
     *    工资级别分别为：教授1.3， 副教授1.2， 讲师类1.1
     *    在三个子类的方法里重写父类的introduce()方法
     * 4. 定义并初始化一个老师对象，调用业务方法，实现基本信息的后台打印
     */
    public static void main(String[] args) {
        Teacher[] teacher = new Teacher[4];
        teacher[0] = new Teacher("a", 20, "教师", 1);
        teacher[1] = new Professor("b", 23, "教师", 1.3);
        teacher[2] = new AssociateProfessor("c", 22, "副教授", 1.2);
        teacher[3] = new Lecturer("d", 21, "讲师", 1.1);
        for(int i=0 ; i<teacher.length ; i++) {
            teacher[i].introduce();
        }
    }
}

class Teacher{
    private String name;
    private int age;
    private String post;
    private double salary;

    public Teacher(){

    }
    public Teacher(String name, int age, String post, double salary){
        this.setName(name);
        this.setAge(age);
        this.setPost(post);
        this.setSalary(salary);
    }

    public void introduce(){
        String msg = "教师-" + this.getName()
                   + ", 年龄为 " + this.getAge()
                   + ", 基本工资为 " + this.getSalary();
        System.out.println(msg);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getPost() {
        return post;
    }

    public void setPost(String post) {
        this.post = post;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }




}

class Professor extends Teacher{

    public Professor(String name, int age, String post, double salary){
        super(name, age, post, salary);
    }
    @Override
    public void introduce(){
        String msg = "教授-" + this.getName()
                + ", 年龄为 " + this.getAge()
                + ", 基本工资为 " + this.getSalary();
        System.out.println(msg);
    }
}

class AssociateProfessor extends Teacher{
    public AssociateProfessor(String name, int age, String post, double salary){
        super(name, age, post, salary);
    }
    @Override
    public void introduce(){
        String msg = "副教授-" + this.getName()
                + ", 年龄为 " + this.getAge()
                + ", 基本工资为 " + this.getSalary();
        System.out.println(msg);
    }
}

class Lecturer extends Teacher{
    public Lecturer(String name, int age, String post, double salary){
        super(name, age, post, salary);
    }
    @Override
    public void introduce(){
        String msg = "讲师-" + this.getName()
                + ", 年龄为 " + this.getAge()
                + ", 基本工资为 " + this.getSalary();
        System.out.println(msg);
    }
}