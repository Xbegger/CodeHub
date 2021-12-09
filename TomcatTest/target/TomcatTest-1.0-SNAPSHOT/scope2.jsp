<%--
  Created by IntelliJ IDEA.
  User: Robot_Zero
  Date: 2021/12/5
  Time: 12:06
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    <h1>scope2.jsp 页面</h1>
    pageContext 域是否有值: <%=pageContext.getAttribute("key")%><br>
    request 域是否有值: <%=request.getAttribute("key")%><br>
    session 域是否有值: <%=session.getAttribute("key")%><br>
    applicvation 域是否有值： <%=application.getAttribute("key")%><br>

</body>
</html>
