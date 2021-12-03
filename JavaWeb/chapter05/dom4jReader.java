
public class dom4jReader{
    public static void main(String[] args) {
        SAXReader reader = new SAXReader();
        Document document =  reader.read("books.xml");
        System.out.println(document);
    }
}
