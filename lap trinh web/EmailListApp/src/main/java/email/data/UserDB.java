package email.data;

import java.io.*;
import java.nio.charset.StandardCharsets;
import email.business.User;

public class UserDB {
    
    public static void insert(User user) {
        String defaultPath = System.getProperty("user.home") + File.separator + "murach" + File.separator + "email" + File.separator + "UserEmail.txt";
        insert(user, defaultPath);
    }
    
    public static void insert(User user, String filePath) {
        File file = new File(filePath);
        
        try {
            File parent = file.getParentFile();
            if (parent != null && !parent.exists()) {
                parent.mkdirs();
            }
            
            try (PrintWriter out = new PrintWriter(
                    new BufferedWriter(
                        new OutputStreamWriter(
                            new FileOutputStream(file, true), StandardCharsets.UTF_8)))) {
                out.println("Email: " + user.getEmail());
                out.println("First Name: " + user.getFirstName());
                out.println("Last Name: " + user.getLastName());
                out.println();
            }
        }
        catch (IOException e) {
            System.out.println(e);
        }
    }
}