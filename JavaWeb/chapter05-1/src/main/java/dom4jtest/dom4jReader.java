package dom4jtest;

import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.io.SAXReader;

public class dom4jReader{
    public static void main(String[] args) throws DocumentException {
        SAXReader reader = new SAXReader();
        Document document =  reader.read("chapter05-1/src/main/java/dom4jtest/books.xml");
        System.out.println(document);
    }
}
