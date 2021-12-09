package com.example.tomcattest;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.lang.reflect.Method;

@WebServlet(name = "sessionServlet", value = "/sessionServlet")
public class SessionServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doPost(req, resp);
    }

    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 解决post请求中文乱码问题
        // 一定要在获取请求参数之前调用才有效
        req.setCharacterEncoding("UTF-8");
        // 解决响应中文乱码问题
        resp.setContentType("text/html; charset=UTF-8");

        String action = req.getParameter("action");
        try {
            // 获取action业务鉴别字符串，获取相应的业务 方法反射对象
            Method method = this.getClass().getDeclaredMethod(action, HttpServletRequest.class, HttpServletResponse.class);
//            System.out.println(method);
            // 调用目标业务 方法
            method.invoke(this, req, resp);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * 往 Session 中保存数据
     * @param req
     * @param resp
     * @throws ServletException
     * @throws IOException
     */
    protected void setAttribute(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        req.getSession().setAttribute("key1", "value1");
        req.getSession().setAttribute("user", "root");
        resp.getWriter().write("已经往 Session 中保存了数据");
    }
    /**
     * 获取 Session 域中的数据
     * @param req
     * @param resp
     * @throws ServletException
     * @throws IOException
     */
    protected void getAttribute(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        Object attribute = req.getSession().getAttribute("key1");
        resp.getWriter().write("从 Session 中获取出 key1 的数据是" + attribute);
    }

    protected void life3(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{

        HttpSession session = req.getSession();

        session.setMaxInactiveInterval(3);

        resp.getWriter().write("当前 Session 已经设置为 3 秒后超时");
    }

    protected void deleteNow(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        HttpSession session = req.getSession();

        session.invalidate();

        resp.getWriter().write("Session 已经设置为超时（无效）");
    }
}
