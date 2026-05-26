class Solution {
    fun solution(answers: IntArray): IntArray {
        val patterns = arrayOf(
            intArrayOf(1, 2, 3, 4, 5),
            intArrayOf(2, 1, 2, 3, 2, 4, 2, 5),
            intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
        )

        val scores = IntArray(3)

        answers.forEachIndexed { index, answer ->
            patterns.forEachIndexed { person, pattern ->
                if (answer == pattern[index % pattern.size]) {
                    scores[person]++
                }
            }
        }

        val maxScore = scores.maxOrNull() ?: 0

        return scores.indices
            .filter { scores[it] == maxScore }
            .map { it + 1 }
            .toIntArray()
    }
}