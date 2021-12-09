<%--
  Created by IntelliJ IDEA.
  User: Robot_Zero
  Date: 2021/12/5
  Time: 20:09
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    ${cookie.nameTest.value}<br>
    获取 Cookie 的名称: ${ cookie.JSESSIONID.name}<br>
    获取 Cookie 的值: ${ cookie.JSESSIONID.value}<br>
</body>
</html>
