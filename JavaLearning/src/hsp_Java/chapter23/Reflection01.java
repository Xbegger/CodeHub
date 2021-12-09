package hsp_Java.chapter23;

import java.io.FileInputStream;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Properties;

public class Reflection01 {

    public static void main(String[] args) throws Exception{
        //1. 使用Properties 类，读写配置文件
        Properties properties = new Properties();
        properties.load(new FileInputStream("src\\re.propperties"));
        String classfullpath = properties.get("classfullpath").toString();
        String methodName = properties.get("method").toString();

        //2. 使用反射机制
        Class cls = Class.forName(classfullpath);//(1) 加载类，返回 Class 类型的对象 cls
        Object o = cls.newInstance();//(2) 通过cls得到 加载的类   的 对象实例
        System.out.println("o 的运行类型" + o.getClass());

        // 方法反射
        Method method1 = cls.getMethod(methodName);//(3)通过 cls 得到加载类的 方法对象
        System.out.println("============================");

        method1.invoke(o);//(4) 通过method1 调用方法，即通过方法对象来实现调用方法

        // 成员反射
        Field nameField = cls.getField("age");
        System.out.println(nameField.get(o));

        //构造器反射
        Constructor constructor = cls.getConstructor();
        System.out.println(constructor);

        Constructor constructor2 = cls.getConstructor(String.class);// 有参数构造器
        System.out.println(constructor2);
    }
}
