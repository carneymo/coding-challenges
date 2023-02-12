//https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1

/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    for(let i=0; i < nums.length; i++) {
        let pivot = i;
        let leftSum = 0;
        let rightSum = 0;

        if(i>0) {
            let leftNums = nums.slice(0,i);
            leftNums.map(x => leftSum += x);
        }

        if(i<nums.length) {
            let rightNums = nums.slice(i+1);
            rightNums.map(x => rightSum += x);
        }

        if(leftSum - rightSum == 0) {
            return pivot;
        }
    }
    return -1;
};

const test1 = [1,2,3];
const test2 = [1,7,3,6,5,6];
const test3 = [2,1,-1];

console.log(pivotIndex(test1));
console.log(pivotIndex(test2));
console.log(pivotIndex(test3));
