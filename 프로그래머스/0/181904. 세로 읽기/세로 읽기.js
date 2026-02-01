function solution(my_string, m, c) {
    var answer = "";
    
    for (let i = c-1; i < my_string.length; i+=m){
        // answer.push(my_string.slice(i * m, (i+1)*m))
        answer += my_string[i]
    }
    
    return answer;
}