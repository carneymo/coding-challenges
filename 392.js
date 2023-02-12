/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let curIndex = 0;
    if(s.length == 0) return true;
    for(let i=0; i<t.length; i++) {
        if(t[i] === s[curIndex]) {
            curIndex++;
            if(curIndex === s.length) {
                return true;
            }
        }
    }
    return false;
};


console.log(isSubsequence("abc", "ahbgdc"));
console.log(isSubsequence("axc", "ahbgdc"));