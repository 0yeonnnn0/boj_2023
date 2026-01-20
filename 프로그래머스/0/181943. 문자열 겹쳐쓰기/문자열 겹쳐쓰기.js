function solution(my_string, overwrite_string, s) {
    let overwrite_num = 0
    let arr = my_string.split('');

    for (let i = 0; i < overwrite_string.length; i++){
        arr[s + i] = overwrite_string[i];
    }
    
    let answer = arr.join("")

    return answer;
}