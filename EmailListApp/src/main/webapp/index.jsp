<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="email.business.User" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Join our email list</title>
    <style>
        body { font-family: Arial, Helvetica, sans-serif; }
        .container { max-width: 640px; margin: 40px auto; }
        label { display: inline-block; width: 120px; margin: 8px 0; }
        input[type="text"], input[type="email"] { width: 300px; padding: 6px 8px; }
        .error { color: #c00; margin: 12px 0; }
        .actions { margin-top: 12px; }
    </style>
    <%
        User user = (User) request.getAttribute("user");
        if (user == null) {
            user = new User();
        }
        String message = (String) request.getAttribute("message");
        if (message == null) message = "";
    %>
</head>
<body>
    <div class="container">
        <h2>Join our email list</h2>
        <p>To join our email list, enter your name and email address below.</p>

        <% if (!message.isEmpty()) { %>
            <div class="error"><%= message %></div>
        <% } %>

        <form action="emailList" method="post">
            <input type="hidden" name="action" value="add">

            <div>
                <label for="email">Email:</label>
                <input id="email" name="email" type="email" value="<%= user.getEmail() %>" />
            </div>

            <div>
                <label for="firstName">First Name:</label>
                <input id="firstName" name="firstName" type="text" value="<%= user.getFirstName() %>" />
            </div>

            <div>
                <label for="lastName">Last Name:</label>
                <input id="lastName" name="lastName" type="text" value="<%= user.getLastName() %>" />
            </div>

            <div class="actions">
                <button type="submit">Join Now</button>
            </div>
        </form>
    </div>
</body>
</html>

