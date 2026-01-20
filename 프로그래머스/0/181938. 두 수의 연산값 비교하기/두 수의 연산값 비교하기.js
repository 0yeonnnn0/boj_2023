function solution(a, b) {
    var answer = 0
    
    var aaa = Math.pow(10, b.toString().length)
    answer = aaa * a + b
    
    var cal2 = 2*a*b
    
    if (answer < cal2){
        answer = cal2
    }
    
    
    return answer;
}