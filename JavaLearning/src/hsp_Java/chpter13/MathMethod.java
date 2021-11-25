package hsp_Java.chpter13;

public class MathMethod {
    public static void main(String[] args) {
        // 1. abs 绝对值
        int abs = Math.abs(-9);
        System.out.println(abs);

        // 2. pow 求幂
        double pow = Math.pow(2, 4);
        System.out.println(pow);

        // 3. ceil 向上取整， 返回>= 该参数的最小整数(转成 double)
        double ceil = Math.ceil(3.9);
        System.out.println(ceil);

        // 4. floor 向下取整，返回<= 该参数的最大整数(转成 double)
        double floor = Math.floor(4.001);
        System.out.println(floor);

        // 5. round 四舍五入 Math.floor(该参数+0.5)
        long round = Math.round(5.51);
        System.out.println(round);

        // 6. sqrt 求求开方
        double sqrt = Math.sqrt(9.0);
        System.out.println(sqrt);

        for(int i=0; i<100; i++){
            System.out.println((int)(2 + Math.random() * (7 - 2 + 1)));
        }
        int min = Math.min(1, 9);
        int max = Math.max(45, 90);
        System.out.println("min = " + min);
        System.out.println("max = " + max);
    }
}
