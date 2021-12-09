package com.example.tomcattest;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "servlet1", value = "/servlet1")
public class Servlet1 extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        String username = req.getParameter("username");
        System.out.println("在 Servlet1 (柜台 1) 中查看参数 (材料):" + username);

        req.setAttribute("key1", "柜台 1的章");

        //转发
        //  "/" 表示为 http://ip:port/工程名/
        RequestDispatcher requestDispatcher = req.getRequestDispatcher("/servlet2");
        requestDispatcher.forward(req, resp);

    }
}
