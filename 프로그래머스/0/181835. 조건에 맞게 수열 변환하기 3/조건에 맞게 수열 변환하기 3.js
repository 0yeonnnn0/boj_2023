function solution(arr, k) {
    var answer = [];
    
    for (let i = 0; i < arr.length; i++){
        k % 2 == 0 ? arr[i] += k : arr[i] *= k
    }
    
    return arr;
}