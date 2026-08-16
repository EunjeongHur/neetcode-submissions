class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // Make hash tables for s & t, and add the character as a key 
        // # of character as a value
        // Lastly, compare two hashmaps
        // If same, it's anagram
        
        // compare length first

        if (s.length !== t.length) {
            return false;
        }

        // Will create an character array 
        // [0, 0, 0, 0, ...] (same as values for key [a, b, c, d, ...])
        const count = new Array(26).fill(0);
        for (let i = 0; i < s.length; i++) {
            count[s.charCodeAt(i) - 'a'.charCodeAt(0)]++; //add the character to array
            count[t.charCodeAt(i) - 'a'.charCodeAt(0)]--; // eliminate the value in array
        }
        return count.every(val => val === 0);
    }
}
