/*
 * @Author: leekwe 
 * @Date: 2019-06-14 16:14:46 
 * @Last Modified by: leekwe
 * @Last Modified time: 2019-06-14 18:25:32
 */
const fs = require('fs');
const path = require('path');
let data = require('../data.json');
// 存储原始数据,防止经过第一次排序后的排序都是已排序好的数据
let source = new Array().concat(data);
// 是否打印数据输出日志
let debug = false; 
fs.readdir(__dirname+"/",(err,files)=>{
  files.forEach(file=>{
    if(file!==path.basename(__filename)){
      console.time(file + `================数据量为${data.length}耗时`)
      let sortDatas=  require(__dirname + "/" + file)(data,0,data.length-1);
      console.timeEnd(file + `================数据量为${data.length}耗时`)
      if(debug){
        console.log("排序前原始数据",data)
        console.log("排序后数据",sortDatas)
      }
      data = new Array().concat(source);
    }
  })
})
