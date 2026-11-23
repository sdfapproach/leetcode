// https://leetcode.com/problems/product-of-the-last-k-numbers/?envType=daily-question&envId=2026-11-23
// Product of the Last K Numbers

var ProductOfNumbers = function() {
    this.prefixProducts = [1];

};

/** 
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    if (num === 0) {
        this.prefixProducts = [1];
    } else {
        const last = this.prefixProducts[this.prefixProducts.length - 1];
        this.prefixProducts.push(last * num);
    }
};

/** 
 * @param {number} k
 * @return {number}
 */
ProductOfNumbers.prototype.getProduct = function(k) {
    const n = this.prefixProducts.length;

    if (k >= n) {
        return 0;
    }

    return this.prefixProducts[n - 1] /
           this.prefixProducts[n - k - 1];
};

/** 
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */