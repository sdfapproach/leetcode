// https://leetcode.com/problems/trapping-rain-water-ii/?envType=daily-question&envId=2025-10-03
// Trapping Rain Water II

/**
 * @param {number[][]} heightMap
 * @return {number}
 */
var trapRainWater = function(heightMap) {
/**
 * @param {number[][]} heightMap
 * @return {number}
 */
    if (!heightMap || !heightMap[0]) {
        return 0;
    }
    
    const m = heightMap.length;
    const n = heightMap[0].length;
    
    class MinHeap {
        constructor() {
            this.heap = [];
        }
        
        push(val) {
            this.heap.push(val);
            this.bubbleUp(this.heap.length - 1);
        }
        
        pop() {
            if (this.heap.length === 0) return null;
            if (this.heap.length === 1) return this.heap.pop();
            
            const min = this.heap[0];
            this.heap[0] = this.heap.pop();
            this.bubbleDown(0);
            return min;
        }
        
        bubbleUp(idx) {
            while (idx > 0) {
                const parentIdx = Math.floor((idx - 1) / 2);
                if (this.heap[idx][0] >= this.heap[parentIdx][0]) break;
                [this.heap[idx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[idx]];
                idx = parentIdx;
            }
        }
        
        bubbleDown(idx) {
            while (true) {
                let minIdx = idx;
                const left = 2 * idx + 1;
                const right = 2 * idx + 2;
                
                if (left < this.heap.length && this.heap[left][0] < this.heap[minIdx][0]) {
                    minIdx = left;
                }
                if (right < this.heap.length && this.heap[right][0] < this.heap[minIdx][0]) {
                    minIdx = right;
                }
                
                if (minIdx === idx) break;
                [this.heap[idx], this.heap[minIdx]] = [this.heap[minIdx], this.heap[idx]];
                idx = minIdx;
            }
        }
        
        isEmpty() {
            return this.heap.length === 0;
        }
    }
    
    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const heap = new MinHeap();
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 || j === 0 || i === m - 1 || j === n - 1) {
                heap.push([heightMap[i][j], i, j]);
                visited[i][j] = true;
            }
        }
    }
    
    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    let waterTrapped = 0;
    
    while (!heap.isEmpty()) {
        const [height, x, y] = heap.pop();
        
        for (const [dx, dy] of directions) {
            const nx = x + dx;
            const ny = y + dy;
            
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny]) {
                waterTrapped += Math.max(0, height - heightMap[nx][ny]);
                heap.push([Math.max(height, heightMap[nx][ny]), nx, ny]);
                visited[nx][ny] = true;
            }
        }
    }
    
    return waterTrapped;
};