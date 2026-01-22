function solution(my_string, is_suffix) {
    var answer = 0;
    
    answer = my_string.slice(my_string.length-is_suffix.length)
    
    
    return is_suffix == my_string.slice(my_string.length-is_suffix.length) ? 1 : 0;
}