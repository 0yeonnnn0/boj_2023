class Solution {
    fun solution(numbers: IntArray): String {
    val sorted = numbers
        .map { it.toString() } // ["6" "10" "2"]
        .sortedWith { a, b ->   // "6", "10" -> 106, 610
            (b + a).compareTo(a + b)
        } // [6102, 6210, 1062, 1026, 2610, 2106]

    // 예외 처리: [0, 0, 0] 같은 경우
    if (sorted[0] == "0") return "0"

    return sorted.joinToString("")
}
}