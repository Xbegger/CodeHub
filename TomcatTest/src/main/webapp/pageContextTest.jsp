<%--
  Created by IntelliJ IDEA.
  User: Robot_Zero
  Date: 2021/12/5
  Time: 19:57
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<%--    <% pageContext.setAttribute("req", request);%>--%>

<%--    <%=request.getScheme()%><br>--%>
    1. 协议：${pageContext.request.scheme} <br>
    2. 服务器ip:${pageContext.request.serverName}<br>
    3. 服务器端口:${pageContext.request.serverPort}<br>
    4. 获取工程路径:${pageContext.request.contextPath}<br>
    5. 获取请求方法：${pageContext.request.method}<br>
    6. 获取客户端 ip 地址:${pageContext.request.remoteHost}<br>
    7. 获取会话的 id 编号:${pageContext.session.id}<br>
</body>
</html>
