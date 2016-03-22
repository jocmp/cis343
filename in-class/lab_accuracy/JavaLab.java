public class JavaLab {
    
    private static int a = 5;

    public static void main(String[] args) {    
        a = a + fun();
        System.out.println("This is 'a': " + a);
    }

    private static int fun() {
        a = 17;
        return 3;
    }
}
