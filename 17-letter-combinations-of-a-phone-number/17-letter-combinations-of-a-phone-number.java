class Solution {
    ArrayList answer = new ArrayList<>();
    HashMap<String, String[]> mapping = new HashMap<String, String[]>();
    int length;
    String d;
    
    public List<String> letterCombinations(String digits) {
        length = digits.length();
        if (length == 0) {
            return new ArrayList<String>();
        }
        d = digits;
        mapping.put("2", new String[]{"a", "b", "c"});
        mapping.put("3", new String[]{"d", "e", "f"});
        mapping.put("4", new String[]{"g", "h", "i"});
        mapping.put("5", new String[]{"j", "k", "l"});
        mapping.put("6", new String[]{"m", "n", "o"});
        mapping.put("7", new String[]{"p", "q", "r", "s"});
        mapping.put("8", new String[]{"t", "u", "v"});
        mapping.put("9", new String[]{"w", "x", "y", "z"});
        helper(0, new ArrayList<>());
        return answer;
    }
    private void helper(int index, ArrayList num) {
        if (index == length) {
            answer.add(String.join("",num));
        } else {
            for(String c: mapping.get(Character.toString(d.charAt(index)))) {
                num.add(c);
                helper(index+1, num);
                num.remove(num.size()-1);
            }
        }
    }
}