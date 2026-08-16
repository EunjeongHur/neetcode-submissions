class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // Create a hash map {input_num: num_count}
        let num_maps = new Set()
        for (const i of nums) {
            if (num_maps.has(i)) {
                return true;
            } 
            num_maps.add(i);
        }
        return false;
    }
}
