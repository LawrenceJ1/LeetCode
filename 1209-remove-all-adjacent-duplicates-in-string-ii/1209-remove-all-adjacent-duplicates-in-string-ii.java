class Solution {
    public String removeDuplicates(String s, int k) {
        Deque<ArrayList> deque = new ArrayDeque<ArrayList>();
        ArrayList ret = new ArrayList<>();
        for(int i = 0; i < s.length(); i++) {
            ArrayList x = new ArrayList<>();
            if(deque.size() >= 1 && deque.getLast().get(0).equals(Character.toString(s.charAt(i)))) {
                x.add(Character.toString(s.charAt(i)));
                x.add((int)deque.removeLast().get(1)+1);
                deque.add(x);
            } else {
                x.add(Character.toString(s.charAt(i)));
                x.add(1);
                deque.add(x);
            }
            if((int)deque.getLast().get(1) == k) {
                deque.removeLast();
            }
        }
        while(deque.size() != 0) {
            String a;
            int b;
            ArrayList x = deque.removeFirst();
            a = (String)x.get(0);
            b = (int)x.get(1);
            for(int i = 0; i < b; i++) {
                ret.add(a);
            }
        }
        return String.join("", ret);
    }
}