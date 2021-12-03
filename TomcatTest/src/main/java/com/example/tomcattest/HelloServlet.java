package com.example.tomcattest;

import java.io.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;


import javax.servlet.*;
import java.io.IOException;

@WebServlet(name = "helloServlet", value = "/helloServlet")
public class HelloServlet implements Servlet {
    @Override
    public void init(ServletConfig servletConfig) throws ServletException {

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
