public class Solution {
    private void postorder(Node root, List<int> list){
        if(root == null){
            return;
        }

        for(int i = 0; i < root.children.Count; i++){
            postorder(root.children[i], list);
        }

        list.Add(root.val);
    }

    public IList<int> Postorder(Node root) {
        List<int> list = new List<int>();
        postorder(root, list);
        return(list);
    }
}
