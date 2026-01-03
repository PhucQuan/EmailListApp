package murach.cart;

import java.io.*;
import jakarta.servlet.*; // <-- restore jakarta for Tomcat 11
import jakarta.servlet.http.*;
import murach.business.*;
import murach.data.*;
public class CartServlet extends HttpServlet {
    
    @Override
    protected void doPost(HttpServletRequest request, 
                         HttpServletResponse response)
            throws ServletException, IOException {
        
        String url = "/index.html";
        String action = request.getParameter("action");
        
        if (action == null) {
            action = "cart";
        }
        
        if (action.equals("cart")) {
            url = "/cart.jsp";
        } 
        else if (action.equals("shop")) {
            url = "/index.html";
        } 
        else if (action.equals("add")) {
            String productCode = request.getParameter("productCode");
            Product product = ProductDB.getProduct(productCode);

            if (product == null) {
                request.setAttribute("errorMessage", "Product not found: " + productCode);
                url = "/index.html";
            } else {
                LineItem item = new LineItem();
                item.setProduct(product);
                item.setQuantity(1);

                HttpSession session = request.getSession();
                Cart cart = (Cart) session.getAttribute("cart");

                if (cart == null) {
                    cart = new Cart();
                }

                cart.addItem(item);
                session.setAttribute("cart", cart);

                url = "/cart.jsp";
            }
        }
        else if (action.equals("update")) {
            String productCode = request.getParameter("productCode");
            String quantityString = request.getParameter("quantity");
            int quantity = Integer.parseInt(quantityString);
            
            HttpSession session = request.getSession();
            Cart cart = (Cart) session.getAttribute("cart");
            
            if (cart != null) {
                for (LineItem item : cart.getItems()) {
                    if (item.getProduct().getCode().equals(productCode)) {
                        if (quantity > 0) {
                            item.setQuantity(quantity);
                        } else {
                            cart.removeItem(item);
                        }
                        break;
                    }
                }
            }
            
            url = "/cart.jsp";
        } 
        else if (action.equals("remove")) {
            String productCode = request.getParameter("productCode");
            
            HttpSession session = request.getSession();
            Cart cart = (Cart) session.getAttribute("cart");
            
            if (cart != null) {
                for (LineItem item : cart.getItems()) {
                    if (item.getProduct().getCode().equals(productCode)) {
                        cart.removeItem(item);
                        break;
                    }
                }
            }
            
            url = "/cart.jsp";
        }
        
        getServletContext()
                .getRequestDispatcher(url)
                .forward(request, response);
    }
    
    @Override
    protected void doGet(HttpServletRequest request,
                        HttpServletResponse response)
            throws ServletException, IOException {
        doPost(request, response);
    }
}