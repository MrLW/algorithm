/**
 * Initialize your data structure here.
 */
var MyHashMap = function () {
  this.seed = 1001;
  this.table = new Array(this.seed).fill(0);
};

/**
 * value will always be non-negative.
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function (key, value) {
  var node = new Node(key, value);
  var head = this.table[this.hash(key)];
  if (!head) {
    this.table[this.hash(key)] = node;
    return;
  }
  var last;
  while (head) {
    if (head.key == key) {
      head.value = value;
      return;
    }
    last = head;
    head = head.next;
  }
  last.next = node;
};

/**
 * Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function (key) {
  var hashKey = this.hash(key);
  var head = this.table[hashKey];
  while (head) {
    if (head.key == key) {
      return head.value;
    }
    head = head.next;
  }
  return -1;
};

/**
 * Removes the mapping of the specified value key if this map contains a mapping for the key
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function (key) {
  var hashKey = this.hash(key);
  var head = this.table[hashKey];
  if (!head) {
    return;
  }
  // 如果删除的是table的第一个元素
  if (head.key == key) {
    this.table[hashKey] = head.next;
    return;
  }
  var last;
  while (head) {
    if (head.key == key) {
      last.next = head.next;
      return;
    }
    last = head;
    head = head.next;
  }
};

MyHashMap.prototype.hash = function (key) {
  return key % this.seed;
};

function Node(key, value) {
  this.key = key;
  this.value = value;
  this.next = null;
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
// ["MyHashMap","get","put","put","put","remove","put","put","put","get","put","put","put","put","get","put","get","put","put","put","put","remove","put","put","put","put","put","put","put","get","put","put","put","put","put","put","put","put","put","put","put","put","put","remove","put","remove","put","remove","put","remove","put","put","put","remove","put","put","put","put","get","put","put","put","get","remove","put","put","put","put","remove","put","put","put","get","put","put","get","get","put","put","put","put","put","put","put","put","get","put","put","put","get","get","remove","remove","put","get","get","put","get","put","put","get"]
// [[],[79],[72,7],[77,1],[10,21],[26],[94,5],[53,35],[34,9],[94],[96,8],[73,79],[7,60],[84,79],[94],[18,13],[18],[69,34],[21,82],[57,64],[23,60],[0],[12,97],[56,90],[44,57],[30,12],[17,10],[42,13],[62,6],[34],[70,16],[51,39],[22,98],[82,42],[84,7],[29,32],[96,54],[57,36],[85,82],[49,33],[22,14],[63,8],[56,8],[94],[78,77],[51],[20,89],[51],[9,38],[20],[29,64],[92,69],[72,25],[73],[6,90],[1,67],[70,83],[58,49],[79],[73,2],[56,16],[58,26],[53],[7],[27,17],[55,40],[55,13],[89,32],[49],[75,75],[64,52],[94,74],[81],[39,82],[47,36],[57],[66],[3,7],[54,34],[56,46],[58,64],[22,81],[3,1],[21,96],[6,19],[77],[60,66],[48,85],[77,16],[78],[23],[72],[27],[20,80],[30],[94],[74,85],[49],[79,59],[15,15],[26]]
var map = new MyHashMap();
map.put(94, 5);
map.put(91, 1);
map.put(92, 2);
console.info(map.get(94));
map.remove(94);
console.info(map.get(94));
map.put(94, 3);
console.info(map.get(94));
