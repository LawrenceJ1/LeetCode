/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return node;
        }
        Map<Node, Node> nodes = new HashMap<>();
        nodes.put(node, new Node(node.val));
        cloneNeighbours(node, nodes);
        return nodes.get(node);
    }
    private void cloneNeighbours(Node node, Map<Node, Node> nodes) {
        for(Node neighbour: node.neighbors) {
            if (!nodes.containsKey(neighbour)) {
                nodes.put(neighbour, new Node(neighbour.val));
                cloneNeighbours(neighbour, nodes);
            }
            nodes.get(node).neighbors.add(nodes.get(neighbour));
        }
    }
}