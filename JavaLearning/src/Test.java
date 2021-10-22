import java.util.LinkedList;
import java.util.List;

public class Test {
    public static void main(String[] args) {
        LinkedList<Integer> res = new LinkedList<>();
        res.add(1);
        res.add(2);
        res.add(1);
        List<Integer> ans = res;
        System.out.println(res);
    }
}
