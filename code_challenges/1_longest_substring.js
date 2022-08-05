/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maxSubstr = "";
    let previousSubstr = new Set();
    let previousLetters = new Set();

    for (let i = 0; i < s.length; i++) {
        previousLetters.clear();
        for (let j = i; j < s.length; j++) {
            const currentLetter = s[j];
            if (previousLetters.has(currentLetter)) break;
            
            const newSubstr = s.substring(i, j + 1);
            previousLetters.add(currentLetter);
            
            if (previousSubstr.has(newSubstr)) continue;
            
            if (newSubstr.length > maxSubstr.length) maxSubstr = newSubstr;
            previousSubstr.add(newSubstr);
        }
    }
    return Number(maxSubstr.length);
};

if (typeof require !== undefined && require.main === module) {
    console.log({ result: lengthOfLongestSubstring("dvdf") })
}