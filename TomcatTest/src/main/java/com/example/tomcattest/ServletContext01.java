package com.example.tomcattest;

import javax.servlet.ServletContext;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.rmi.ServerException;

@WebServlet(name = "servletContext", value = "/servletContext")
public class ServletContext01 extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServerException, IOException{

        response.sendRedirect("http://localhost:8080/TomcatTest/servlet1");

        ServletContext context = getServletConfig().getServletContext();
        String username = context.getInitParameter("username");

        System.out.println("context-param 参数 username 的值是：" + username);
        System.out.println("context-param 参数 password 的值是：" + context.getInitParameter("password"));


        System.out.println("当前工程路径：" + context.getContextPath());

        System.out.println("工程部署的路径是：" + context.getRealPath("/"));
        System.out.println("工程下 css 目录的绝对路径是：" + context.getRealPath("/css"));
        System.out.println("工程下 imgs 目录 1.jpg 的绝对路径是：" + context.getRealPath("/imgs/1.jpg"));


        System.out.println(context);
        System.out.println("在保存之前：Context1 获取 key1 的值是：" + context.getAttribute("key1"));

        context.setAttribute("key1", "value1");

        System.out.println("Context1 中获取域数据 key1 的值是：" + context.getAttribute("key1"));

//        System.out.println(getServletContext().getRealPath("/"));
//        request.getRequestDispatcher("/");

//        response.sendRedirect("/");
    }
}
