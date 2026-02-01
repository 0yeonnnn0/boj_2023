function solution(my_string, indices) {
    var answer = '';
    
    my_string.split("")
    
    for (let i = 0; i < my_string.length; i++){
        indices.includes(i) ? null : answer +=my_string[i]
    }
    
    
    return answer;
}