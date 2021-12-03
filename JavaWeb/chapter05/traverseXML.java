
public class traverseXML{

    public void readXML() throws DocuentException{

        SAXReader reader = new SAXReader();
        Document document = reader.read("books.xml");

        Element root = document.getRootElement();

        System.out.println(root.asXML());

        List<Element> books = root.elements("books");

        for(Element book : books){
            Elements nameElement = book.element("name");

            Elements pricaeElement = book.element("price");

            Elements authorElement = book.element("author");

            System.out.println("书名" + nameElement.getText() + "，价格："
                                + pricaeElement.getText() + "，作者：" + authorElement.getText()
             );
        }
    }
}