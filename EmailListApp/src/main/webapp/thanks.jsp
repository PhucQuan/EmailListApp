<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thanks</title>
    <style>
        body { font-family: Arial, Helvetica, sans-serif; }
        .container { max-width: 640px; margin: 40px auto; }
        .value { font-weight: bold; }
        a { display: inline-block; margin-top: 16px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Thanks for joining our email list</h2>
        <p>Here is the information that you entered:</p>
        <p>Email: <span class="value">${user.email}</span></p>
        <p>First Name: <span class="value">${user.firstName}</span></p>
        <p>Last Name: <span class="value">${user.lastName}</span></p>

        <a href="index.jsp">Return</a>
    </div>
    
</body>
</html>

