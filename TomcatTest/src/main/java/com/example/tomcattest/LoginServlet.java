package com.example.tomcattest;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "loginServlet", value = "/loginServlet")
public class LoginServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        String username = req.getParameter("username");
        String password = req.getParameter("password");

        if( "user".equals(username) && "123456".equals(password)){
            Cookie cookie = new Cookie("user", username);
            cookie.setMaxAge(60 * 60 * 24 * 7);
            resp.addCookie( cookie );
            System.out.println("登录成功");
        }else{
            System.out.println("登录失败");
        }
    }
}
