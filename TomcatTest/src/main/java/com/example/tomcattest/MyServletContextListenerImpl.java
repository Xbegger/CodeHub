package com.example.tomcattest;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;

@WebListener
public class MyServletContextListenerImpl implements ServletContextListener {
    @Override
    public void contextInitialized(ServletContextEvent sce){
        System.out.println("ServletContext 对象被创建了");
    }

    @Override
    public void contextDestroyed(ServletContextEvent sce){
        System.out.println("ServletContext 对象被销毁了");
    }
}
