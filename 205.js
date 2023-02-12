/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    for(let i=0; i<s.length;i++) {
        s=s.replaceAll(s[i],t[i]);
        if(s === t) return true;
    }
    return false;
};

const test1 = ["egg", "add"];
const test2 = ["foo", "bar"];
const test3 = ["paper", "title"];

console.log(isIsomorphic(test1[0], test1[1]));
console.log(isIsomorphic(test2[0], test2[1]));
console.log(isIsomorphic(test3[0], test3[1]));