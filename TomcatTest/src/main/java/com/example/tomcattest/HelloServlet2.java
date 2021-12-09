package com.example.tomcattest;

import javax.servlet.annotation.WebInitParam;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.rmi.ServerException;


@WebServlet(name = "helloServlet2", value = "/helloServlet2")
public class HelloServlet2 extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
        throws IOException{
        System.out.println("HelloServlet2 的 doGet 方法");
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
        throws ServerException, IOException{
        System.out.println("HelloServlet2 的 doPost 方法");
    }
}
