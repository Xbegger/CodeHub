package com.example.tomcattest;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.lang.reflect.Method;

@WebServlet(name = "cookieTest", value = "/cookieTest")
public class cookieTest extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        doPost(req, resp);
    }
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{

        // 解决 post 请求中文乱码问题
        // 一定要在获取请求参数之前调用才有效
        req.setCharacterEncoding("UTF-8");
        // 解决响应中文乱码问题
        resp.setContentType("text/html;charset=UTF-8");


        String action = req.getParameter("action");

        try{
            Method method = this.getClass().getDeclaredMethod(action, HttpServletRequest.class, HttpServletResponse.class);
            method.invoke(this, req, resp);
        }catch(Exception e){
            e.printStackTrace();
        }
    }

    protected void testPath(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        Cookie cookie = new Cookie("path1", "path1");
        cookie.setPath(req.getContextPath() + "/abc");
        resp.addCookie( cookie );
        resp.getWriter().write(req.getContextPath());
        resp.getWriter().write("创建了一个带有 Path 路径的 Cookie");
    }
    protected void createCookie(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        Cookie cookie = new Cookie("key4", "value4");
        resp.addCookie(cookie);

        Cookie cookie1 = new Cookie("key5", "value5");
        resp.addCookie(cookie1);

        resp.getWriter().write("Cookie 创建成功");
    }

    protected void getCookie(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{

        Cookie[] cookies = req.getCookies();

        for(Cookie cookie : cookies){
            resp.getWriter().write("Cookie[" + cookie.getName() + "="
                                        + cookie.getValue() + "]<br>");
        }
        Cookie iWantCookie = CookieUtils.findCookie("key4", cookies);

        if( iWantCookie != null){
            resp.getWriter().write("找到了需要的Cookie 【" + iWantCookie.getName() + "="
                                      + iWantCookie.getValue() + "】");
        }
    }

    protected void editCookie(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{

        // 方案一
        Cookie cookie = new Cookie("key1", "newValue1");

        resp.addCookie(cookie);

        // 方案二
        Cookie cookie1 = CookieUtils.findCookie("key2", req.getCookies());
        if( cookie != null){
            cookie.setValue("newValue2");
            resp.addCookie(cookie1);
        }
    }

    /**
     * 设置存活 1 个小时的 Cooie
     * @param req
     * @param resp
     * @throws ServletException
     * @throws IOException
     */
    protected void life3600(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{

        Cookie cookie = new Cookie("life3600", "life3600");

        cookie.setMaxAge(60 * 60);
        resp.addCookie(cookie);
        resp.getWriter().write("已经创建了一个存活一小时的 Cookie");
    }
    /**
     * 马上删除一个 Cookie
     * @param req
     * @param resp
     * @throws ServletException
     * @throws IOException
     */
    protected void deleteNow(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{

        Cookie cookie = CookieUtils.findCookie("key4", req.getCookies());
        if(cookie != null){
            cookie.setMaxAge(0);
            resp.addCookie(cookie);
            resp.getWriter().write("key4 的 Cookie 已经被删除");
        }
    }

    /**
     * 默认的会话级别的 Cookie
     * @param req
     * @param resp
     * @throws ServletException
     * @throws IOException
     */
    protected void defaultLife(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException{
        Cookie cookie = new Cookie("defaultLife", "defaultLife");
        cookie.setMaxAge(-1);
        resp.addCookie(cookie);
    }
}
