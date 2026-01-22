function solution(arr, queries) {
    var answer = [];
    
    for (let i = 0; i < queries.length; i++){
        let s = queries[i][0]
        let e = queries[i][1]
        let k = queries[i][2]
        
        let tmp = Infinity
        
        for (let j = s; j <= e; j++){
            if (arr[j] > k && tmp > arr[j]){
                tmp = arr[j]
        }
        }
        
        tmp == Infinity ? answer.push(-1) : answer.push(tmp)
    }
    
    return answer;
}