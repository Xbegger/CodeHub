package hsp_Java.chapter23;


import java.lang.reflect.Field;

public class Class02 {
    public static void main(String[] args)
        throws ClassNotFoundException, IllegalAccessException, InstantiationException,
            NoSuchFieldException{

        String classALlPath = "hsp_Java.chapter23.Car";

        Class<?> cls = Class.forName(classALlPath);

        //2.输出 cls
        System.out.println(cls);
        System.out.println(cls.getClass());

        //3.得到包名
        System.out.println(cls.getPackage().getName());

        //4.得到全类名
        System.out.println(cls.getName());

        //5.通过 cls 创建对象实例
        Car car = (Car)cls.newInstance();
        System.out.println(car);

        //6.通过反射获取属性 brand
        Field brand = cls.getField("brand");
        System.out.println(brand.get(car));

        //7.通过反射给属性赋值
        brand.set(car, "奔驰");
        System.out.println(brand.get(car));

        //8.得到所有的属性(字段）
        System.out.println("=========所有的字段属性============");
        Field[] fields = cls.getFields();
        for(Field f : fields){
            System.out.println(f.getName());
        }
    }
}
