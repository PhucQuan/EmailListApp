<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Murach's Java Servlets and JSP</title>
    <link rel="stylesheet" href="styles/main.css" type="text/css"/>
</head>
<body>

<h1>Your cart</h1>

<table>
    <tr>
        <th>Quantity</th>
        <th>Description</th>
        <th class="right">Price</th>
        <th class="right">Amount</th>
        <th></th>
    </tr>
    
    <c:forEach var="item" items="${cart.items}">
    <tr>
        <td>
            <form action="cart" method="post">
                <input type="hidden" name="action" value="update">
                <input type="hidden" name="productCode" value="${item.product.code}">
                <input type="text" name="quantity" value="${item.quantity}">
                <input type="submit" value="Update">
            </form>
        </td>
        <td>${item.product.description}</td>
        <td class="right">${item.product.priceCurrencyFormat}</td>
        <td class="right">${item.totalCurrencyFormat}</td>
        <td>
            <form action="cart" method="post">
                <input type="hidden" name="action" value="remove">
                <input type="hidden" name="productCode" value="${item.product.code}">
                <input type="submit" value="Remove Item">
            </form>
        </td>
    </tr>
    </c:forEach>
</table>

<p><b>To change the quantity</b>, enter the new quantity and click on the Update button.</p>

<form action="cart" method="post">
    <input type="hidden" name="action" value="shop">
    <input type="submit" value="Continue Shopping">
</form>

<form action="cart" method="post">
    <input type="hidden" name="action" value="checkout">
    <input type="submit" value="Checkout">
</form>

</body>
</html>
```

## BƯỚC 9: KIỂM TRA CẤU TRÚC PROJECT

Cấu trúc project của bạn phải như sau:
```
Cartw5
├── Source Packages
│   ├── murach.business
│   │   ├── Cart.java
│   │   ├── LineItem.java
│   │   └── Product.java
│   ├── murach.cart
│   │   └── CartServlet.java
│   └── murach.data
│       └── ProductDB.java
├── Web Pages
│   ├── styles
│   │   └── main.css
│   ├── cart.jsp
│   ├── index.html
│   └── WEB-INF
│       └── web.xml