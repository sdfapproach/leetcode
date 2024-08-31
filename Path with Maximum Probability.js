// https://leetcode.com/problems/path-with-maximum-probability/?envType=daily-question&envId=2024-08-31
// Path with Maximum Probability

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} succProb
 * @param {number} start_node
 * @param {number} end_node
 * @return {number}
 */
var maxProbability = function(n, edges, succProb, start_node, end_node) {
    
    const graph = new Map();

    for (let i = 0; i < edges.length; i++) {
        const [a, b] = edges[i];
        if (!graph.has(a)) graph.set(a, []);
        if (!graph.has(b)) graph.set(b, []);
        graph.get(a).push([b, succProb[i]]);
        graph.get(b).push([a, succProb[i]]);
    }

    const maxProb = new Array(n).fill(0);
    maxProb[start_node] = 1;

    const pq = new MinPriorityQueue({ compare: (a, b) => b.prob - a.prob });
    pq.enqueue({ node: start_node, prob: 1 });

    while (!pq.isEmpty()) {
        const { node, prob } = pq.dequeue();

        if (node === end_node) return prob;

        const neighbors = graph.get(node) || [];
        for (const [neighbor, edgeProb] of neighbors) {
            const newProb = prob * edgeProb;
            if (newProb > maxProb[neighbor]) {
                maxProb[neighbor] = newProb;
                pq.enqueue({ node: neighbor, prob: newProb });
            }
        }
    }

    return 0;
};