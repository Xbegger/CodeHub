<%--
  Created by IntelliJ IDEA.
  User: Robot_Zero
  Date: 2021/12/5
  Time: 15:46
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    <h1 align="center"> 九九乘法口诀表 </h1>
    <table align="center">
        <% for(int i = 1; i <= 9; i++){ %>
          <tr>
              <% for(int j=1; j <= i; j++){%>
                <td><%=j + "x" + i + "=" + (i * j)%></td>
              <%}%>
          </tr>
        <%}%>
    </table>
</body>
</html>
