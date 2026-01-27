function solution(a, b, c, d) {
    var answer = 0;
    let dice = [a, b, c, d]
    dice.sort((x, y) => x - y); 
    
    if (dice[0] === dice[3]){
        answer = 1111*dice[0]
    }
    else if (dice[0] === dice[2] && dice[0] !== dice[3]){
        answer = Math.pow((10 * dice[0] + dice[3]), 2)
    }
    else if (dice[1] === dice[3] && dice[0] !== dice[3]){
        answer = Math.pow((10 * dice[3] + dice[0]), 2)
    }
    
    else if (dice[0] === dice[1] && dice[2] === dice[3]){
        answer = (dice[0]+dice[2]) * (dice[0]-dice[3]) * (-1)
    }
    else if (dice[0] === dice[1]){
        answer = dice[2] * dice[3]
    }
    else if (dice[1] === dice[2]){
        answer = dice[0] * dice[3]
    }
    else if (dice[2] === dice[3]){
        answer = dice[0] * dice[1]
    }

    
    else if (dice[0] !== dice[1] && dice[1] !== dice[2] && dice[2] !== dice[3]){
    answer = dice[0]
    }
    
    return answer;
}