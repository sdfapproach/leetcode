// https://leetcode.com/problems/find-the-safest-path-in-a-grid/?envType=daily-question&envId=2026-07-01
// Find the Safest Path in a Grid

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maximumSafenessFactor = function(grid) {
    
    const n = grid.length;
    const dirs = [[0,1],[1,0],[0,-1],[-1,0]];

    const dist = Array.from({ length: n }, () => Array(n).fill(Infinity));
    const queue = [];
    let head = 0;

    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 1) {
                dist[r][c] = 0;
                queue.push([r, c]);
            }
        }
    }

    while (head < queue.length) {
        const [r, c] = queue[head++];

        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;

            if (
                nr >= 0 && nr < n &&
                nc >= 0 && nc < n &&
                dist[nr][nc] === Infinity
            ) {
                dist[nr][nc] = dist[r][c] + 1;
                queue.push([nr, nc]);
            }
        }
    }

    class MaxHeap {
        constructor() {
            this.heap = [];
        }

        push(item) {
            this.heap.push(item);
            this.bubbleUp(this.heap.length - 1);
        }

        pop() {
            if (this.heap.length === 1) return this.heap.pop();

            const top = this.heap[0];
            this.heap[0] = this.heap.pop();
            this.bubbleDown(0);
            return top;
        }

        bubbleUp(i) {
            while (i > 0) {
                const p = Math.floor((i - 1) / 2);
                if (this.heap[p][0] >= this.heap[i][0]) break;

                [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
                i = p;
            }
        }

        bubbleDown(i) {
            const n = this.heap.length;

            while (true) {
                let largest = i;
                const l = i * 2 + 1;
                const r = i * 2 + 2;

                if (l < n && this.heap[l][0] > this.heap[largest][0]) {
                    largest = l;
                }

                if (r < n && this.heap[r][0] > this.heap[largest][0]) {
                    largest = r;
                }

                if (largest === i) break;

                [this.heap[i], this.heap[largest]] = [this.heap[largest], this.heap[i]];
                i = largest;
            }
        }

        size() {
            return this.heap.length;
        }
    }

    const visited = Array.from({ length: n }, () => Array(n).fill(false));
    const heap = new MaxHeap();

    heap.push([dist[0][0], 0, 0]);
    visited[0][0] = true;

    while (heap.size()) {
        const [safe, r, c] = heap.pop();

        if (r === n - 1 && c === n - 1) {
            return safe;
        }

        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;

            if (
                nr >= 0 && nr < n &&
                nc >= 0 && nc < n &&
                !visited[nr][nc]
            ) {
                visited[nr][nc] = true;
                heap.push([
                    Math.min(safe, dist[nr][nc]),
                    nr,
                    nc
                ]);
            }
        }
    }

    return 0;
};