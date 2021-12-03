package dom4jtest;

import com.sun.xml.internal.ws.developer.MemberSubmissionEndpointReference.Elements;
import org.dom4j.Attribute;
import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;

import java.util.List;

public class traverseXML{

    public static void main(String[] args) throws DocumentException{

        SAXReader reader = new SAXReader();
        Document document = reader.read("chapter05-1/src/main/java/dom4jtest/books.xml");

        Element root = document.getRootElement();

        System.out.println(root.asXML());

        List<Element> books = root.elements("book");

        for(Element book : books){
            Attribute idAttribute = book.attribute("id");
            Element nameElement = book.element("name");

            Element pricaeElement = book.element("price");

            Element authorElement = book.element("author");

            System.out.println( "id:" + idAttribute.getText()
                                + "书名:" + nameElement.getText() + "，价格："
                                + pricaeElement.getText() + "，作者：" + authorElement.getText()
             );
        }
    }
}