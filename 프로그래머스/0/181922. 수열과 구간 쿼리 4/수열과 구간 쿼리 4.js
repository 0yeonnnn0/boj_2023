function solution(arr, queries) {
    var answer = [];
    
    for (let i = 0; i < queries.length; i++){
        let s = queries[i][0]
        let e = queries[i][1]
        let k = queries[i][2]
        
        for (let j = s; j <= e; j++){
            if (j % k === 0){
                arr[j] += 1
            }
        }
        
    }
    
    answer = arr
    
    return answer;
}