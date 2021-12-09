package com.example.tomcattest;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "requestAPIServlet", value = "/requestAPIServlet")
public class RequestAPIServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        System.out.println("URL =>" + req.getRequestURI());
        System.out.println("URL =>" + req.getRequestURL());

        System.out.println("客户端 ip 地址 =>" + req.getRemoteHost());
        System.out.println("请求头 User-Agent ==>>" + req.getHeader("User-Agent"));
        System.out.println("请求的方式 ==>>" + req.getMethod());
    }
}
