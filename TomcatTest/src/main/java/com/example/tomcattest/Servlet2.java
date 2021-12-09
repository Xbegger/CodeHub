package com.example.tomcattest;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "servlet2", value = "/servlet2")
public class Servlet2 extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        String username = req.getParameter("username");
        System.out.println("在 Servlet2 (柜台 2) 中查看参数（材料）：" + username);

        Object key1 = req.getAttribute("key1");
        System.out.println("柜台 1 是否有章" + key1);

        System.out.println("Servlet2 处理自己的业务");
    }
}
