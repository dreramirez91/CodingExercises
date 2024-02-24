package javaExercises.ExpressionsMatter;

public class ExpressionsMatter {
    public static int expressionsMatter(int a, int b, int c) {
        return Math.max(Math.max(a + b + c, a * b * c), Math.max((a + b) * c, a * (b + c)));
    }

    public static void main(String[] args) {
        System.out.println(expressionsMatter(1, 2, 3));
    }

}
