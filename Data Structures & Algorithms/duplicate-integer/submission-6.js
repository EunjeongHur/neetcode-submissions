class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // Create a Set because set does not contain duplicate values

        let num_maps = new Set()
        for (const i of nums) {
            if (num_maps.has(i)) { // check if num_maps alreaedy has 'i' num
                return true; // it true, that means it's duplicate values
            } 
            num_maps.add(i); // Otherwise, add that num to num_maps set
        }
        return false; // no duplicate values in nums
    }
}
