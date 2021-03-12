/**
 * @param {string} preorder
 * @return {boolean}
 */
var isValidSerialization = function (preorder) {
    let i = 0, stack = new Array();
    preorder = preorder.split(',');
    while (i < preorder.length) {
        stack.push(preorder[i]);
        while (stack.length >= 3 && stack[stack.length - 1] == '#' && stack[stack.length - 2] == '#' && stack[stack.length - 3] != '#') {
            stack.pop();
            stack.pop();
            stack.pop();
            stack.push('#');
        }
        i++;
    }
    return stack.length == 1 && stack[0] == '#';
};

console.info(isValidSerialization("9,3,1,#,#,4,#,#,2,#,6,#,#"))

//      _9_
//     /     \
//    3      2
//   / \    /  \
//  1   4  #   6
//  / \  / \   / \
// #  # #  #   # #


// 9 3 1 #