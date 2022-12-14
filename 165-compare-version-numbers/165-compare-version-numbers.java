class Solution {
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\.");
        String[] v2 = version2.split("\\.");
        for (int i = 0; i < Math.max(v1.length, v2.length); i++) {
            int temp1 = i < v1.length ? Integer.parseInt(v1[i]) : 0;
            int temp2 = i < v2.length ? Integer.parseInt(v2[i]) : 0;
            if (temp1 > temp2) {
                return 1;
            } else if (temp2 > temp1) {
                return -1;
            }
        }
        return 0;
    }
}