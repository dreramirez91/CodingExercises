package javaExercises.CuboidVolumes;

import java.lang.Math;

public class CuboidVolumes {
    public static int findDifference(final int[] firstCuboid, final int[] secondCuboid) {
        int firstVolume = 1, secondVolume = 1;
        for (int side : firstCuboid) {
            firstVolume *= side;
        }
        for (int side : secondCuboid) {
            secondVolume *= side;
        }
        return Math.abs(firstVolume - secondVolume);
    }

    public static void main(String[] args) {
        System.out.println(findDifference(new int[] { 3, 2, 5 }, new int[] { 1, 4, 4 }));
    }
}
