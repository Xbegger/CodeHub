package hsp_Java.courseExercise.chapter4;

public class ArithmeticOperatorExercise01 {
    public static void main(String[] args) {
        int i = 1;
        i = i++;//规则， （1）temp = i; (2) i = i + 1; (3) i = temp;
        System.out.println(i);//1

        i = 1;
        i = ++ i; // (1)i = i + 1; (2) temp = i; (3) i = temp;
        System.out.println(i);//2
    }
}
