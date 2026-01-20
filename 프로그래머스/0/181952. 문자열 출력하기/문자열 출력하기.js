const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
    rl.close();          // 더 이상 입력 안 받으니 닫기

}).on('close',function(){
    str = input[0];
    console.log(str);      // 그대로 출력
});
