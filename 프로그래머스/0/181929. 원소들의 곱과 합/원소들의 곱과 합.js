function solution(num_list) {
    var answer = 0
    
    var gop = 1
    var zegop = 0

    for (let i = 0; i < num_list.length; i++){
        gop *= num_list[i];
        zegop += num_list[i];
    }
    
    if (gop < Math.pow(zegop, 2)){
        answer = 1
    }

    return answer;
}