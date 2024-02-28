public class Square {
    public static boolean isSquare(int n) {
        // ! Typecast using (dataType) value;
        return Math.sqrt(n) == (int) Math.sqrt(n);
        // ! To find if something is an int, simply check if % 1 == 0
        // return Math.sqrt(n) % 1 == 0;
    }

    public static void main(String[] args) {
        System.out.println(Square.isSquare(4));
    }
}
