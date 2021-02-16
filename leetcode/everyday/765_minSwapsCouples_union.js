/**
 * 并查集 
 */
class UnionFind {

    constructor(n){
        // 连通数量
        this.count = n;
        this.parent = [];
        this.rank = [];
        // 初始化, 每个元素的父节点都是自己
        for(let i = 0 ;i < n; i++){
            this.parent[i] = i;
            this.rank[i] = 0;
        }
    }

    union(i,j){
        let i_root = this.find(i);
        let j_root = this.find(j);
        if(i_root == j_root) {
            return ;
        }
        if(this.rank[i_root] <= this.rank[j_root]){
            this.parent[i_root] = j_root;
        }else {
            this.parent[i_root] = j_root;
        }
        if(this.rank[i_root] == this.rank[j_root]){
            this.rank[j_root]++;
        }
        this.count--;
    }
    find(x){
        if(this.parent[x] == x) return x;
        // 路径压缩
        this.parent[x] = this.find(this.parent[x]);
        return this.parent[x];
    }
    getCount(){
        return this.count;
    }
}

var minSwapsCouples = function (nums) {
    let len = nums.length;
    let N = len/2;
    let uf = new UnionFind(N);
    for(let i = 0 ; i < len; i+=2 ){
        uf.union(Math.floor(row[i]/2), Math.floor(row[i+1]/2));
    }
    return N - uf.getCount();
}

let row = [5,6,4,0,2,1,9,3,8,7,11,10];
const result = minSwapsCouples(row);
console.info(result);