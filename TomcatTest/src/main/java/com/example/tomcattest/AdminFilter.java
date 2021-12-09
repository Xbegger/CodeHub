package com.example.tomcattest;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.annotation.WebInitParam;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.security.spec.RSAOtherPrimeInfo;


@WebFilter(filterName = "AdminFilter", urlPatterns = "/cookieTest", initParams = {
        @WebInitParam(name = "username", value = "root"),
        @WebInitParam(name = "url", value = "jdbc:mysql://localhost:3306/test")
})
public class AdminFilter implements Filter {

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain)
        throws IOException, ServletException{
        HttpServletRequest httpServletRequest = (HttpServletRequest) servletRequest;

        HttpSession session = httpServletRequest.getSession();
        Object user = session.getAttribute("user");
        if(user == null){
            servletRequest.getRequestDispatcher("/index.jsp").forward(servletRequest, servletResponse);
        } else {
            filterChain.doFilter(servletRequest, servletResponse);
        }
    }

    @Override
    public void init(FilterConfig filterConfig)
        throws ServletException{
        System.out.println("2. Filter 的 init(FilterConfig filterconfig) 初始化)");

        System.out.println("filter-name 的值是：" + filterConfig.getFilterName());

        System.out.println("初始化参数 username 的值是：" + filterConfig.getInitParameter("username"));
        System.out.println("初始化参数 url 的值是：" + filterConfig.getInitParameter("url"));

        System.out.println(filterConfig.getServletContext());
    }
}
