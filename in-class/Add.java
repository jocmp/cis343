

public class Add {

  public static void main(String args[]) {
    Add add = new Add();
    int firstParam = Integer.parseInt(args[0]);
    int secondParam = Integer.parseInt(args[1]);

    double doubleFirst = Double.parseDouble(args[0]);
    double doubleSecond = Double.parseDouble(args[1]);

    int impreciseResult = add.add(firstParam, secondParam);
    double result = add.add(doubleFirst, doubleSecond);
    System.out.printf("This is confusing int: %d", impreciseResult);
    System.out.printf("This is confusing int: %f", result);
  }

  private double add(double x, double y) {
    return x + y;
  }

  private int add(int dx, int dy) {
    return dx + dy;
  }
}
