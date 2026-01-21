function solution(a, b) {
    
    var num1 = Math.pow(10, b.toString().length) * a + b
    var num2 = Math.pow(10, a.toString().length)* b + a
    
    
    return num1 < num2 ? num2 : num1;
}