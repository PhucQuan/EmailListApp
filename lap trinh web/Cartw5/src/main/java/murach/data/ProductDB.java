package murach.data;

import murach.business.Product;
import java.util.ArrayList;

public class ProductDB {
    
    public static ArrayList<Product> getProducts() {
        ArrayList<Product> products = new ArrayList<>();
        
        Product p1 = new Product();
        p1.setProductId(1L);
        p1.setCode("8601");
        p1.setDescription("86 (the band) - True Life Songs and Pictures");
        p1.setPrice(14.95);
        products.add(p1);
        
        Product p2 = new Product();
        p2.setProductId(2L);
        p2.setCode("pf01");
        p2.setDescription("Paddlefoot - The first CD");
        p2.setPrice(12.95);
        products.add(p2);
        
        Product p3 = new Product();
        p3.setProductId(3L);
        p3.setCode("pf02");
        p3.setDescription("Paddlefoot - The second CD");
        p3.setPrice(14.95);
        products.add(p3);
        
        Product p4 = new Product();
        p4.setProductId(4L);
        p4.setCode("jr01");
        p4.setDescription("Joe Rut - Genuine Wood Grained Finish");
        p4.setPrice(14.95);
        products.add(p4);
        
        return products;
    }
    
    public static Product getProduct(String productCode) {
        ArrayList<Product> products = getProducts();
        for (Product p : products) {
            if (p.getCode().equals(productCode)) {
                return p;
            }
        }
        return null;
    }
}