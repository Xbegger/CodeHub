package com.example.tomcattest;

import java.io.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;


import javax.servlet.*;
import java.io.IOException;

@WebServlet(name = "helloServlet", value = "/helloServlet",
        initParams = {
                @WebInitParam(name = "username", value = "root"),
                @WebInitParam(name = "url", value = "jdbc:mysql://localhost:3306/test")
        })
public class HelloServlet implements Servlet {
    @Override
    public void init(ServletConfig servletConfig) throws ServletException {
        System.out.println("init 初始化方法");
        System.out.println("HelloServlet 程序的别名是：" + servletConfig.getServletName());
        System.out.println("初始化参数 username 的值是" + servletConfig.getInitParameter("username"));
        System.out.println("初始化参数url 的值是：" + servletConfig.getInitParameter("url"));
        System.out.println(servletConfig.getServletContext());
    }

    @Override
    public ServletConfig getServletConfig() {
        return null;
    }

    /**
     * @function service 方法是专门用来处理请求和响应的
     * @param servletRequest
     * @param servletResponse
     * @throws ServletException
     * @throws IOException
     */
    @Override
    public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws
            ServletException, IOException{
        System.out.println("Hello Servlet 被访问了");

        HttpServletRequest httpServletRequest = (HttpServletRequest) servletRequest;
        // 获取请求的方式
        String method = httpServletRequest.getMethod();

        if("GET".equals(method)){
            doGet();
        }else if("POST".equals(method)){
            doPost();
        }
    }
    public void doGet(){
        System.out.println("get 请求");
    }
    public void doPost(){
        System.out.println("post请求");
    }

    @Override
    public String getServletInfo() {
        return null;
    }

    @Override
    public void destroy() {

    }
}
