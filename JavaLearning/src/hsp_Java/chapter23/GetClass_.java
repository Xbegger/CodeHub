package hsp_Java.chapter23;

public class GetClass_ {
    public static void main(String[] args)
        throws ClassNotFoundException{

//        1. CLass.forName
        String classAllPath = "hsp_Java.chapter23.Car";
        Class<?> cls1 = Class.forName(classAllPath);
        System.out.println(cls1);

//        2. 类名.class, 用于参数传递
        Class cls2 = Car.class;
        System.out.println(cls2);

//        3. 对象.getClass(),用于有实例对象
        Car car = new Car();
        Class cls3 = car.getClass();
        System.out.println(cls3);

//        4. 通过类加载器 来获取到类的 Class 对象
        ClassLoader classLoader = car.getClass().getClassLoader();
        Class cls4 = classLoader.loadClass(classAllPath);
        System.out.println(cls4);

//        cls1, cls2, cls3, cls4 其实是同一个对象
        System.out.println(cls1.hashCode());
        System.out.println(cls2.hashCode());
        System.out.println(cls3.hashCode());
        System.out.println(cls4.hashCode());

//        5. 基本数据
        Class<Integer> integerClass = int.class;
        Class<Character> characterClass = char.class;
        Class<Boolean> booleanClass = boolean.class;
        System.out.println(integerClass);

//        6. 基本数据类型对应的包装类, 可以通过 .TYPE 得到 Class 类对象
        Class<Integer> type1 = Integer.TYPE;
        Class<Character> type2 = Character.TYPE;
        System.out.println(type1);

        System.out.println(integerClass.hashCode());
        System.out.println(type1.hashCode());
    }
}
