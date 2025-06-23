public class TriangleSum {
  public static long sumOddNumbersRow(int n) {
    return n * n * n;
  }

  public static void main(String[] args) {
    // Example usage
    int n = 5; // Row number
    long sum = sumOddNumbersRow(n);
    System.out.println("The sum of the odd numbers in row " + n + " is: " + sum);
  }
}