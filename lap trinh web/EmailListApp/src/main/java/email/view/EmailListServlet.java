package email.view;

import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

import email.business.User;
import email.data.UserDB;

@WebServlet(name = "EmailListServlet", urlPatterns = {"/emailList"})
public class EmailListServlet extends HttpServlet {
    
    @Override
    protected void doPost(HttpServletRequest request, 
                         HttpServletResponse response)
            throws ServletException, IOException {
        
        String url = "/index.jsp";
        
        String action = request.getParameter("action");
        if (action == null) {
            action = "join";
        }
        
        if (action.equals("join")) {
            url = "/index.jsp";
        }
        else if (action.equals("add")) {
            String firstName = request.getParameter("firstName");
            String lastName = request.getParameter("lastName");
            String email = request.getParameter("email");
            
            User user = new User(firstName, lastName, email);
            
            String message;
            if (firstName == null || lastName == null || email == null ||
                firstName.isEmpty() || lastName.isEmpty() || email.isEmpty()) {
                message = "Please fill out all three text boxes.";
                url = "/index.jsp";
            }
            else {
                message = "";
                url = "/thanks.jsp";
                String storagePath = getServletContext().getRealPath("/WEB-INF/emails/UserEmail.txt");
                UserDB.insert(user, storagePath);
            }
            
            request.setAttribute("user", user);
            request.setAttribute("message", message);
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