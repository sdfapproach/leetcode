// https://leetcode.com/problems/count-the-number-of-complete-components/?envType=daily-question&envId=2026-07-11
// Count the Number of Complete Components

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countCompleteComponents = function(n, edges) {
    
    const graph = Array.from({ length: n }, () => new Set());

    for (const [u, v] of edges) {
        graph[u].add(v);
        graph[v].add(u);
    }

    const visited = new Array(n).fill(false);
    let completeCount = 0;

    function bfs(start) {
        const queue = [start];
        let head = 0;
        const component = [];

        visited[start] = true;

        while (head < queue.length) {
            const node = queue[head++];
            component.push(node);

            for (const neighbor of graph[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.push(neighbor);
                }
            }
        }

        return component;
    }

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            const component = bfs(i);
            const componentSet = new Set(component);
            const k = component.length;

            let isComplete = true;

            for (const node of component) {
                let neighborCount = 0;

                for (const neighbor of graph[node]) {
                    if (componentSet.has(neighbor)) {
                        neighborCount++;
                    }
                }

                if (neighborCount !== k - 1) {
                    isComplete = false;
                    break;
                }
            }

            if (isComplete) {
                completeCount++;
            }
        }
    }

    return completeCount;
};