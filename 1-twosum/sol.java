import java.util.*;

class node implements Comparable<node>{
    int idx;
    int value;

    public node(int idx, int value){
        this.idx =idx;
        this.value =value;
    }
    @Override
    public int compareTo(node o1){
        return this.value - o1.value;
    }
}
class Solution {
    // java의 sort가 nlogn인 것을 이용해
    // 투 포인트로 풀었다.
    public int[] twoSum(int[] nums, int target) {
        ArrayList<node> no = new ArrayList<>();
        for(int i=0; i<nums.length; i++){
            no.add(new node(i,nums[i]));
        }
        Collections.sort(no);
        int i=0;
        int j=nums.length-1;
        while(i<j){
            int sum= no.get(i).value + no.get(j).value;
            if(sum==target) return new int[]{no.get(i).idx, no.get(j).idx};
            else if(sum<target) i++;
            else j--;
        }
        return new int[]{0,0};
    }
}