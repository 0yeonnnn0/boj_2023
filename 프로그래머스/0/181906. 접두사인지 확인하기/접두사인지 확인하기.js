function solution(my_string, is_prefix) {
    var answer = 0;
    
    answer = my_string.startsWith(is_prefix)
    
    return Number(answer);
}